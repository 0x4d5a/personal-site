#!/usr/bin/env python3
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

REPO_ROOT = Path(__file__).resolve().parent.parent
ALLOWED_SCHEMES = {"mailto", "tel"}


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []
        self.has_title = False
        self.has_h1 = False
        self.has_csp_meta = False

    def handle_starttag(self, tag: str, attrs) -> None:  # noqa: ANN001
        attrs_dict = dict(attrs)
        if tag == "a" and "href" in attrs_dict:
            self.links.append(attrs_dict["href"])
        if tag in {"img", "script", "link"} and "src" in attrs_dict:
            self.links.append(attrs_dict["src"])
        if tag == "title":
            self.has_title = True
        if tag == "h1":
            self.has_h1 = True
        if tag == "meta" and attrs_dict.get("http-equiv", "").lower() == "content-security-policy":
            self.has_csp_meta = True


def resolve_link(source_file: Path, href: str) -> Path | None:
    if href.startswith("#") or href.startswith("javascript:") or href.startswith("data:"):
        return None

    parsed = urlparse(href)
    if parsed.scheme:
        if parsed.scheme in ALLOWED_SCHEMES:
            return None
        if parsed.scheme == "https":
            return None
        if parsed.scheme == "http" and parsed.netloc in {"127.0.0.1:4000", "localhost:4000"}:
            return None
        raise ValueError(f"disallowed external scheme in link '{href}'")

    clean_href = href.split("#", 1)[0].split("?", 1)[0]
    if not clean_href:
        return None

    if clean_href.startswith("/"):
        candidate = REPO_ROOT / clean_href.lstrip("/")
    else:
        candidate = source_file.parent / clean_href

    if candidate.is_dir():
        candidate = candidate / "index.html"

    if candidate.suffix == "":
        candidate_index = candidate / "index.html"
        if candidate_index.exists():
            candidate = candidate_index

    return candidate


def validate_html_file(path: Path) -> list[str]:
    parser = LinkParser()
    parser.feed(path.read_text(encoding="utf-8"))

    errors: list[str] = []

    if not parser.has_title:
        errors.append(f"{path}: missing <title>")
    if not parser.has_h1:
        errors.append(f"{path}: missing <h1>")
    if not parser.has_csp_meta:
        errors.append(f"{path}: missing CSP <meta http-equiv='Content-Security-Policy'>")

    for href in parser.links:
        try:
            target = resolve_link(path, href)
        except ValueError as exc:
            errors.append(f"{path}: {exc}")
            continue

        if target is None:
            continue

        if not target.exists():
            errors.append(f"{path}: broken internal link '{href}' -> '{target.relative_to(REPO_ROOT)}'")

    return errors


def main() -> int:
    html_files = sorted(REPO_ROOT.rglob("*.html"))
    errors: list[str] = []

    if not html_files:
        print("No HTML files found")
        return 1

    for html_file in html_files:
        errors.extend(validate_html_file(html_file))

    if errors:
        print("Site validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    print(f"Site validation passed for {len(html_files)} HTML file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

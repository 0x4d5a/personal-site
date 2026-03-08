# GitHub Pages Development Workflow

## Local preview
```bash
./scripts/serve.sh
```
Open `http://127.0.0.1:4000`.

## Local validation
```bash
./scripts/check.sh
```
This checks:
- required `title` and `h1` in each page
- CSP meta tag exists
- internal links are valid
- only `https` external links are allowed

## Publishing flow
1. Create a branch from `main`.
2. Make content edits.
3. Run local validation.
4. Open a pull request.
5. Ensure `Site CI` passes.
6. Merge PR to `main`.
7. GitHub Pages publishes from `main` automatically.

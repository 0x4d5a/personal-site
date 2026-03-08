# personal-site

Static website hosted on GitHub Pages.

## Structure
- `index.html`: homepage
- `about.html`: about page
- `blog/index.html`: blog landing placeholder
- `styles.css`: shared styles

## Local development
- Preview locally:
  - `./scripts/serve.sh`
- Run site checks:
  - `./scripts/check.sh`

## GitHub Pages publish
1. Push to `main` in repository `personal-site`.
2. GitHub Pages publishes from branch `main` and folder `/`.
3. Optional custom domain: set it in repository settings.
4. For apex domain on DreamHost DNS, add GitHub Pages A records:
   - `185.199.108.153`
   - `185.199.109.153`
   - `185.199.110.153`
   - `185.199.111.153`

## Pull request flow
1. Create a branch from `main`.
2. Make content changes.
3. Run `./scripts/check.sh` locally.
4. Open a pull request.
5. Wait for `Site CI` to pass.
6. Merge to `main`.

## Security checklist
- Enforce HTTPS in Pages settings.
- Enable Dependabot and secret scanning.
- Keep repository free of secrets.

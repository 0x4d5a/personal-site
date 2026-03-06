# personal-site

Static website hosted on GitHub Pages for `yourdomain.com`.

## Structure
- `index.html`: homepage
- `about.html`: about page
- `blog/index.html`: blog landing placeholder
- `styles.css`: shared styles

## GitHub Pages
1. Push to GitHub repository `personal-site`.
2. Enable GitHub Pages using GitHub Actions.
3. Set custom domain to `yourdomain.com` in repository settings.
4. In DreamHost DNS, add apex A records for GitHub Pages:
   - `185.199.108.153`
   - `185.199.109.153`
   - `185.199.110.153`
   - `185.199.111.153`

## Security checklist
- Enforce HTTPS in Pages settings.
- Enable Dependabot and secret scanning.
- Keep repository free of secrets.

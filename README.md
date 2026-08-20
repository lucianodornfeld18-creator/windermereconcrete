# Windermere Concrete

Static local-service website for `windermereconcrete.com`, generated with Python and deployed to Cloudflare Pages.

## Build

Regenerate the site pages:

```bash
python build_all.py
```

Prepare the publishable Pages output in `dist/`:

```bash
npm run build
```

The packaging step excludes generator source files, internal audit notes, and the `preview-homes/` concepts from the deployed site.

## Cloudflare Pages

- Project name: `windermereconcrete`
- Production branch: `main`
- Build command: `npm run build`
- Build output directory: `dist`

## Launch inputs still required

Before the custom domain is made public, replace the unresolved business placeholders documented in `WHAT-I-NEED-FROM-YOU.md`, especially the phone number, email address, and form endpoint. The image manifest in `images/IMAGE-MANIFEST.md` also lists the production images that are still missing.

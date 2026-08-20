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

## Contact delivery

- Public email: `hello@windermereconcrete.com`
- All addresses on the domain forward through Cloudflare Email Routing.
- The contact form posts to `/api/contact`, a Pages Function that calls the private `windermereconcrete-contact` Worker through a service binding.
- The Worker sends the lead with its `EMAIL` binding. Its destination is stored in the `CONTACT_DESTINATION` Worker secret and is intentionally not committed.

Deploy the private email Worker with:

```bash
npm run deploy:email-worker
```

## Cloudflare Pages

- Project name: `windermereconcrete`
- Production branch: `main`
- Build command: `npm run build`
- Build output directory: `dist`

## Remaining launch inputs

The image manifest in `images/IMAGE-MANIFEST.md` lists the production images that are still missing. Other non-contact business placeholders are documented in `WHAT-I-NEED-FROM-YOU.md`.

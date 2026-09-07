# dragan.me

Static site on GitHub Pages (`CNAME` → dragan.me). Push to `main` deploys.

`index.html`, `404.html`, `legal/*.html` and `support/*.html` are **generated**
(`build/site.py`, `build/legal.py` → `build/site/`, copied over the tracked
dirs, `build/site/` deleted afterwards). Never hand-edit them.

`.nojekyll` is load-bearing: without it Jekyll drops every dot-directory and
`/.well-known/` would 404.

## ⚠️ TODO — Android App Links are only half-verified

`.well-known/assetlinks.json` lists ONE fingerprint: the local **upload** key.
With Play App Signing there is a second one — the key Google re-signs with —
and it is not known yet (Play Console → Setup → App signing). Until it is added,
`https://dragan.me/bibliada/i/<code>` opens the app for locally-installed builds
and falls through to the browser for **everyone who installed from Play**.

A bogus placeholder cannot be parked in the file: one malformed fingerprint
invalidates the whole statement, so the miss is silent. This note is the alarm.
Keep in sync with `bibliada-api/src/app/modules/auth/controller/well-known.controller.ts`.

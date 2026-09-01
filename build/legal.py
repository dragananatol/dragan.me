#!/usr/bin/env python3
"""Bibliada — legal.html + support.html, in stilul dragan.me. Minim necesar pentru App Store / Play."""
import pathlib, importlib.util
HERE = pathlib.Path(__file__).parent
spec = importlib.util.spec_from_file_location("sitemod", HERE / "site.py")
sitemod = importlib.util.module_from_spec(spec); spec.loader.exec_module(sitemod)
page = sitemod.page
OUT = HERE / "site"; (OUT/"legal").mkdir(parents=True, exist_ok=True); (OUT/"support").mkdir(exist_ok=True)

UPDATED = "31 August 2026"

LEGAL_CSS = """
  .doc{padding:clamp(48px,8vh,92px) 0 0;max-width:760px}
  .doc h1{font-family:var(--display);font-weight:300;font-size:clamp(34px,5vw,58px);line-height:1.05;letter-spacing:-.01em;margin:18px 0 10px}
  .doc .upd{font-size:10px;letter-spacing:.24em;text-transform:uppercase;color:var(--muted)}
  .toc{display:flex;gap:8px;flex-wrap:wrap;margin:28px 0 8px}
  .toc a{font-size:10px;letter-spacing:.2em;text-transform:uppercase;text-decoration:none;color:var(--muted);
    border:1px solid var(--line);border-radius:100px;padding:9px 15px;transition:.25s}
  .toc a:hover{color:var(--ink);border-color:var(--edge)}
  .sec{padding:clamp(40px,6vh,64px) 0 0}
  .sec > h2{font-family:var(--display);font-weight:400;font-size:clamp(24px,3vw,34px);margin-bottom:6px}
  .sec > .num{font-size:10px;letter-spacing:.26em;color:var(--muted)}
  .sec h3{font-size:12px;font-weight:400;letter-spacing:.2em;text-transform:uppercase;margin:26px 0 8px}
  .sec p{font-size:15px;color:var(--muted);margin-bottom:12px}
  .sec ul{margin:0 0 12px 18px}
  .sec li{font-size:15px;color:var(--muted);margin-bottom:7px}
  .sec strong{color:var(--ink);font-weight:400}
  .sec a{color:var(--ink);text-decoration:none;border-bottom:1px solid var(--line)}
  .sec a:hover{border-color:var(--ink)}
  .note{border-left:1px solid var(--edge);padding:4px 0 4px 18px;margin:18px 0}
  .back{font-size:10px;letter-spacing:.24em;text-transform:uppercase;color:var(--muted);text-decoration:none}
  .back:hover{color:var(--ink)}
"""

def sec(num, title, html, sid):
    return f'<section class="sec" id="{sid}"><div class="num">{num}</div><h2>{title}</h2>{html}</section>'

TERMS = """
<p>Bibliada is a daily Bible puzzle game, published by <strong>Dragan Software Ultimate S.R.L.</strong>,
Timișoara, Romania. By using the app you agree to the terms below.</p>

<h3>Your account</h3>
<p>You need an account to play and keep your progress. You must be at least 13 years old.
You are responsible for your password and for what happens through your account.</p>

<h3>Fair play</h3>
<ul>
  <li>Results are validated on our servers. Do not use bots, automation or modified builds of the app.</li>
  <li>Your name and profile picture appear in leaderboards and duels — keep them decent.</li>
  <li>Accounts that cheat or abuse other players can be suspended or deleted.</li>
</ul>

<h3>Content</h3>
<p>Scripture quotations are taken from public domain translations. Everything else — the games, the questions,
the text and the design — belongs to us and may not be copied or redistributed without our written consent.</p>

<h3>Donations</h3>
<p>Donations made in the app are voluntary, processed by Stripe, unlock no features and are not refundable.
Bibliada can be played in full without paying anything.</p>

<h3>Availability and liability</h3>
<p>The service is provided “as is”. We may change or discontinue features, and the daily game depends on your
connection. We are not liable for indirect losses arising from your use of the app.</p>

<h3>App Store</h3>
<p>This agreement is between you and us, not with Apple. Apple has no obligation to provide support for the app,
but is a third-party beneficiary of this agreement and may enforce it.</p>

<h3>Governing law and changes</h3>
<p>Romanian law applies, without affecting your consumer rights. We may update these terms; continuing to use
the app after an update means you accept them.</p>
"""

PRIVACY = """
<p>Data controller: <strong>Dragan Software Ultimate S.R.L.</strong>, Timișoara, Romania.
Contact: <a href="mailto:contact@dragan.me">contact@dragan.me</a>. We process personal data under the GDPR
(EU Regulation 2016/679).</p>

<h3>What we collect</h3>
<ul>
  <li><strong>Account</strong>: your email address, display name (optional) and password, stored only in hashed form.</li>
  <li><strong>Profile</strong>: profile picture, language, time zone, theme and notification preferences.</li>
  <li><strong>Gameplay</strong>: answers, scores, XP, daily streak, league standing, duels and your friends list.</li>
  <li><strong>Technical</strong>: app version, operating system and your push notification token.</li>
  <li><strong>Donations</strong>: a record of the donation. Card details go straight to Stripe and never reach us.</li>
</ul>

<h3>Why we use it</h3>
<ul>
  <li>To run your account, progress, leaderboards and duels — performance of our contract with you.</li>
  <li>To prevent cheating and abuse and keep the service secure — our legitimate interest.</li>
  <li>To send push notifications — based on your consent, which you can withdraw at any time in settings.</li>
  <li>To keep accounting records for donations — legal obligation.</li>
</ul>

<h3>Who we share it with</h3>
<p>Only the providers we need to run the app: <strong>Google Firebase</strong> (push notifications),
<strong>Stripe</strong> (donations), <strong>RevoPush</strong> (app updates) and our server hosting provider.
We show no ads, we do not sell data, and we use no tracking or advertising SDKs.</p>

<h3>How long we keep it</h3>
<p>Account data stays until you delete your account. Backups roll over within 35 days.
Financial records related to donations are kept for as long as accounting law requires.</p>

<h3>Your rights</h3>
<p>You have the right of access, rectification, erasure, restriction, portability and objection, and the right to
withdraw consent. Write to <a href="mailto:contact@dragan.me">contact@dragan.me</a>.
You may also lodge a complaint with the Romanian Data Protection Authority
(<a href="https://www.dataprotection.ro" target="_blank" rel="noopener">dataprotection.ro</a>).</p>

<h3>Children</h3>
<p>Bibliada is not directed at children under 13 and we do not knowingly collect their data.</p>

<h3>Security</h3>
<p>Passwords are stored with argon2id, traffic is encrypted with TLS, and sessions use rotating refresh tokens.</p>
"""

DELETE = """
<p>You can delete your account at any time, without asking us. Deletion is permanent.</p>

<h3>From the app (recommended)</h3>
<p>Open Bibliada → <strong>Settings</strong> → <strong>Account</strong> → <strong>Delete account</strong> and confirm.
The request starts immediately, with no further steps.</p>

<h3>If you can no longer open the app</h3>
<p>Email <a href="mailto:contact@dragan.me?subject=Delete%20Bibliada%20account">contact@dragan.me</a>
with the subject “Delete account” and the email address on the account. We process the request manually and
confirm the deletion to you.</p>

<h3>What happens next</h3>
<ul>
  <li>The account is disabled immediately and every active session is signed out.</li>
  <li>Within about 30 days the account, profile, progress, streak, friends, duels and push token are permanently deleted.</li>
  <li>Only the financial records of donations remain, which accounting law requires us to keep.</li>
</ul>
"""

legal_body = f"""
<section class="doc"><div class="wrap">
  <a class="back" href="../index.html">← Dragan.me</a>
  <div class="upd" style="margin-top:26px">Last updated {UPDATED}</div>
  <h1>Bibliada — terms,<br>privacy &amp; your account</h1>
  <div class="toc">
    <a href="#terms">Terms</a><a href="#privacy">Privacy</a>
    <a href="#delete">Account deletion</a><a href="../support/bibliada.html">Support</a>
  </div>
  {sec("01","Terms of use",TERMS,"terms")}
  {sec("02","Privacy policy",PRIVACY,"privacy")}
  {sec("03","Deleting your account",DELETE,"delete")}
</div></section>
"""

SUPPORT = """
<p>Bibliada is made by a small team in Timișoara. Write to us directly — we usually reply within one or two working days.</p>
<h3>Contact</h3>
<p><a href="mailto:contact@dragan.me?subject=Bibliada%20support">contact@dragan.me</a></p>
<h3>Frequently asked</h3>
<p><strong>I forgot my password.</strong> Use “Forgot password” on the sign-in screen; a reset link is sent to your email.</p>
<p><strong>I lost my streak.</strong> Streaks are calculated in your account's time zone. If a day you played did not register, write to us with the date and we will check your history.</p>
<p><strong>A puzzle has a wrong answer.</strong> Send us the game name, the date and a screenshot — we fix the content and publish it without needing a store update.</p>
<p><strong>I want another game or another language.</strong> Tell us. Content ships in Romanian, English and Spanish, and new games come out of what people ask for.</p>
<p><strong>How do I delete my account?</strong> In <strong>Settings → Account → Delete account</strong>, or see the
<a href="../legal/bibliada.html#delete">account deletion page</a>.</p>
<p><strong>Do donations unlock anything?</strong> No. The game is entirely free; a donation is only support for the project.</p>
"""

support_body = f"""
<section class="doc"><div class="wrap">
  <a class="back" href="../index.html">← Dragan.me</a>
  <div class="upd" style="margin-top:26px">Support</div>
  <h1>Bibliada — support</h1>
  <div class="toc"><a href="../legal/bibliada.html#terms">Terms</a><a href="../legal/bibliada.html#privacy">Privacy</a><a href="../legal/bibliada.html#delete">Account deletion</a></div>
  <section class="sec">{SUPPORT}</section>
</div></section>
"""

(OUT/"legal"/"bibliada.html").write_text(
    page("Bibliada — Terms, privacy & account deletion",
         "Terms of use, privacy policy and account deletion for the Bibliada app.",
         legal_body, LEGAL_CSS), encoding="utf-8")
(OUT/"support"/"bibliada.html").write_text(
    page("Bibliada — Support", "Contact and frequently asked questions for the Bibliada app.",
         support_body, LEGAL_CSS), encoding="utf-8")
print("legal/bibliada.html + support/bibliada.html")

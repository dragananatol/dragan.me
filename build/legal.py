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

<h3>Payments</h3>
<p>Bibliada offers no purchases, subscriptions or donations of any kind, on either platform.
The whole app is free.</p>

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
</ul>

<h3>Why we use it</h3>
<ul>
  <li>To run your account, progress, leaderboards and duels — performance of our contract with you.</li>
  <li>To prevent cheating and abuse and keep the service secure — our legitimate interest.</li>
  <li>To send push notifications — based on your consent, which you can withdraw at any time in settings.</li>
</ul>

<h3>Who we share it with</h3>
<p>Only the providers we need to run the app: <strong>Google Firebase</strong> (push notifications),
<strong>RevoPush</strong> (app updates) and our server hosting provider.
We show no ads, we do not sell data, and we use no tracking or advertising SDKs.</p>

<h3>How long we keep it</h3>
<p>Account data stays until you delete your account. Backups roll over within 35 days.</p>

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
</ul>
"""

legal_body = f"""
<section class="doc"><div class="wrap">
  <a class="back" href="/">← Dragan.me</a>
  <div class="upd" style="margin-top:26px">Last updated {UPDATED}</div>
  <h1>Bibliada — terms,<br>privacy &amp; your account</h1>
  <div class="toc">
    <a href="#terms">Terms</a><a href="#privacy">Privacy</a>
    <a href="#delete">Account deletion</a><a href="/support/bibliada.html">Support</a>
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
<a href="/legal/bibliada.html#delete">account deletion page</a>.</p>
"""

support_body = f"""
<section class="doc"><div class="wrap">
  <a class="back" href="/">← Dragan.me</a>
  <div class="upd" style="margin-top:26px">Support</div>
  <h1>Bibliada — support</h1>
  <div class="toc"><a href="/legal/bibliada.html#terms">Terms</a><a href="/legal/bibliada.html#privacy">Privacy</a><a href="/legal/bibliada.html#delete">Account deletion</a></div>
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

# ------------------------------------------------------------------ WanderTale
# EN + RO, one page per language. Keep in step with what wandertale-api stores
# (users, user_tokens, user_travel, user_localities, trips, crews, routes,
# audit_events, contact_match_usage) and with the App Store privacy label.
WT_UPDATED = {"en": "5 October 2026", "ro": "5 octombrie 2026"}
WT_MAIL = '<a href="mailto:contact@dragan.me?subject=WanderTale">contact@dragan.me</a>'

WT_TERMS = {"en": f"""
<p>WanderTale is an audio companion for road trips and walks: it tells stories about the places you pass.
It is operated by <strong>Anatol Dragan</strong>, an individual developer in Romania
(contact: {WT_MAIL}). By creating an account you agree to these terms.</p>

<h3>Your account</h3>
<ul>
  <li>You need an account to use WanderTale. You must be at least <strong>16 years old</strong>, or have the consent of a parent or guardian.</li>
  <li>Keep your password safe; you are responsible for what happens through your account.</li>
  <li>You can delete your account at any time in the app (Settings → Delete account).</li>
</ul>

<h3>Drive safely</h3>
<p>Stories are audio so your eyes stay on the road. Do not handle the phone while driving, and always follow
traffic rules and road signs. Routes, detours and travel times are estimates, not navigation.</p>

<h3>AI-generated content</h3>
<p>Stories are written automatically by an AI model from public sources (Wikipedia, Wikidata, OpenStreetMap and
other web sources) and read aloud by synthetic voices — no human narrator. They can contain mistakes:
check anything important, and tell us at {WT_MAIL} when a story is wrong so we can fix it.
Texts derived from Wikipedia are available under <a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank" rel="noopener">CC BY-SA 4.0</a>;
map data © <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap contributors</a> (ODbL).</p>

<h3>Acceptable use</h3>
<ul>
  <li>Do not abuse the service: no scraping, automated requests, attempts to bypass limits, or access to other people's accounts.</li>
  <li>Your name, username and profile photo are seen by the people you travel with and, for public routes, by other users — keep them decent.</li>
</ul>

<h3>Routes you publish</h3>
<p>Routes you make public are visible to other users together with your name. Do not publish anything unlawful,
offensive or that infringes other people's rights. You keep the rights to what you publish and give us a
licence to show it in the app. Users can report a route or block its author; a route reported by several users is
hidden automatically and reviewed, and we may remove content or suspend accounts that break these rules.</p>

<h3>Price</h3>
<p>WanderTale is currently free. Usage limits may apply. If we ever introduce paid plans, we will announce them
in the app before anything is charged, and nothing is charged without your explicit purchase.</p>

<h3>Availability and liability</h3>
<p>The service is provided “as is”, without guarantees of availability or accuracy, to the extent the law allows.
We may change or discontinue features. Nothing in these terms limits liability that cannot be limited by law,
or your rights as a consumer.</p>

<h3>App Store</h3>
<p>This agreement is between you and us, not with Apple. Apple has no obligation to provide support for the app,
but is a third-party beneficiary of this agreement and may enforce it.</p>

<h3>Governing law and changes</h3>
<p>Romanian law applies. If you are a consumer in the EU, you keep the protection of the mandatory consumer law of
your country of residence and may bring a claim there. We may update these terms; we will tell you in the app or by email
about material changes before they take effect, and the date above always shows the current version.</p>
""", "ro": f"""
<p>WanderTale este un însoțitor audio pentru drumuri și plimbări: îți spune povești despre locurile pe lângă care treci.
Este operat de <strong>Anatol Dragan</strong>, dezvoltator persoană fizică din România
(contact: {WT_MAIL}). Prin crearea unui cont ești de acord cu acești termeni.</p>

<h3>Contul tău</h3>
<ul>
  <li>Ai nevoie de un cont ca să folosești WanderTale. Trebuie să ai cel puțin <strong>16 ani</strong> sau acordul unui părinte ori tutore.</li>
  <li>Păstrează parola în siguranță; răspunzi de ce se întâmplă prin contul tău.</li>
  <li>Îți poți șterge contul oricând din aplicație (Setări → Șterge contul).</li>
</ul>

<h3>Condu în siguranță</h3>
<p>Poveștile sunt audio, ca să rămâi cu ochii pe drum. Nu manevra telefonul în timp ce conduci și respectă mereu
regulile de circulație și indicatoarele. Rutele, ocolurile și timpii sunt estimări, nu navigație.</p>

<h3>Conținut generat cu AI</h3>
<p>Poveștile sunt scrise automat de un model AI din surse publice (Wikipedia, Wikidata, OpenStreetMap și alte surse
web) și citite de voci sintetice — nu de un narator uman. Pot conține greșeli: verifică ce este important și
scrie-ne la {WT_MAIL} când o poveste e greșită, ca să o corectăm.
Textele derivate din Wikipedia sunt disponibile sub licența <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.ro" target="_blank" rel="noopener">CC BY-SA 4.0</a>;
date de hartă © <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">contribuitorii OpenStreetMap</a> (ODbL).</p>

<h3>Utilizare acceptabilă</h3>
<ul>
  <li>Nu abuza de serviciu: fără extragere automată de date, cereri automate, ocolirea limitelor sau acces la conturile altora.</li>
  <li>Numele, numele de utilizator și poza de profil sunt văzute de cei cu care călătorești și, pentru rutele publice, de alți utilizatori — păstrează-le decente.</li>
</ul>

<h3>Rutele pe care le publici</h3>
<p>Rutele făcute publice sunt vizibile altor utilizatori, împreună cu numele tău. Nu publica nimic ilegal, jignitor
sau care încalcă drepturile altora. Drepturile asupra a ce publici rămân ale tale; ne dai o licență să le afișăm
în aplicație. Utilizatorii pot raporta o rută sau îi pot bloca autorul; o rută raportată de mai mulți utilizatori
este ascunsă automat și verificată, iar noi putem șterge conținut sau suspenda conturi care încalcă aceste reguli.</p>

<h3>Preț</h3>
<p>WanderTale este în prezent gratuit. Se pot aplica limite de utilizare. Dacă vom introduce planuri plătite, le vom
anunța în aplicație înainte de orice plată, și nimic nu se plătește fără o achiziție făcută explicit de tine.</p>

<h3>Disponibilitate și răspundere</h3>
<p>Serviciul este oferit „ca atare”, fără garanții de disponibilitate sau exactitate, în limitele permise de lege.
Putem modifica sau opri funcții. Nimic din acești termeni nu limitează răspunderea care nu poate fi limitată prin lege
și nici drepturile tale de consumator.</p>

<h3>App Store</h3>
<p>Acest acord este între tine și noi, nu cu Apple. Apple nu are obligația de a oferi suport pentru aplicație,
dar este terț beneficiar al acestui acord și îl poate pune în aplicare.</p>

<h3>Legea aplicabilă și modificări</h3>
<p>Se aplică legea română. Dacă ești consumator în UE, păstrezi protecția legii obligatorii a consumatorului din țara
în care locuiești și poți face o reclamație acolo. Putem actualiza termenii; te anunțăm în aplicație sau pe email despre
schimbările importante înainte să intre în vigoare, iar data de mai sus arată mereu versiunea curentă.</p>
"""}

WT_PRIVACY = {"en": f"""
<p>Data controller: <strong>Anatol Dragan</strong>, individual developer, Romania.
Contact for anything about your data: {WT_MAIL}. We process personal data under the GDPR (EU Regulation 2016/679).
WanderTale shows no ads, does not track you across other apps or websites, and does not sell your data.</p>

<h3>What we collect</h3>
<ul>
  <li><strong>Account</strong>: email address, name, username, optional profile photo, home town, narration language,
    interests and story preferences. Your password is stored only as an argon2 hash; with Sign in with Apple or Google
    we store the provider's account identifier instead. We also keep a SHA-256 fingerprint of your email so friends
    who have you in their contacts can find you.</li>
  <li><strong>Sessions</strong>: for each signed-in device, the IP address and app user agent at sign-in. A session ends
    after 30 days without use (90 days at most).</li>
  <li><strong>Location</strong>: the app uses your precise location while you explore, drive or walk — also in the
    background, with the screen locked, if you allow location “Always” for background narration. We store
    <strong>only your last position</strong> (latitude, longitude, speed, heading and time, overwritten on every update)
    and the distance travelled, <strong>not</strong> a continuous GPS trail. We also keep the list of localities you
    passed, with the first time you passed each one, and your trips with their stops, detours and the stories heard
    along the way.</li>
  <li><strong>Activity</strong>: stories you listened to or saved, your story passport, and routes you create or save.</li>
  <li><strong>Contacts (optional)</strong>: when you look for friends, the app reads email addresses from your
    contacts on the phone and sends only their SHA-256 fingerprints, to find who already uses WanderTale. The
    fingerprints are compared and discarded; we keep only a daily count of lookups (to stop abuse), never your
    contacts.</li>
  <li><strong>Crews (shared trips)</strong>: the other members of a crew see your name, profile photo, device name,
    connection signal and the next stop; your votes on stories are shared with them. “Join nearby” briefly uses your
    position to match you with a host within about 50 metres.</li>
  <li><strong>Voice search (optional)</strong>: while you hold the microphone, speech is turned into text by Apple's
    speech recognition, which may process the audio on Apple's servers. We receive only the text.</li>
  <li><strong>Push notifications (optional)</strong>: your device's push token.</li>
  <li><strong>Security log</strong>: for actions in the app (sign-in, trips, changes to your account) we record your user id,
    IP address, platform, app version and the action — never your location.</li>
  <li><strong>Diagnostics</strong>: when the app crashes it sends the error message and stack trace, platform and app
    version to our server and to Sentry. These reports are not linked to your account.</li>
  <li><strong>Product interaction</strong> (analytics, linked to you, first-party only): a few usage events, described
    under <a href="#usage-events">First-party usage events</a> below.</li>
</ul>

<h3 id="usage-events">First-party usage events</h3>
<p>To understand how people find and use WanderTale, the app sends a few usage events directly to our own servers —
for example app first opened, sign-in screen shown, account created, a story played (the point of interest's ID only,
never your location), a trip started, and the ad campaign name if you opened the app from a tagged link. They carry a
random identifier created when the app is installed (not your device's advertising ID) and, once you are signed in,
your account. We use no third-party analytics or advertising SDKs, do not track you across other apps or websites,
and do not share these events with anyone. They are deleted after 400 days, and the link to your account is removed
when you delete your account.</p>

<h3>Why we use it, and on what legal basis</h3>
<ul>
  <li>To run your account and deliver the service — stories near you, trips, routes, crews, account emails:
    <strong>performance of our contract</strong> with you (Art. 6(1)(b) GDPR).</li>
  <li>Background location, contact matching and push notifications: <strong>your consent</strong> (Art. 6(1)(a)), given
    through the phone's permission prompts. You can withdraw it at any time in the phone's settings; the rest of the
    app keeps working.</li>
  <li>Security log, abuse prevention, moderation of public routes, crash diagnostics and first-party usage events: our
    <strong>legitimate interest</strong> in keeping the service secure and working (Art. 6(1)(f)).</li>
  <li>Where the law requires us to keep or hand over data: <strong>legal obligation</strong> (Art. 6(1)(c)).</li>
</ul>
<p>We make no automated decisions with legal or similarly significant effects about you. Stories are chosen by
place, language and your interests only.</p>

<h3>Who processes it</h3>
<p>Only the providers we need to run the app, each under its data processing terms:</p>
<ul>
  <li><strong>Railway</strong> (United States) — hosts the server, the database and media storage (profile photos, audio).</li>
  <li><strong>Google Gemini API</strong> (United States) — writes the stories. It receives data about places only
    (name, map tags, coordinates, public descriptions), never data about you.</li>
  <li><strong>Modal</strong> (United States) — synthesises the narration voices from story text. No personal data.</li>
  <li><strong>Mapbox</strong> (United States) — computes walking routes and some driving routes; it receives the
    coordinates of the route's start, stops and end, not your identity.</li>
  <li><strong>Brevo</strong> (European Union) — sends account emails (verification code, password reset).</li>
  <li><strong>Google Firebase Cloud Messaging</strong> (United States) and <strong>Apple Push Notification service</strong> — deliver push notifications.</li>
  <li><strong>Sentry</strong> (United States) — receives server and app error reports.</li>
  <li><strong>Apple</strong> and <strong>Google</strong> — Sign in with Apple / Google if you use them; Apple speech recognition for voice search.</li>
  <li><strong>Wikipedia, Wikidata, Wikimedia Commons, OpenStreetMap</strong> — public sources our server reads about places.
    No personal data is sent to them.</li>
</ul>
<p>Transfers outside the European Economic Area (to the United States) rely on the EU–US Data Privacy Framework where
the provider is certified, and otherwise on the European Commission's Standard Contractual Clauses.</p>

<h3>How long we keep it</h3>
<ul>
  <li>Account, preferences, last position, localities, trips, routes and listening history: until you delete them or
    your account.</li>
  <li>Sessions: until you sign out, or 30 days after last use (90 days at most).</li>
  <li>Contact fingerprints: not stored; only the daily lookup count, until your account is deleted.</li>
  <li>Security log: 180 days for actions, 14 days for views. It is kept for that period even after you delete your
    account, so that abuse and attacks can still be investigated.</li>
  <li>Server logs: up to 30 days. Error reports in Sentry: up to 90 days.</li>
  <li>Push token: until you sign out, delete the account, or the token expires.</li>
  <li>Usage events: 400 days; the link to your account is removed when you delete your account.</li>
  <li>Database backups: kept 14–20 days, then overwritten. Deleted data disappears from backups within that period.</li>
</ul>

<h3>Your rights</h3>
<p>You have the right of access, rectification, erasure, restriction of processing, data portability and objection,
and the right to withdraw consent at any time without affecting earlier processing. Most data can be edited or
deleted in the app; for anything else, including a copy of your data, write to {WT_MAIL} — we reply within one month.</p>
<p>You may also lodge a complaint with a data protection authority, in particular where you live or work:
in Romania <a href="https://www.dataprotection.ro" target="_blank" rel="noopener">ANSPDCP</a>,
in Italy the <a href="https://www.garanteprivacy.it" target="_blank" rel="noopener">Garante per la protezione dei dati personali</a>,
in the Republic of Moldova the <a href="https://datepersonale.md" target="_blank" rel="noopener">National Center for Personal Data Protection</a> (NCPDP).</p>

<h3>Children</h3>
<p>WanderTale is for people aged 16 and over. Younger users need the consent of a parent or guardian. If you
believe a child gave us data without that consent, write to us and we will delete it.</p>

<h3>Security</h3>
<p>Traffic is encrypted with TLS, passwords are hashed with argon2, sessions use rotating refresh tokens, and access
to production data is limited to the operator.</p>

<h3>Changes</h3>
<p>We will update this policy when the app changes what it collects, and tell you in the app or by email about material changes.
The date at the top shows the current version.</p>
""", "ro": f"""
<p>Operator de date: <strong>Anatol Dragan</strong>, dezvoltator persoană fizică, România.
Contact pentru orice privește datele tale: {WT_MAIL}. Prelucrăm date personale conform GDPR (Regulamentul UE 2016/679).
WanderTale nu afișează reclame, nu te urmărește în alte aplicații sau site-uri și nu vinde datele tale.</p>

<h3>Ce colectăm</h3>
<ul>
  <li><strong>Contul</strong>: adresa de email, numele, numele de utilizator, poza de profil (opțional), orașul de
    reședință, limba narațiunii, interesele și preferințele pentru povești. Parola se păstrează doar ca hash argon2;
    la autentificarea cu Apple sau Google păstrăm în schimb identificatorul contului de la furnizor. Păstrăm și o
    amprentă SHA-256 a emailului tău, ca prietenii care te au în agendă să te poată găsi.</li>
  <li><strong>Sesiunile</strong>: pentru fiecare dispozitiv conectat, adresa IP și agentul aplicației la autentificare.
    O sesiune se încheie după 30 de zile fără utilizare (maximum 90 de zile).</li>
  <li><strong>Locația</strong>: aplicația folosește locația ta exactă cât timp explorezi, conduci sau te plimbi — și în
    fundal, cu ecranul blocat, dacă permiți locația „Întotdeauna” pentru narațiunea în fundal. Păstrăm
    <strong>doar ultima poziție</strong> (latitudine, longitudine, viteză, direcție și ora, suprascrise la fiecare
    actualizare) și distanța parcursă, <strong>nu</strong> un traseu GPS continuu. Păstrăm și lista localităților prin
    care ai trecut, cu momentul primei treceri, precum și călătoriile tale cu opririle, ocolurile și poveștile ascultate pe drum.</li>
  <li><strong>Activitatea</strong>: poveștile ascultate sau salvate, pașaportul de povești și rutele create sau salvate.</li>
  <li><strong>Contactele (opțional)</strong>: când cauți prieteni, aplicația citește adresele de email din agenda
    telefonului și trimite doar amprentele lor SHA-256, ca să afle cine folosește deja WanderTale. Amprentele sunt
    comparate și apoi aruncate; păstrăm doar un număr zilnic de căutări (contra abuzurilor), niciodată contactele tale.</li>
  <li><strong>Echipaje (călătorii comune)</strong>: ceilalți membri ai echipajului văd numele tău, poza de profil, numele
    dispozitivului, semnalul conexiunii și următoarea oprire; voturile tale pentru povești le sunt vizibile.
    „Alătură-te din apropiere” folosește pentru scurt timp poziția ta ca să te potrivească cu o gazdă aflată la cel mult ~50 de metri.</li>
  <li><strong>Căutarea vocală (opțional)</strong>: cât ții apăsat microfonul, vorbirea este transformată în text de
    recunoașterea vocală Apple, care poate prelucra sunetul pe serverele Apple. Noi primim doar textul.</li>
  <li><strong>Notificări (opțional)</strong>: tokenul de notificări al dispozitivului.</li>
  <li><strong>Jurnalul de securitate</strong>: pentru acțiunile din aplicație (autentificare, călătorii, modificări ale
    contului) înregistrăm id-ul de utilizator, adresa IP, platforma, versiunea aplicației și acțiunea — niciodată locația.</li>
  <li><strong>Diagnostic</strong>: când aplicația se blochează, trimite mesajul erorii și stack trace-ul, platforma și
    versiunea aplicației către serverul nostru și către Sentry. Aceste rapoarte nu sunt legate de contul tău.</li>
  <li><strong>Interacțiunea cu produsul</strong> (statistici, legate de tine, doar proprii): câteva evenimente de
    utilizare, descrise mai jos la <a href="#usage-events">Evenimente de utilizare proprii</a>.</li>
</ul>

<h3 id="usage-events">Evenimente de utilizare proprii</h3>
<p>Ca să înțelegem cum găsesc și folosesc oamenii WanderTale, aplicația trimite câteva evenimente de utilizare direct
către serverele noastre — de exemplu prima deschidere a aplicației, afișarea ecranului de autentificare, crearea
contului, o poveste ascultată (doar ID-ul locului, niciodată locația ta), o călătorie începută și numele campaniei
publicitare, dacă ai deschis aplicația dintr-un link etichetat. Ele poartă un identificator aleatoriu creat la
instalarea aplicației (nu identificatorul de publicitate al dispozitivului) și, după ce te autentifici, contul tău.
Nu folosim SDK-uri de statistici sau publicitate ale terților, nu te urmărim în alte aplicații sau site-uri și nu
împărtășim aceste evenimente cu nimeni. Ele se șterg după 400 de zile, iar legătura cu contul tău se elimină când îți
ștergi contul.</p>

<h3>De ce le folosim și pe ce temei legal</h3>
<ul>
  <li>Pentru contul tău și serviciul în sine — povești din apropiere, călătorii, rute, echipaje, emailurile contului:
    <strong>executarea contractului</strong> cu tine (art. 6 alin. (1) lit. b GDPR).</li>
  <li>Locația în fundal, potrivirea contactelor și notificările: <strong>consimțământul tău</strong> (art. 6 alin. (1) lit. a),
    dat prin solicitările de permisiune ale telefonului. Îl poți retrage oricând din setările telefonului; restul
    aplicației continuă să funcționeze.</li>
  <li>Jurnalul de securitate, prevenirea abuzurilor, moderarea rutelor publice, diagnosticarea erorilor și evenimentele de utilizare proprii:
    <strong>interesul nostru legitim</strong> de a ține serviciul sigur și funcțional (art. 6 alin. (1) lit. f).</li>
  <li>Când legea ne obligă să păstrăm sau să predăm date: <strong>obligația legală</strong> (art. 6 alin. (1) lit. c).</li>
</ul>
<p>Nu luăm decizii automate cu efecte juridice sau la fel de importante asupra ta. Poveștile sunt alese doar după
loc, limbă și interesele tale.</p>

<h3>Cine le prelucrează</h3>
<p>Doar furnizorii de care avem nevoie ca aplicația să funcționeze, fiecare în baza condițiilor sale de prelucrare a datelor:</p>
<ul>
  <li><strong>Railway</strong> (Statele Unite) — găzduiește serverul, baza de date și fișierele media (poze de profil, audio).</li>
  <li><strong>Google Gemini API</strong> (Statele Unite) — scrie poveștile. Primește doar date despre locuri
    (nume, etichete de hartă, coordonate, descrieri publice), niciodată date despre tine.</li>
  <li><strong>Modal</strong> (Statele Unite) — sintetizează vocile narațiunii din textul poveștilor. Fără date personale.</li>
  <li><strong>Mapbox</strong> (Statele Unite) — calculează rutele pietonale și unele rute auto; primește coordonatele
    plecării, opririlor și destinației, nu identitatea ta.</li>
  <li><strong>Brevo</strong> (Uniunea Europeană) — trimite emailurile contului (cod de verificare, resetarea parolei).</li>
  <li><strong>Google Firebase Cloud Messaging</strong> (Statele Unite) și <strong>Apple Push Notification service</strong> — livrează notificările.</li>
  <li><strong>Sentry</strong> (Statele Unite) — primește rapoartele de erori ale serverului și aplicației.</li>
  <li><strong>Apple</strong> și <strong>Google</strong> — autentificarea cu Apple / Google, dacă o folosești; recunoașterea vocală Apple pentru căutarea vocală.</li>
  <li><strong>Wikipedia, Wikidata, Wikimedia Commons, OpenStreetMap</strong> — surse publice pe care serverul nostru le
    citește despre locuri. Nu li se trimit date personale.</li>
</ul>
<p>Transferurile în afara Spațiului Economic European (în Statele Unite) se bazează pe Cadrul UE–SUA privind
confidențialitatea datelor, acolo unde furnizorul este certificat, iar altfel pe Clauzele contractuale standard ale
Comisiei Europene.</p>

<h3>Cât timp le păstrăm</h3>
<ul>
  <li>Contul, preferințele, ultima poziție, localitățile, călătoriile, rutele și istoricul ascultărilor: până le ștergi
    tu sau îți ștergi contul.</li>
  <li>Sesiunile: până te deconectezi sau 30 de zile după ultima utilizare (maximum 90 de zile).</li>
  <li>Amprentele contactelor: nu se păstrează; doar numărul zilnic de căutări, până la ștergerea contului.</li>
  <li>Jurnalul de securitate: 180 de zile pentru acțiuni, 14 zile pentru vizualizări. Se păstrează pe această perioadă
    și după ștergerea contului, ca abuzurile și atacurile să poată fi investigate.</li>
  <li>Jurnalele serverului: până la 30 de zile. Rapoartele de erori din Sentry: până la 90 de zile.</li>
  <li>Tokenul de notificări: până te deconectezi, îți ștergi contul sau tokenul expiră.</li>
  <li>Evenimentele de utilizare: 400 de zile; legătura cu contul tău se elimină când îți ștergi contul.</li>
  <li>Copiile de rezervă ale bazei de date: păstrate 14–20 de zile, apoi suprascrise. Datele șterse dispar din copii în acest interval.</li>
</ul>

<h3>Drepturile tale</h3>
<p>Ai dreptul de acces, rectificare, ștergere, restricționarea prelucrării, portabilitatea datelor și opoziție,
precum și dreptul de a-ți retrage oricând consimțământul, fără a afecta prelucrarea anterioară. Majoritatea datelor
le poți modifica sau șterge din aplicație; pentru orice altceva, inclusiv o copie a datelor, scrie la {WT_MAIL} —
răspundem în cel mult o lună.</p>
<p>Poți depune și o plângere la o autoritate de protecție a datelor, mai ales acolo unde locuiești sau lucrezi:
în România <a href="https://www.dataprotection.ro" target="_blank" rel="noopener">ANSPDCP</a>,
în Italia <a href="https://www.garanteprivacy.it" target="_blank" rel="noopener">Garante per la protezione dei dati personali</a>,
în Republica Moldova <a href="https://datepersonale.md" target="_blank" rel="noopener">Centrul Național pentru Protecția Datelor cu Caracter Personal</a> (CNPDCP).</p>

<h3>Copii</h3>
<p>WanderTale este pentru persoane de cel puțin 16 ani. Utilizatorii mai tineri au nevoie de acordul unui părinte
sau tutore. Dacă crezi că un copil ne-a dat date fără acest acord, scrie-ne și le ștergem.</p>

<h3>Securitate</h3>
<p>Traficul este criptat cu TLS, parolele sunt hash-uite cu argon2, sesiunile folosesc tokenuri de reîmprospătare
rotative, iar accesul la datele de producție este limitat la operator.</p>

<h3>Modificări</h3>
<p>Actualizăm această politică atunci când aplicația schimbă ce colectează și te anunțăm în aplicație sau pe email despre
schimbările importante. Data de sus arată versiunea curentă.</p>
"""}

WT_DELETE = {"en": f"""
<p>You can delete your account at any time, without asking us. Deletion is immediate and permanent.</p>
<h3>From the app</h3>
<p>Open WanderTale → <strong>Settings</strong> → <strong>Delete account</strong> and confirm. If you used Sign in with
Apple, the app's access to your Apple ID is revoked as well.</p>
<h3>If you can no longer open the app</h3>
<p>Email <a href="mailto:contact@dragan.me?subject=Delete%20WanderTale%20account">contact@dragan.me</a> from the address
on the account, with the subject “Delete account”. We delete it and confirm to you.</p>
<h3>What is deleted</h3>
<p>Your account, profile and photo, sessions, push tokens, last position, localities, trips, crews, routes,
saved and listened stories and preferences are deleted at once. Only the security log keeps your user id and IP
address, for up to 180 days, and usage events stay for up to 400 days without the link to your account, as
described in the privacy policy. Backups roll over within 14–20 days.</p>
""", "ro": f"""
<p>Îți poți șterge contul oricând, fără să ne ceri. Ștergerea este imediată și definitivă.</p>
<h3>Din aplicație</h3>
<p>Deschide WanderTale → <strong>Setări</strong> → <strong>Șterge contul</strong> și confirmă. Dacă ai folosit
autentificarea cu Apple, se revocă și accesul aplicației la Apple ID-ul tău.</p>
<h3>Dacă nu mai poți deschide aplicația</h3>
<p>Scrie la <a href="mailto:contact@dragan.me?subject=Stergere%20cont%20WanderTale">contact@dragan.me</a> de pe adresa
contului, cu subiectul „Ștergere cont”. Îl ștergem și îți confirmăm.</p>
<h3>Ce se șterge</h3>
<p>Contul, profilul și poza, sesiunile, tokenurile de notificări, ultima poziție, localitățile, călătoriile,
echipajele, rutele, poveștile salvate și ascultate și preferințele se șterg imediat. Doar jurnalul de securitate
păstrează id-ul de utilizator și adresa IP, cel mult 180 de zile, iar evenimentele de utilizare rămân cel mult 400 de
zile fără legătura cu contul tău, așa cum scrie în politica de confidențialitate. Copiile de rezervă se înlocuiesc în 14–20 de zile.</p>
"""}

WT_SUPPORT = {"en": f"""
<p>WanderTale is made by one developer in Romania. Write directly — we usually reply within two working days.</p>
<h3>Contact</h3>
<p>{WT_MAIL}</p>
<h3>Frequently asked</h3>
<p><strong>Do I need an account?</strong> Yes — sign up with email, Apple or Google. Your account works as soon as
your email is verified.</p>
<p><strong>I didn't get the verification code.</strong> Check your spam folder, then tap “Resend code”. Each new email
replaces the previous code.</p>
<p><strong>I forgot my password.</strong> Use “Forgot password” on the sign-in screen; a reset link is sent to your email.</p>
<p><strong>Why are there no stories around me?</strong> WanderTale covers Romania, Moldova and Italy. The first visit to
a new area can take a few seconds while its places load; if nothing is close, the app shows the nearest stories.</p>
<p><strong>Stories stop when the screen locks.</strong> Allow location “Always” for WanderTale in the phone's settings —
background narration needs it. You can turn it back to “While using” at any time.</p>
<p><strong>A story is wrong.</strong> Stories are generated by AI and can contain mistakes. Send us the place name, the
language and, if you can, a screenshot — we correct the story without needing an app update.</p>
<p><strong>How do I delete my account?</strong> In <strong>Settings → Delete account</strong>, or see
<a href="/legal/wandertale.html#delete">account deletion</a>.</p>
""", "ro": f"""
<p>WanderTale este făcut de un singur dezvoltator din România. Scrie-ne direct — de obicei răspundem în două zile lucrătoare.</p>
<h3>Contact</h3>
<p>{WT_MAIL}</p>
<h3>Întrebări frecvente</h3>
<p><strong>Am nevoie de cont?</strong> Da — te înregistrezi cu email, Apple sau Google. Contul funcționează imediat
ce emailul este verificat.</p>
<p><strong>Nu am primit codul de verificare.</strong> Verifică dosarul spam, apoi apasă „Retrimite codul”. Fiecare email
nou înlocuiește codul anterior.</p>
<p><strong>Am uitat parola.</strong> Folosește „Am uitat parola” pe ecranul de autentificare; primești un link de resetare pe email.</p>
<p><strong>De ce nu sunt povești în jurul meu?</strong> WanderTale acoperă România, Moldova și Italia. Prima vizită într-o
zonă nouă poate dura câteva secunde cât se încarcă locurile; dacă nu e nimic aproape, aplicația arată cele mai apropiate povești.</p>
<p><strong>Poveștile se opresc când se blochează ecranul.</strong> Permite locația „Întotdeauna” pentru WanderTale din
setările telefonului — narațiunea în fundal are nevoie de ea. O poți schimba oricând înapoi pe „Când folosesc aplicația”.</p>
<p><strong>O poveste e greșită.</strong> Poveștile sunt generate cu AI și pot conține greșeli. Trimite-ne numele locului,
limba și, dacă poți, o captură de ecran — corectăm povestea fără o actualizare a aplicației.</p>
<p><strong>Cum îmi șterg contul?</strong> Din <strong>Setări → Șterge contul</strong>, sau vezi
<a href="/legal/wandertale-ro.html#delete">ștergerea contului</a>.</p>
"""}

WT_L = {
 "en": dict(file="", other="-ro", other_label="Română", updated="Last updated", support="Support",
            h1="WanderTale — terms,<br>privacy &amp; your account", terms="Terms", privacy="Privacy",
            delete="Account deletion", t_terms="Terms of use", t_privacy="Privacy policy", t_delete="Deleting your account",
            title="WanderTale — Terms, privacy & account deletion",
            desc="Terms of use, privacy policy and account deletion for the WanderTale app.",
            s_title="WanderTale — Support", s_desc="Contact and frequently asked questions for the WanderTale app."),
 "ro": dict(file="-ro", other="", other_label="English", updated="Ultima actualizare", support="Suport",
            h1="WanderTale — termeni,<br>confidențialitate &amp; contul tău", terms="Termeni", privacy="Confidențialitate",
            delete="Ștergerea contului", t_terms="Termeni de utilizare", t_privacy="Politica de confidențialitate",
            t_delete="Ștergerea contului", title="WanderTale — Termeni, confidențialitate și ștergerea contului",
            desc="Termenii de utilizare, politica de confidențialitate și ștergerea contului pentru aplicația WanderTale.",
            s_title="WanderTale — Suport", s_desc="Contact și întrebări frecvente pentru aplicația WanderTale."),
}

for lang, L in WT_L.items():
    legal = f"/legal/wandertale{L['file']}.html"
    sup = f"/support/wandertale{L['file']}.html"
    body = f"""
<section class="doc"><div class="wrap">
  <a class="back" href="/">← Dragan.me</a>
  <div class="upd" style="margin-top:26px">{L['updated']} {WT_UPDATED[lang]}</div>
  <h1>{L['h1']}</h1>
  <div class="toc">
    <a href="#terms">{L['terms']}</a><a href="#privacy">{L['privacy']}</a>
    <a href="#delete">{L['delete']}</a><a href="{sup}">{L['support']}</a>
    <a href="/legal/wandertale{L['other']}.html" hreflang="{'ro' if lang == 'en' else 'en'}">{L['other_label']}</a>
  </div>
  {sec("01",L['t_terms'],WT_TERMS[lang],"terms")}
  {sec("02",L['t_privacy'],WT_PRIVACY[lang],"privacy")}
  {sec("03",L['t_delete'],WT_DELETE[lang],"delete")}
</div></section>
"""
    (OUT/"legal"/f"wandertale{L['file']}.html").write_text(
        page(L['title'], L['desc'], body, LEGAL_CSS, lang=lang), encoding="utf-8")
    body = f"""
<section class="doc"><div class="wrap">
  <a class="back" href="/">← Dragan.me</a>
  <div class="upd" style="margin-top:26px">{L['support']}</div>
  <h1>WanderTale — {L['support'].lower()}</h1>
  <div class="toc"><a href="{legal}#terms">{L['terms']}</a><a href="{legal}#privacy">{L['privacy']}</a><a href="{legal}#delete">{L['delete']}</a>
    <a href="/support/wandertale{L['other']}.html" hreflang="{'ro' if lang == 'en' else 'en'}">{L['other_label']}</a></div>
  <section class="sec">{WT_SUPPORT[lang]}</section>
</div></section>
"""
    (OUT/"support"/f"wandertale{L['file']}.html").write_text(
        page(L['s_title'], L['s_desc'], body, LEGAL_CSS, lang=lang), encoding="utf-8")
print("legal/wandertale{,-ro}.html + support/wandertale{,-ro}.html")

#!/usr/bin/env python3
"""dragan.me — index cu 4 dale + cate o pagina de showcase per aplicatie."""
import pathlib, importlib.util, sys

HERE = pathlib.Path(__file__).parent
OUT = HERE / "site"; OUT.mkdir(exist_ok=True)
spec = importlib.util.spec_from_file_location("parts", HERE / "parts.py")
parts = importlib.util.module_from_spec(spec); spec.loader.exec_module(parts)

PALETTE = """--bg:#FAFAF8; --card:#FFFFFF; --ink:#1A1A18; --muted:#6E6C66;
    --line:#E2E0DA; --edge:#B9B6AE; --soft:#F0EFEA; --pill-ink:#5E5C57;"""

WINS = '<div class="win"></div>' * 28

SCENE_HTML = {
 "emas": f'<div class="grid-lines"></div><div class="crane"></div><div class="facade">{WINS}</div>'
         '<div class="logotype">EMAS</div><div class="sublabel">Residence</div>',
 "plomus": '<div class="p-grid"></div><div class="cross h"></div><div class="cross v"></div>'
           '<div class="ring r1"></div><div class="ring r2"></div><div class="ring r3"></div>'
           '<div class="sweep"></div><div class="sweep-line"></div>'
           '<div class="blip b1"></div><div class="blip b2"></div><div class="blip b3"></div><div class="blip b4"></div>'
           '<div class="logotype">Plomus</div><div class="sublabel">Property radar</div>',
 "bibliada": '<div class="spine"></div><div class="gilt"></div><div class="passage">'
             '<span class="ln">Cuvântul Tău este o candelă</span><span class="ln">pentru picioarele mele</span>'
             '<span class="ln">și o lumină pe cărarea mea.</span><span class="ref">Psalmul 119:105</span></div>'
             '<div class="logotype">Bibliada</div><div class="sublabel">Daily scripture games</div>',
 "bnp": '<div class="rays"></div><div class="haze"></div><div class="horizon"></div><div class="sun"></div>'
        '<div class="mote m1"></div><div class="mote m2"></div><div class="mote m3"></div><div class="mote m4"></div>'
        '<div class="logotype">Breakfast &amp; Pray</div><div class="sublabel">Morning community</div>',
}

PROJECTS = [
 dict(slug="emas", scene="emas", idx="01", kind="Real Estate Platform",
   status="Live", name="EMAS Residence", short="Real-estate sales, from the site map down to one apartment.",
   tagline="Proprietatea ta, simplificată.",
   intro="A sales platform for a residential development. Parcels, blocks and apartments live in one model, "
         "so a buyer scrolls from the site map down to a single unit without ever losing the thread.",
   features=[("Site map to unit","One scroll walks the buyer from the parcel plan to a block, a floor and finally one apartment."),
             ("Live availability","Sold, reserved and free units update in place — no stale PDF price lists."),
             ("Unit dossier","Surface, orientation, floor plan and price kept on the unit itself."),
             ("Reservation trail","Interest, reservation and paperwork stages tracked per unit."),
             ("Mobile app","The same catalogue in the sales agent's pocket, built in React Native.")],
   stack=["NestJS","Angular","React Native","PostgreSQL","iOS"],
   links=[("primary","Visit site","https://emasresidence.ro"),
          ("ghost","Privacy","https://emasresidence.ro/privacy"),
          ("ghost","Terms","https://emasresidence.ro/termeni"),
          ("ghost","Support","mailto:contact@dragan.me?subject=EMAS%20Residence")]),

 dict(slug="plomus", scene="plomus", idx="02", kind="Real Estate SaaS",
   status="Live", name="Plomus", short="A radar for Romanian agents: every new listing, the second it appears.",
   tagline="Radarul tău imobiliar.",
   intro="A working platform for Romanian agents and ANEVAR appraisers. Listings are scraped from every portal, "
         "matched against your buyers, and pushed to you the moment one lands inside a zone you drew.",
   features=[("Zone alerts","Draw a zone on the map; anything new inside it reaches you in seconds."),
             ("Portal scraping","Listings pulled continuously from the Romanian portals, deduplicated and geocoded."),
             ("Buyer matching","Every listing is scored against your clients' criteria — hot matches surface first."),
             ("CRM for agents","Clients, leads, viewings, deals and commissions in one pipeline."),
             ("Market intel","Local price movement, comparables and a morning brief in your inbox."),
             ("Web and mobile","Angular on the desktop, React Native on iOS and Android, one API behind both.")],
   stack=["NestJS","Angular","React Native","PostgreSQL","Maps","Scraping","LLM"],
   links=[("primary","Visit site","https://plomus.ro"),
          ("ghost","Privacy","https://plomus.ro/privacy"),
          ("ghost","Terms","https://plomus.ro/terms"),
          ("ghost","Support","mailto:contact@dragan.me?subject=Plomus")]),

 dict(slug="bibliada", scene="bibliada", idx="03", kind="Daily Bible Game",
   status="In development", name="Bibliada", short="Thirteen daily Scripture puzzles, one streak to keep.",
   tagline="Cunoaște Scriptura, verset cu verset.",
   intro="A daily game built on Scripture. Thirteen puzzle types, one round a day, a streak worth protecting — "
         "and a weekly league that keeps a small group reading together.",
   features=[("Thirteen games","Verse detective, who said it, word order, timeline, odd one out, two truths, and more."),
             ("One round a day","Server-authoritative daily puzzle, the same for everyone, keyed to the date."),
             ("XP and streaks","Progress is event-sourced, so a streak survives a bad connection or a reinstall."),
             ("Weekly leagues","Cohorts of about thirty players, ten tiers, promotion every Monday."),
             ("Live duels","Head-to-head rounds against a friend."),
             ("Offline first","Play with no signal; the server reconciles when you come back."),
             ("Three languages","Romanian, English and Spanish content packs kept in parity by a checker.")],
   stack=["React Native","NestJS","PostgreSQL","Redis","BullMQ","RO · EN · ES"],
   links=[("dead","Coming 2026",""),
          ("ghost","Privacy","/legal/bibliada/privacy.html"),
          ("ghost","Terms","/legal/bibliada/terms.html"),
          ("ghost","Notify me","mailto:contact@dragan.me?subject=Bibliada")]),

 dict(slug="breakfast-pray", scene="bnp", idx="04", kind="Faith Community",
   status="On the App Store", name="Breakfast &amp; Pray", short="A quiet circle for prayer, kept off the noisy feeds.",
   tagline="Comunitatea de mic dejun cu rugăciune.",
   intro="An app for a real breakfast circle. Prayer requests, answers and testimonies stay inside the group — "
         "the design is deliberately calm, and nothing about it is built to be endless.",
   features=[("Private groups","Invite-only circles with roles for the people who host the table."),
             ("Prayer requests","Post a request, mark it answered, and keep the answer with it."),
             ("A calm feed","Chronological, no ranking, no infinite scroll."),
             ("Comments","Short replies in place, so a thread stays a conversation."),
             ("Moderation","Validation of new members and roles the host controls."),
             ("Push, sparingly","Notified when your circle needs you, not when an algorithm wants you.")],
   stack=["React Native","NestJS","PostgreSQL","iOS","Push"],
   links=[("primary","App Store","https://apps.apple.com/ro/app/breakfast-pray/id6765490933"),
          ("ghost","Privacy","/legal/breakfast-pray/privacy.html"),
          ("ghost","Terms","/legal/breakfast-pray/terms.html"),
          ("ghost","Support","mailto:contact@dragan.me?subject=Breakfast%20%26%20Pray")]),
]

def acts(links):
    out=[]
    for kind,label,href in links:
        if kind=="primary": out.append(f'<a class="act primary" href="{href}" target="_blank" rel="noopener">{label} <span aria-hidden="true">&#8599;</span></a>')
        elif kind=="dead":  out.append(f'<span class="act dead">{label}</span>')
        else:               out.append(f'<a class="act ghost" href="{href}">{label}</a>')
    return "\n        ".join(out)

# ------------------------------------------------------------------ shell
def page(title, desc, body, extra_css="", home=False):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#FAFAF8">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90' font-family='Georgia,serif'>D</text></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500&family=Jost:wght@200;300;400;500&display=swap" rel="stylesheet">
<style>
  :root{{{PALETTE}
    --display:"Cormorant Garamond", Georgia, serif;
    --sans:"Jost", -apple-system, system-ui, sans-serif;}}
  *{{box-sizing:border-box;margin:0;padding:0}}
  html{{scroll-behavior:smooth}}
  body{{background:var(--bg);color:var(--ink);font-family:var(--sans);font-weight:300;line-height:1.6;-webkit-font-smoothing:antialiased;overflow-x:hidden}}
  ::selection{{background:var(--ink);color:var(--bg)}}
  a{{color:inherit}}
  .wrap{{max-width:1320px;margin:0 auto;padding:0 clamp(24px,5vw,80px)}}
  .eyebrow{{font-weight:200;font-size:11px;letter-spacing:.34em;text-transform:uppercase;color:var(--muted)}}

  header.site{{position:sticky;top:0;z-index:50;backdrop-filter:blur(8px);background:color-mix(in srgb,var(--bg) 85%,transparent);border-bottom:1px solid transparent;transition:border-color .4s}}
  header.site.scrolled{{border-bottom-color:var(--line)}}
  .site-inner{{display:flex;align-items:center;justify-content:space-between;height:74px}}
  @media(max-width:640px){{.site-inner{{height:62px}}nav.top a{{margin-left:22px}}}}
  .brand{{font-family:var(--display);font-weight:400;font-size:24px;letter-spacing:.02em;text-decoration:none}}
  .brand span{{color:var(--muted)}}
  nav.top a{{font-size:11px;letter-spacing:.28em;text-transform:uppercase;color:var(--muted);text-decoration:none;margin-left:32px;transition:color .25s}}
  nav.top a:hover{{color:var(--ink)}}

  /* ---- scene (aceleasi in index si in paginile de produs) ---- */
  .visual{{position:relative;overflow:hidden;display:flex;align-items:center;justify-content:center;background:var(--vs-bg)}}
  .visual .logotype{{font-family:var(--display);font-weight:300;letter-spacing:.03em;text-align:center;line-height:1;z-index:5;color:var(--vs-ink)}}
  .visual .sublabel{{position:absolute;bottom:20px;left:0;right:0;text-align:center;font-size:10px;letter-spacing:.3em;text-transform:uppercase;z-index:5;color:var(--vs-mut)}}
{parts.SCENES}
  .act{{font-size:10px;letter-spacing:.2em;text-transform:uppercase;text-decoration:none;color:var(--ink);
    border:1px solid var(--edge);border-radius:100px;padding:10px 18px;transition:.25s;white-space:nowrap;display:inline-block}}
  .act.primary:hover{{background:var(--ink);color:var(--bg);border-color:var(--ink)}}
  .act.ghost{{border-color:transparent;color:var(--muted);padding:10px 12px}}
  .act.ghost:hover{{color:var(--ink);border-color:var(--line)}}
  .act.dead{{border-style:dashed;color:var(--muted);cursor:default}}
  .acts{{display:flex;align-items:center;gap:8px;flex-wrap:wrap}}

  footer.site{{padding:80px 0 64px;border-top:1px solid var(--line);margin-top:clamp(60px,10vh,120px)}}
  .foot-grid{{display:flex;justify-content:space-between;align-items:flex-end;flex-wrap:wrap;gap:30px}}
  footer .big{{font-family:var(--display);font-weight:300;font-size:clamp(32px,5vw,52px);line-height:1}}
  footer a.mail{{text-decoration:none;border-bottom:1px solid var(--line);padding-bottom:3px;transition:border-color .3s}}
  footer a.mail:hover{{border-color:var(--ink)}}
  .foot-meta{{font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--muted);text-align:right;line-height:2}}
  @media(max-width:640px){{.foot-meta{{text-align:left}}footer.site{{padding:56px 0 48px}}}}
  .foot-legal{{margin-top:40px;display:flex;gap:24px;flex-wrap:wrap;font-size:10px;letter-spacing:.2em;text-transform:uppercase}}
  .foot-legal a{{color:var(--muted);text-decoration:none}}
  .foot-legal a:hover{{color:var(--ink)}}

  .reveal{{opacity:0;transform:translateY(20px);transition:opacity .9s ease,transform .9s ease}}
  .reveal.in{{opacity:1;transform:none}}
  @media(prefers-reduced-motion:reduce){{
    .reveal{{opacity:1;transform:none;transition:none}}
    .win,.crane,.sweep,.sweep-line,.blip,.passage .ln,.passage .ref,.gilt,.rays,.sun,.haze,.mote{{animation:none!important}}
    .passage .ln,.passage .ref,.blip{{opacity:1}} html{{scroll-behavior:auto}}
  }}
{extra_css}
</style>
</head>
<body>
<header class="site" id="siteHeader">
  <div class="wrap site-inner">
    <a class="brand" href="{'#top' if home else 'index.html'}">Dragan<span>.me</span></a>
    <nav class="top">{'<a href="#work">Work</a><a href="#contact">Contact</a>' if home else '<a href="index.html">All work</a><a href="#contact">Contact</a>'}</nav>
  </div>
</header>
{body}
<footer class="site" id="contact">
  <div class="wrap">
    <div class="foot-grid">
      <div><div class="eyebrow" style="margin-bottom:18px">Get in touch</div>
        <div class="big"><a class="mail" href="mailto:contact@dragan.me">contact@dragan.me</a></div></div>
      <div class="foot-meta">Dragan Software Ultimate S.R.L.<br>Timișoara · România<br>© 2026</div>
    </div>
    <div class="foot-legal">
      <a href="index.html">Work</a><a href="/legal/privacy.html">Privacy</a>
      <a href="/legal/terms.html">Terms</a><a href="mailto:contact@dragan.me?subject=Support">Support</a>
    </div>
  </div>
</footer>
<script>
  const h=document.getElementById('siteHeader');
  addEventListener('scroll',()=>{{h.classList.toggle('scrolled',scrollY>12)}},{{passive:true}});
  const cue=document.getElementById('cue');
  if(cue) addEventListener('scroll',()=>{{cue.classList.toggle('gone',scrollY>60)}},{{passive:true}});
  const io=new IntersectionObserver(es=>es.forEach(e=>{{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target)}}}}),{{threshold:.14}});
  document.querySelectorAll('.reveal').forEach((el,i)=>{{el.style.transitionDelay=(i%2*110)+'ms';io.observe(el)}});
</script>
</body>
</html>
"""

# ------------------------------------------------------------------ index
INDEX_CSS = """
  .intro{height:calc(100svh - 74px);display:flex;flex-direction:column;justify-content:center;position:relative;padding:0}
  .intro > .wrap{width:100%}
  .scrollcue{position:absolute;left:0;right:0;bottom:clamp(64px,15vh,150px);display:flex;justify-content:center;
    transition:opacity .5s ease}
  .scrollcue.gone{opacity:0;pointer-events:none}
  .scrollcue a{display:block;padding:10px;line-height:0;color:var(--muted);transition:color .3s}
  .scrollcue a:hover{color:var(--ink)}
  .scrollcue svg{overflow:visible}
  .scrollcue .stem{animation:cueStem 2.6s ease-in-out infinite}
  .scrollcue .head{animation:cueHead 2.6s ease-in-out infinite}
  @keyframes cueStem{0%,100%{transform:translateY(0);opacity:.45}45%{transform:translateY(5px);opacity:1}}
  @keyframes cueHead{0%,100%{transform:translateY(0);opacity:.45}45%{transform:translateY(8px);opacity:1}}
  @media(prefers-reduced-motion:reduce){.scrollcue .stem,.scrollcue .head{animation:none}}
  .intro h1{font-family:var(--display);font-weight:300;font-size:clamp(44px,7.4vw,96px);line-height:1;letter-spacing:-.015em;margin:20px 0 0}
  .intro h1 .soft{color:var(--muted)}
  .intro .place{margin-top:24px;font-size:10px;letter-spacing:.26em;text-transform:uppercase;color:var(--muted)}

  .show{padding:clamp(56px,10vh,120px) 0 0;border-top:1px solid var(--line)}
  .show:first-of-type{border-top:0;padding-top:0}
  .phead{display:flex;align-items:flex-end;justify-content:space-between;gap:28px;flex-wrap:wrap;margin:0 0 30px}
  .phead h2{font-family:var(--display);font-weight:300;font-size:clamp(40px,6.4vw,84px);line-height:1;letter-spacing:-.015em}
  .phead .tagline{font-family:var(--display);font-size:clamp(18px,2vw,24px);color:var(--muted);margin-top:12px}
  .pstatus{font-size:10px;letter-spacing:.24em;text-transform:uppercase;color:var(--muted);padding-bottom:10px;white-space:nowrap}
  .stage{border:1px solid var(--line);border-radius:18px;overflow:hidden}
  .stage .visual{min-height:clamp(340px,52vh,580px)}
  .stage .visual .logotype{font-size:clamp(42px,6.4vw,80px)}
  .pbody{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.25fr);gap:clamp(30px,6vw,90px);padding:clamp(44px,7vh,88px) 0 0}
  .pbody .lede{font-family:var(--display);font-size:clamp(20px,2.2vw,28px);line-height:1.45;font-weight:400}
  .feat div{padding:20px 0;border-top:1px solid var(--line)}
  .feat div:first-child{border-top:0;padding-top:0}
  .feat h3{font-size:12px;font-weight:400;letter-spacing:.2em;text-transform:uppercase;margin-bottom:6px}
  .feat p{font-size:14px;color:var(--muted);max-width:56ch}
  .prow{display:flex;justify-content:space-between;gap:30px;flex-wrap:wrap;align-items:center;
    margin-top:clamp(40px,6vh,72px);padding-bottom:clamp(24px,5vh,52px)}
  .stack{display:flex;flex-wrap:wrap;gap:7px}
  .stack span{font-size:9px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);border:1px solid var(--line);border-radius:100px;padding:6px 12px}
  @media(max-width:860px){.pbody{grid-template-columns:1fr;gap:30px}}
  @media(max-width:640px){
    .intro{height:calc(100svh - 62px)}
    .stage{border-radius:14px}
    .stage .visual{min-height:clamp(240px,34svh,380px)}
    .stage .visual .logotype{font-size:clamp(30px,9vw,44px)}
    .phead{margin-bottom:22px;align-items:flex-start;flex-direction:column;gap:10px}
    .phead .pstatus{order:-1;padding-bottom:0}
    .pbody{padding-top:34px}
    .prow{flex-direction:column;align-items:flex-start;gap:20px;margin-top:34px}
    .acts{gap:6px}
    .act{padding:9px 14px}
    .act.ghost{padding:9px 8px}
  }
"""

def showcase(p):
    feats = "".join(f"<div><h3>{t}</h3><p>{d}</p></div>" for t,d in p["features"])
    stack = "".join(f"<span>{t}</span>" for t in p["stack"])
    return f"""
<section class="show" id="{p['slug']}">
  <div class="wrap">
    <div class="phead reveal">
      <div><h2>{p['name']}</h2><div class="tagline">{p['tagline']}</div></div>
      <div class="pstatus">{p['idx']} — {p['kind']} · {p['status']}</div>
    </div>
    <div class="stage reveal"><div class="visual v-{p['scene']}">{SCENE_HTML[p['scene']]}</div></div>
    <div class="pbody">
      <p class="lede reveal">{p['intro']}</p>
      <div class="feat reveal">{feats}</div>
    </div>
    <div class="prow">
      <div class="stack">{stack}</div>
      <div class="acts">{acts(p['links'])}</div>
    </div>
  </div>
</section>"""

index_body = f"""
<section class="intro" id="top">
  <div class="wrap">
    <h1 class="reveal">Products we<br>design &amp; <span class="soft">build.</span></h1>
    <div class="place reveal">Timișoara · România</div>
  </div>
  <div class="scrollcue" id="cue">
    <a href="#emas" aria-label="Scroll to work">
      <svg width="14" height="34" viewBox="0 0 14 34" fill="none" stroke="currentColor" stroke-width="1">
        <line class="stem" x1="7" y1="0" x2="7" y2="22"/>
        <polyline class="head" points="2,19 7,25 12,19"/>
      </svg>
    </a>
  </div>
</section>
{''.join(showcase(p) for p in PROJECTS)}
"""

# ------------------------------------------------------------------ product page
PRODUCT_CSS = """
  .phero{padding:clamp(52px,8vh,96px) 0 0}
  .back{font-size:10px;letter-spacing:.24em;text-transform:uppercase;color:var(--muted);text-decoration:none}
  .back:hover{color:var(--ink)}
  .phead{display:flex;align-items:flex-end;justify-content:space-between;gap:28px;flex-wrap:wrap;margin:26px 0 30px}
  .phead h1{font-family:var(--display);font-weight:300;font-size:clamp(44px,7vw,92px);line-height:1;letter-spacing:-.015em}
  .phead .tagline{font-family:var(--display);font-size:clamp(18px,2vw,24px);color:var(--muted);margin-top:12px}
  .pstatus{font-size:10px;letter-spacing:.24em;text-transform:uppercase;color:var(--muted);padding-bottom:10px}
  .stage{border:1px solid var(--line);border-radius:18px;overflow:hidden}
  .stage .visual{min-height:clamp(360px,56vh,620px)}
  .stage .visual .logotype{font-size:clamp(44px,7vw,86px)}
  .pbody{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.25fr);gap:clamp(30px,6vw,90px);padding:clamp(48px,8vh,96px) 0 0}
  .pbody .lede{font-family:var(--display);font-size:clamp(20px,2.2vw,28px);line-height:1.45;font-weight:400}
  .feat{display:grid;gap:0}
  .feat div{padding:22px 0;border-top:1px solid var(--line)}
  .feat div:first-child{border-top:0;padding-top:0}
  .feat h3{font-size:12px;font-weight:400;letter-spacing:.2em;text-transform:uppercase;margin-bottom:6px}
  .feat p{font-size:14px;color:var(--muted);max-width:56ch}
  .prow{display:flex;justify-content:space-between;gap:30px;flex-wrap:wrap;align-items:center;
    margin-top:clamp(44px,7vh,80px);padding-top:26px;border-top:1px solid var(--line)}
  .stack{display:flex;flex-wrap:wrap;gap:7px}
  .stack span{font-size:9px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);border:1px solid var(--line);border-radius:100px;padding:6px 12px}
  .pnext{display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap;
    margin-top:clamp(56px,9vh,110px);padding-top:28px;border-top:1px solid var(--line);
    font-size:11px;letter-spacing:.24em;text-transform:uppercase;color:var(--muted)}
  .pnext a{text-decoration:none}
  .pnext a:hover{color:var(--ink)}
  .pnext .nname{font-family:var(--display);font-size:26px;letter-spacing:0;text-transform:none;color:var(--ink)}
  @media(max-width:860px){.pbody{grid-template-columns:1fr;gap:34px}}
"""

def product_page(p, nxt):
    feats = "".join(f"<div><h3>{t}</h3><p>{d}</p></div>" for t,d in p["features"])
    stack = "".join(f"<span>{t}</span>" for t in p["stack"])
    body = f"""
<section class="phero">
  <div class="wrap">
    <a class="back" href="index.html">← All work</a>
    <div class="phead">
      <div><h1>{p['name']}</h1><div class="tagline">{p['tagline']}</div></div>
      <div class="pstatus">{p['idx']} — {p['kind']} · {p['status']}</div>
    </div>
    <div class="stage reveal"><div class="visual v-{p['scene']}">{SCENE_HTML[p['scene']]}</div></div>
    <div class="pbody">
      <p class="lede reveal">{p['intro']}</p>
      <div class="feat reveal">{feats}</div>
    </div>
    <div class="prow">
      <div class="stack">{stack}</div>
      <div class="acts">{acts(p['links'])}</div>
    </div>
    <div class="pnext">
      <span>Next</span>
      <a href="{nxt['slug']}.html"><span class="nname">{nxt['name']}</span> &nbsp;→</a>
    </div>
  </div>
</section>
"""
    return page(f"{p['name'].replace('&amp;','&')} — Dragan", p["short"], body, PRODUCT_CSS)

(OUT/"index.html").write_text(page("Dragan — Work",
  "A small engineering studio in Timișoara. EMAS Residence, Plomus, Bibliada and Breakfast & Pray.",
  index_body, INDEX_CSS, home=True), encoding="utf-8")
print("\n".join(f"{f.name}  {f.stat().st_size//1024}KB" for f in sorted(OUT.glob('*.html'))))

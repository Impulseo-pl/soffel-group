#!/usr/bin/env python3
"""Generator demo Soffel Group — buduje *.html w katalogu głównym repo.
Uruchom: python3 tools/build.py   (po zmianie CSS/JS hash cache-bustera liczy się sam)
Wszystko, czego brakuje od klienta, jest oznaczone klasą .ph / .ph-img (placeholder)."""
import hashlib, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://impulseo-pl.github.io/soffel-group/"

def h(p): return hashlib.md5((ROOT / p).read_bytes()).hexdigest()[:8]
V_CSS, V_JS = h("assets/styles.css"), h("assets/main.js")

# ---------------------------------------------------------------- ikony
I = {
 "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12h16m-6-6 6 6-6 6"/></svg>',
 "arrow-ur": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17 17 7M8 7h9v9"/></svg>',
 "img": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="2"/><path d="m21 16-5-5-9 9"/></svg>',
 "user": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/></svg>',
 "search": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>',
 "key": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="8" cy="15" r="4"/><path d="m11 12 9-9m-3 3 3 3m-6 0 2 2"/></svg>',
 "brush": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M14 4h6v6M20 4l-8 8M4 20c0-3 2-5 4-5s3 1 3 3-2 2-4 2H4Z"/></svg>',
 "chart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 20h18M6 16l4-5 3 3 6-8"/><path d="M15 6h4v4"/></svg>',
 "sun": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M4.9 4.9l1.4 1.4m11.4 11.4 1.4 1.4M2 12h2m16 0h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>',
 "plane": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13 3 10l1-2 8 1 4-5c1-1 3-1 3 0s0 2-1 3l-5 4 1 8-2 1-3-7-3 2v3l-2 1-1-4-4-1 1-2h3Z"/></svg>',
 "users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c0-3.5 3-5.5 6.5-5.5s6.5 2 6.5 5.5"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14.6c2.2.6 3.5 2.4 3.5 5.4"/></svg>',
 "user1": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/></svg>',
 "bank": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 10 12 4l9 6M5 10v8m4-8v8m6-8v8m4-8v8M3 21h18"/></svg>',
 "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6l-8-3Z"/><path d="m9 12 2 2 4-4"/></svg>',
 "doc": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M14 3H6v18h12V7l-4-4Z"/><path d="M14 3v4h4M9 13h6M9 17h6"/></svg>',
 "home": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11 12 4l9 7"/><path d="M5 10v10h14V10M10 20v-6h4v6"/></svg>',
 "loop": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12a8 8 0 0 1 14-5.3L20 9"/><path d="M20 4v5h-5M20 12a8 8 0 0 1-14 5.3L4 15"/><path d="M4 20v-5h5"/></svg>',
 "sparkle": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v4m0 10v4M3 12h4m10 0h4M6 6l2.5 2.5m7 7L18 18M18 6l-2.5 2.5m-7 7L6 18"/></svg>',
 "bed": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 18V6m0 8h18v4M21 14v-2a3 3 0 0 0-3-3h-7v5"/><circle cx="7" cy="11" r="2"/></svg>',
 "tool": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a4 4 0 0 0 5 5L21 13l-8 8-5-5 8-8-1.3-1.7ZM3 21l5-5"/></svg>',
 "ruler": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="m3 17 14-14 4 4L7 21l-4-4Z"/><path d="m7 13 2 2m1-5 2 2m1-5 2 2"/></svg>',
 "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12 5 5 9-10"/></svg>',
 "close": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"/></svg>',
 "left": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="m15 6-6 6 6 6"/></svg>',
 "right": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="m9 6 6 6-6 6"/></svg>',
 "calendar": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4m8-4v4"/></svg>',
 "eye": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12Z"/><circle cx="12" cy="12" r="3"/></svg>',
}

# ---------------------------------------------------------------- dane
DIVS = [
  dict(key="inv",   name="Investments", pl="Inwestycje",    url="inwestycje.html",    c="#d6b26a", img="s-gold",
       tag="Acquire · Renovate · Return", flag="Flagowy",
       desc="Flip nieruchomości na Costa del Sol — zakup, renowacja i sprzedaż z zyskiem. Dla jednego inwestora lub grupy współinwestorów."),
  dict(key="prop",  name="Properties",  pl="Nieruchomości", url="nieruchomosci.html", c="#3fcf72", img="s-green",
       tag="Real Estate Agency", flag="",
       desc="Pośrednictwo w zakupie i sprzedaży nieruchomości oraz zarządzanie najmem krótkoterminowym."),
  dict(key="reno",  name="Renovations", pl="Renowacje",     url="renowacje.html",     c="#a76cff", img="s-purple",
       tag="Build · Transform · Improve", flag="",
       desc="Projekt, remont i wykończenie pod klucz — od odświeżenia apartamentu po kompleksową przebudowę willi."),
  dict(key="clean", name="Cleaning",    pl="Sprzątanie",    url="sprzatanie.html",    c="#3aa6ff", img="s-blue",
       tag="Cleaner · Brighter · Spaces", flag="",
       desc="Sprzątanie po najemcach, przygotowanie apartamentu na przyjazd gości i bieżąca opieka nad nieruchomością."),
]
D = {x["key"]: x for x in DIVS}

LOCS = ["Marbella", "Málaga", "Estepona", "Benahavís", "Mijas", "Fuengirola", "Nueva Andalucía", "Benalmádena"]

PHOTOS = {  # zdjęcia od klienta (realizacje wykończeń)
 "salon-1": "Salon z aneksem kuchennym i wyjściem na taras",
 "kuchnia-salon": "Kuchnia z wyspą i strefą dzienną",
 "sypialnia-lustro": "Sypialnia z okrągłym podświetlanym lustrem",
 "lazienka-wanna": "Łazienka z wolnostojącą wanną i prysznicem walk-in",
 "kuchnia-wyspa": "Wyspa kuchenna z kamienia i podłoga w jodełkę",
 "lazienka-kamien": "Łazienka z kamienną umywalką i oświetleniem liniowym",
 "korytarz-polki": "Zabudowa z podświetlanymi półkami",
 "lazienka-prysznic": "Łazienka z prysznicem i lustrem w czarnej ramie",
 "antresola": "Antresola z widokiem na salon",
 "sypialnia-2": "Sypialnia z drewnianą ścianą",
 "salon-2": "Strefa dzienna po wykończeniu",
 "korytarz": "Korytarz z oświetleniem liniowym",
 "lazienka-3": "Łazienka z wanną i ścianą 3D",
 "lazienka-4": "Łazienka z wanną zabudowaną kamieniem",
 "budowa-sufit": "Etap prac: konstrukcja sufitu podwieszanego",
 "budowa-2": "Etap prac: płyty i instalacje",
 "budowa-3": "Etap prac: instalacje wentylacji",
}

def ph(text="do uzupełnienia"):
    return f'<span class="ph">{text}</span>'

def ph_img(label, sub="", cls="", style=""):
    return (f'<div class="ph-img {cls}" style="{style}" role="img" aria-label="Miejsce na zdjęcie: {label}"><div class="ph-in">{I["img"]}'
            f'<b>Miejsce na zdjęcie</b><span>{label}</span>{f"<span>{sub}</span>" if sub else ""}</div></div>')

def photo(name, cls="", sizes="(max-width: 900px) 100vw, 50vw", eager=False):
    return (f'<img src="img/{name}.webp" srcset="img/{name}-s.webp 640w, img/{name}.webp 1200w" sizes="{sizes}" '
            f'alt="{PHOTOS[name]}" class="{cls}" loading="{"eager" if eager else "lazy"}" decoding="async" width="1200" height="1600">')

# ---------------------------------------------------------------- SVG wstęg
def ribbons(uid="r"):
    return f'''<svg class="ribbons" viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
  <defs>
    <linearGradient id="{uid}b1" x1="0" y1="0" x2="1" y2="1"><stop offset="0" style="stop-color:var(--rib-1)" stop-opacity=".55"/><stop offset="1" style="stop-color:var(--rib-2)" stop-opacity=".05"/></linearGradient>
    <linearGradient id="{uid}b2" x1="0" y1="1" x2="1" y2="0"><stop offset="0" style="stop-color:var(--rib-2)" stop-opacity=".95"/><stop offset="1" style="stop-color:var(--rib-1)" stop-opacity=".25"/></linearGradient>
  </defs>
  <g class="drift">
    <path class="band" fill="url(#{uid}b1)" d="M1000,-40 C1170,120 1230,380 1140,560 C1070,720 1160,860 1500,940 L1500,-40 Z"/>
    <path class="band" fill="url(#{uid}b2)" d="M-60,790 C220,760 430,820 660,870 C780,895 900,920 1010,950 L-60,950 Z"/>
    <path class="band" fill="url(#{uid}b1)" opacity=".55" d="M-60,800 C300,760 520,700 800,640 C1060,585 1270,455 1500,300 L1500,345 C1270,505 1060,640 800,690 C520,745 300,805 -60,850 Z"/>
    <path class="gl" d="M-60,825 C300,782 520,720 800,665 C1060,610 1270,480 1500,320"/>
    <path class="gl d2" d="M1070,-40 C1190,140 1210,420 1120,600 C1050,760 1160,880 1500,930"/>
    <path class="gl d3" d="M-60,885 C240,860 450,880 670,915 C770,930 850,945 910,960"/>
    <circle class="spark" cx="1290" cy="462" r="3"/>
    <circle class="spark s2" cx="1120" cy="600" r="2.6"/>
  </g>
</svg>'''

HERO_CLIP = "M0.985,0.015 C0.63,-0.005 0.13,0.13 0.035,0.5 C-0.045,0.83 0.29,1 0.6,0.985 C0.87,0.97 1,0.79 1,0.52 L1,0.015 Z"
HERO_FRAME = "M98.5,1.5 C63,-0.5 13,13 3.5,50 C-4.5,83 29,100 60,98.5 C87,97 100,79 100,52"

def svg_defs():
    return f'''<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
  <clipPath id="heroClip" clipPathUnits="objectBoundingBox"><path d="{HERO_CLIP}"/></clipPath>
  <linearGradient id="gGold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f6e6b8"/><stop offset=".45" stop-color="#d4ae62"/><stop offset="1" stop-color="#8d672b"/></linearGradient>
</defs></svg>'''

# ---------------------------------------------------------------- szkielet
NAV = [("inv", "Inwestycje", "inwestycje.html"), ("prop", "Nieruchomości", "nieruchomosci.html"),
       ("reno", "Renowacje", "renowacje.html"), ("clean", "Sprzątanie", "sprzatanie.html"), ("about", "O nas", "o-nas.html")]

def head(title, desc, slug, theme_color="#04120d"):
    ld = {
        "@context": "https://schema.org", "@type": "RealEstateAgent", "name": "Soffel Group",
        "slogan": "People | Property | Better Living", "url": BASE, "logo": BASE + "img/s-green.png",
        "areaServed": ["Costa del Sol", "Marbella", "Málaga"],
        "address": {"@type": "PostalAddress", "addressRegion": "Andalucía", "addressCountry": "ES"},
        "subOrganization": [{"@type": "Organization", "name": f"Soffel {d['name']}"} for d in DIVS],
    }
    url = BASE + ("" if slug == "index" else slug + ".html")
    return f'''<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="{theme_color}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pl_PL">
<meta property="og:site_name" content="Soffel Group">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}img/hero-villa.webp">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="img/favicon.png">
<link rel="apple-touch-icon" href="img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/styles.css?v={V_CSS}">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>'''

MENU_IMG = {"inv": "hero-villa", "prop": "kuchnia-salon", "reno": "salon-1", "clean": "lazienka-wanna"}
EXPLORE = [("index.html", "Strona główna"), ("o-nas.html", "O nas"), ("o-nas.html#zespol", "Zespół"),
           ("inwestycje.html#model", "Model inwestycyjny"), ("#kontakt", "Kontakt")]

def header(active):
    big = "".join(
        f'<li><a href="{d["url"]}" style="--c:{d["c"]}" data-mi="{d["key"]}"{" aria-current=page" if d["key"] == active else ""}>'
        f'<small>{i+1:02d}</small><span>{d["name"]}</span></a></li>' for i, d in enumerate(DIVS))
    explore = "".join(f'<li><a href="{u}">{t}</a></li>' for u, t in EXPLORE)
    imgs = '<img class="on" src="img/hero-villa.webp" alt="" data-mi="group" loading="lazy">' + "".join(
        f'<img src="img/{MENU_IMG[d["key"]]}.webp" alt="" data-mi="{d["key"]}" loading="lazy">' for d in DIVS)
    marks = "".join(f'<img src="img/{d["img"]}.webp" alt="" data-mi="{d["key"]}" loading="lazy">' for d in DIVS)
    return f'''<div class="progress" aria-hidden="true"></div>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="Soffel Group — strona główna">
      <img src="img/s-green.webp" alt="" width="44" height="44">
      <span class="brand-t"><b>SOFFEL</b><i>GROUP</i></span>
    </a>
    <button class="burger" type="button" aria-expanded="false" aria-controls="menu">
      <span class="lbl"><span class="t-open">Menu</span><span class="t-close">Zamknij</span></span><span class="bars"></span>
    </button>
  </div>
</header>
<div class="menu" id="menu" aria-hidden="true">
  <div class="menu-grid">
    <nav class="menu-main" aria-label="Marki Soffel Group"><ol>{big}</ol></nav>
    <div class="menu-side">
      <div><p class="menu-h">Eksploruj</p><ul class="menu-links">{explore}</ul></div>
      <div><p class="menu-h">Kontakt</p><ul class="menu-contact"><li>{ph("e-mail")}</li><li>{ph("telefon")}</li><li class="muted">Costa del Sol · Marbella · Málaga</li></ul></div>
    </div>
    <div class="menu-media" aria-hidden="true">
      <figure class="frame-c">{imgs}<span class="menu-mark">{marks}</span></figure>
    </div>
  </div>
</div>'''

def footer():
    divs = "".join(f'<li><a href="{d["url"]}">Soffel {d["name"]}</a></li>' for d in DIVS)
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="foot-top">
      <div>
        <a class="brand" href="index.html"><img src="img/s-green.webp" alt="" width="44" height="44"><span class="brand-t"><b>SOFFEL</b><i>GROUP</i></span></a>
        <p class="about">Inwestycje, pośrednictwo, renowacje i sprzątanie nieruchomości na Costa del Sol — cztery obszary, jeden proces i jeden standard.</p>
        <p class="tagline">People | Property | Better Living</p>
      </div>
      <div><h4>Marki</h4><ul>{divs}</ul></div>
      <div><h4>Firma</h4><ul><li><a href="o-nas.html">O nas</a></li><li><a href="o-nas.html#zespol">Zespół</a></li><li><a href="inwestycje.html#model">Model inwestycyjny</a></li><li><a href="#kontakt">Kontakt</a></li></ul></div>
      <div><h4>Kontakt</h4><ul><li>{ph("telefon")}</li><li>{ph("e-mail")}</li><li>{ph("adres biura")}</li><li>Costa del Sol, Hiszpania</li></ul></div>
    </div>
    <div class="foot-big" aria-hidden="true">Soffel Group</div>
    <div class="foot-bot">
      <span>© 2026 Soffel Group · {ph("dane rejestrowe spółki")}</span>
      <nav><a href="#">Polityka prywatności</a><a href="#">Cookies</a><span>Projekt i wdrożenie: Impulseo</span></nav>
    </div>
  </div>
</footer>
<div class="lb" role="dialog" aria-modal="true" aria-label="Podgląd zdjęcia"><img alt=""><button class="x" type="button" aria-label="Zamknij">{I["close"]}</button><button class="pv" type="button" aria-label="Poprzednie">{I["left"]}</button><button class="nx" type="button" aria-label="Następne">{I["right"]}</button></div>
<script src="assets/main.js?v={V_JS}" defer></script>
</body>
</html>'''

TOPICS = [("inv", "Inwestycja we flip", "#d6b26a"), ("prop", "Kupno / sprzedaż", "#3fcf72"),
          ("reno", "Renowacja", "#a76cff"), ("clean", "Sprzątanie i najem", "#3aa6ff"), ("other", "Inne", "#9aa59f")]

def contact(preset="inv", title='Porozmawiajmy <span class="acc-text">o inwestycji</span>',
            lead="Opisz krótko, czego szukasz. Oddzwonimy, przedstawimy aktualne projekty i odpowiemy na pytania dotyczące modelu współpracy.",
            capital=True):
    chips = "".join(
        f'<label style="--c:{c}"><input type="radio" name="temat" value="{k}"{" checked" if k == preset else ""} required><span><i></i>{t}</span></label>'
        for k, t, c in TOPICS)
    cap = '''<div class="field"><label for="f-kap">Planowany kapitał</label><select id="f-kap" name="kapital">
          <option value="">Wybierz przedział</option><option>do 100 000 €</option><option>100 000 – 250 000 €</option>
          <option>250 000 – 500 000 €</option><option>powyżej 500 000 €</option><option>Wolę omówić w rozmowie</option></select></div>''' if capital else \
          '''<div class="field"><label for="f-lok">Lokalizacja nieruchomości</label><input id="f-lok" name="lokalizacja" placeholder="np. Marbella, Nueva Andalucía"></div>'''
    return f'''<section class="contact sec" id="kontakt">
  {ribbons("c")}
  <div class="wrap contact-grid">
    <div class="contact-info rv">
      <span class="eyebrow">Kontakt</span>
      <h2 class="h2 split-words">{title}</h2>
      <p class="lead">{lead}</p>
      <div class="contact-lines">
        <div><span>Telefon</span><b>{ph("+48 / +34 — numer do uzupełnienia")}</b></div>
        <div><span>E-mail</span><b>{ph("adres e-mail do uzupełnienia")}</b></div>
        <div><span>Biuro</span><b>Costa del Sol, Hiszpania · {ph("adres")}</b></div>
        <div><span>Odpowiedź</span><b>{ph("np. w ciągu 24 godzin")}</b></div>
      </div>
    </div>
    <form class="form rv" style="--d:.15s" action="#" method="post" novalidate>
      <div class="field full"><label>Czego dotyczy zapytanie?</label><div class="chips">{chips}</div></div>
      <div class="field"><label for="f-imie">Imię i nazwisko</label><input id="f-imie" name="imie" autocomplete="name" required></div>
      <div class="field"><label for="f-tel">Telefon</label><input id="f-tel" name="telefon" type="tel" autocomplete="tel" required></div>
      <div class="field"><label for="f-mail">E-mail</label><input id="f-mail" name="email" type="email" autocomplete="email" required></div>
      {cap}
      <div class="field full"><label for="f-msg">Wiadomość</label><textarea id="f-msg" name="wiadomosc" placeholder="Kilka zdań o Twoich oczekiwaniach, terminie i preferowanej formie kontaktu."></textarea></div>
      <label class="consent full"><input type="checkbox" required><span>Wyrażam zgodę na przetwarzanie moich danych osobowych w celu odpowiedzi na zapytanie. Administratorem danych jest {ph("nazwa spółki")}. Szczegóły w <a href="#" style="text-decoration:underline">polityce prywatności</a>.</span></label>
      <div class="actions full"><small>Pola wymagane: temat, imię, telefon, e-mail.</small><button class="btn btn-primary" type="submit">Wyślij zapytanie {I["arrow"]}</button></div>
      <div class="form-ok"><div class="tick">{I["check"]}</div><h3 class="h3">Dziękujemy za wiadomość</h3><p class="muted">To wersja demonstracyjna — po wdrożeniu formularz będzie trafiał bezpośrednio na skrzynkę Soffel Group.</p></div>
    </form>
  </div>
</section>'''

def siblings(current):
    items = "".join(
        f'<a class="sib rv" style="--c:{d["c"]};--d:{i*.08}s" href="{d["url"]}"><img src="img/{d["img"]}.webp" alt="" width="48" height="48" loading="lazy">'
        f'<div><b>SOFFEL</b><span>{d["name"]}</span></div>{I["arrow-ur"]}</a>'
        for i, d in enumerate([x for x in DIVS if x["key"] != current]))
    return f'''<section class="sec-sm" style="border-top:1px solid var(--line)">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">Pozostałe marki Soffel Group</span></div>
    <div class="siblings">{items}</div>
  </div>
</section>'''

def faq(items, dark=False):
    det = "".join(f'<details class="rv"><summary>{q}<span class="pm" aria-hidden="true"></span></summary><div class="ans"><p>{a}</p></div></details>' for q, a in items)
    return f'<div class="{"dark-faq" if dark else ""}"><div class="faq">{det}</div></div>'

def page(slug, title, desc, div, body, active=None):
    html = head(title, desc, slug) + f'\n<body data-div="{div}">\n{svg_defs()}\n{header(active)}\n<main>\n{body}\n</main>\n{footer()}'
    (ROOT / f"{slug}.html").write_text(html, encoding="utf-8")
    print("✓", slug)

def sub_hero(d, h1_lines, lead, cta_label="Zapytaj o współpracę"):
    lines = "".join(f'<span class="ln"><span>{l}</span></span>' for l in h1_lines)
    return f'''<section class="hero sub">
  {ribbons("h")}
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <nav class="breadcrumbs fade-up" aria-label="Okruszki"><a href="index.html">Soffel Group</a><span>/</span><span>{d["name"]}</span></nav>
      <div class="div-label fade-up"><b>SOFFEL</b><span>{d["name"]}</span></div>
      <h1 class="display">{lines}</h1>
      <p class="lead fade-up d1">{lead}</p>
      <div class="hero-cta fade-up d2">
        <a class="btn btn-primary" href="#kontakt">{cta_label} {I["arrow"]}</a>
        <a class="btn btn-ghost" href="#oferta">Zakres usług</a>
      </div>
      <p class="hero-note fade-up d3">{d["tag"]}</p>
    </div>
    <div class="div-mark" aria-hidden="true"><span class="glow"></span><img src="img/{d["img"]}.webp" alt="" width="240" height="240"></div>
  </div>
</section>'''

def marquee(words):
    seq = "".join(f"<span>{w}</span>" for w in words)
    return f'<div class="marquee" aria-hidden="true"><div class="track">{seq}{seq}</div></div>'

# ================================================================ INDEX
def build_index():
    rows = "".join(f'''<a class="div-row rv" href="{d["url"]}" style="--c:{d["c"]};--d:{i*.08}s">
      <span class="num">{i+1:02d}</span>
      <div class="nm"><img src="img/{d["img"]}.webp" alt="" width="54" height="54" loading="lazy"><h3>Soffel <em>{d["name"]}</em>{f'<span class="tag-flag">{d["flag"]}</span>' if d["flag"] else ""}</h3></div>
      <div class="ds"><b>{d["tag"]}</b>{d["desc"]}</div>
      <span class="go">{I["arrow"]}</span>
    </a>''' for i, d in enumerate(DIVS))

    steps = [
        ("01", "Selekcja i zakup", "Wyszukujemy nieruchomości z potencjałem wzrostu wartości, analizujemy stan techniczny, dokumenty i rynek, a następnie przeprowadzamy zakup.", "prop"),
        ("02", "Projekt i renowacja", "Opracowujemy projekt i budżet, po czym realizujemy remont i wykończenie pod klucz w standardzie oczekiwanym przez kupujących na Costa del Sol.", "reno"),
        ("03", "Home staging i sprzedaż", "Przygotowujemy nieruchomość do prezentacji, wykonujemy sesję zdjęciową i prowadzimy sprzedaż w kanałach lokalnych i międzynarodowych.", "prop"),
        ("04", "Najem do czasu sprzedaży", "Jeżeli sprzedaż wymaga więcej czasu, nieruchomość pracuje na siebie w najmie krótkoterminowym. Obsługę gości i sprzątanie zapewnia grupa.", "clean"),
        ("05", "Wyjście i podział zysku", "Po sprzedaży rozliczamy projekt i wypłacamy zysk zgodnie z umową. Inwestor otrzymuje pełne podsumowanie kosztów i wyniku.", "inv"),
    ]
    steps_html = "".join(f'''<div class="step{" alt" if k=="clean" else ""}" style="--c:{D[k]["c"]}">
        <span class="bul">{n}</span><h3>{t}</h3><p>{p}</p><span class="who"><i></i>Soffel {D[k]["name"]}</span></div>''' for n, t, p, k in steps)

    body = f'''
<section class="hero">
  {ribbons("h")}
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <span class="eyebrow fade-up">Costa del Sol · Marbella · Málaga</span>
      <h1 class="display">
        <span class="ln"><span>Inwestycje w</span></span>
        <span class="ln"><span>nieruchomości</span></span>
        <span class="ln"><span class="gold-text">premium</span></span>
        <span class="ln"><span class="gold-text">w Hiszpanii</span></span>
      </h1>
      <p class="lead fade-up d1">Kupujemy, odnawiamy i sprzedajemy nieruchomości na Costa del Sol z zyskiem dla naszych inwestorów. Cały proces prowadzą cztery marki Soffel Group — bez podwykonawców i bez przekazywania odpowiedzialności.</p>
      <div class="hero-cta fade-up d2">
        <a class="btn btn-primary" href="#kontakt" data-topic="inv">Porozmawiajmy o inwestycji {I["arrow"]}</a>
        <a class="btn btn-ghost" href="#model">Jak działa model flip</a>
      </div>
      <p class="hero-note fade-up d3">Rozmowa bez zobowiązań · {ph("czas odpowiedzi")}</p>
    </div>
    <div class="hero-visual">
      <div class="clip"><img src="img/hero-villa.webp" alt="Nowoczesna willa z basenem na Costa del Sol o zachodzie słońca" width="1125" height="680" fetchpriority="high"></div>
      <svg class="frame" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true"><path d="{HERO_FRAME}"/><path class="f2" d="M97,5 C64,4 18,17 8,50 C1,80 31,95 60,94"/></svg>
      <div class="hero-badge"><img src="img/s-gold.webp" alt="" width="40" height="40"><span><b>Flagowy produkt</b>Flip nieruchomości pod klucz</span></div>
    </div>
  </div>
  <div class="hero-stats">
    <div class="wrap">
      <div class="st"><strong>{ph("+XX M€")}</strong><span>Wartość projektów</span></div>
      <div class="st"><p class="locs">Marbella · Málaga · Estepona</p><span>Costa del Sol</span></div>
      <div class="st"><strong><span data-count="4">4</span> obszary</strong><span>Jeden proces</span></div>
    </div>
  </div>
  <span class="scroll-cue">Przewiń</span>
</section>

{marquee(LOCS)}

<section class="sec" id="spolki">
  <div class="wrap">
    <div class="sec-head split">
      <div style="display:grid;gap:22px"><span class="eyebrow">Obszary działania</span><h2 class="h2 split-words">Cztery obszary.<br><span class="gold-text">Jeden standard.</span></h2></div>
      <p class="lead rv">Soffel Group obejmuje cały cykl życia nieruchomości — od zakupu, przez renowację, sprzedaż i najem, po codzienną opiekę. Każdy etap prowadzi wyspecjalizowana marka grupy, dzięki czemu inwestor ma jednego partnera i jedną odpowiedzialność.</p>
    </div>
    <div class="divs">{rows}</div>
  </div>
</section>

<section class="paper sec" id="model">
  <div class="wrap">
    <div class="sec-head split">
      <div style="display:grid;gap:22px"><span class="eyebrow">Soffel Investments · model flip</span><h2 class="h2 split-words">Od zakupu do zysku w pięciu etapach</h2></div>
      <p class="lead rv">Inwestor wnosi kapitał, a Soffel Group prowadzi projekt od pierwszej analizy do sprzedaży. Na każdym etapie wiadomo, która marka grupy odpowiada za wynik.</p>
    </div>
    <div class="model"><span class="bar"></span>{steps_html}</div>
    <div class="loop-note rv">
      {I["loop"]}
      <p><b>Nieruchomość nie stoi pusta.</b> Do momentu sprzedaży apartament lub willa jest wynajmowana krótkoterminowo, a przychód z najmu pracuje na wynik inwestycji. Zarządzanie najmem i sprzątanie zapewniają Soffel Properties i Soffel Cleaning.</p>
      <a class="btn btn-ghost" href="inwestycje.html" style="color:var(--text);border-color:var(--line-strong)">Szczegóły modelu {I["arrow"]}</a>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head center">
      <span class="eyebrow center">Formy udziału</span>
      <h2 class="h2 split-words">Inwestuj sam lub <span class="gold-text">w grupie</span></h2>
      <p class="lead rv">Projekt może sfinansować jeden inwestor albo kilku współinwestorów. Dla większych przedsięwzięć planujemy strukturę funduszu inwestycyjnego.</p>
    </div>
    <div class="cards" data-stagger>
      <article class="card">
        <span class="ic">{I["user1"]}</span><span class="k">Opcja 01</span><h3>Inwestor indywidualny</h3>
        <p>Jeden inwestor finansuje cały projekt i otrzymuje pełny udział w zysku po rozliczeniu kosztów i wynagrodzenia grupy.</p>
        <div class="feat"><span>Próg wejścia</span><strong>{ph()}</strong><span>Forma prawna</span><strong>{ph()}</strong></div>
      </article>
      <article class="card hl">
        <span class="badge">Niższy próg wejścia</span>
        <span class="ic">{I["users"]}</span><span class="k">Opcja 02</span><h3>Klub współinwestorów</h3>
        <p>Kilku inwestorów wspólnie finansuje jedną nieruchomość. Zysk dzielony jest proporcjonalnie do wniesionego kapitału.</p>
        <div class="feat"><span>Próg wejścia</span><strong>{ph()}</strong><span>Forma prawna</span><strong>{ph()}</strong></div>
      </article>
      <article class="card">
        <span class="ic">{I["bank"]}</span><span class="k">Opcja 03</span><h3>Fundusz inwestycyjny</h3>
        <p>Udział w portfelu kilku projektów jednocześnie, z rozłożeniem ryzyka na więcej niż jedną nieruchomość.</p>
        <div class="feat"><span>Status</span><strong>{ph("w przygotowaniu / dostępny")}</strong><span>Próg wejścia</span><strong>{ph()}</strong></div>
      </article>
    </div>
  </div>
</section>

<section class="sec tint">
  <div class="wrap">
    <div class="sec-head split">
      <div style="display:grid;gap:22px"><span class="eyebrow">Przykładowy projekt</span><h2 class="h2 split-words">Liczby, które pokazujemy inwestorom</h2></div>
      <p class="lead rv">Każdy projekt otrzymuje kartę z ceną zakupu, budżetem renowacji, przychodem z najmu i wynikiem ze sprzedaży. Poniżej miejsce na pierwszy zrealizowany case study.</p>
    </div>
    <article class="case rv">
      <div class="media">{ph_img("Projekt — zdjęcie przed i po renowacji", "np. apartament w Marbelli")}</div>
      <div class="body">
        <span class="eyebrow">{ph("Lokalizacja")} · {ph("typ nieruchomości")}</span>
        <h3 class="h3">{ph("Nazwa projektu")}</h3>
        <dl>
          <div><dt>Cena zakupu</dt><dd>{ph("— €")}</dd></div>
          <div><dt>Budżet renowacji</dt><dd>{ph("— €")}</dd></div>
          <div><dt>Czas projektu</dt><dd>{ph("— mies.")}</dd></div>
          <div><dt>Przychód z najmu</dt><dd>{ph("— €")}</dd></div>
          <div><dt>Cena sprzedaży</dt><dd>{ph("— €")}</dd></div>
          <div><dt>Zwrot dla inwestora</dt><dd class="gold-text">{ph("— %")}</dd></div>
        </dl>
        <a class="link-arrow" href="#kontakt" data-topic="inv">Zapytaj o aktualne projekty {I["arrow"]}</a>
      </div>
    </article>
  </div>
</section>

<section class="sec">
  <div class="wrap split">
    <div class="stack-media rv">
      <div class="media rv-img parallax">{photo("salon-1")}<span class="cap">Soffel Renovations</span></div>
      <div class="media b rv-img">{photo("lazienka-wanna", sizes="30vw")}</div>
    </div>
    <div class="copy">
      <span class="eyebrow" style="--acc:#a76cff">Standard wykończenia</span>
      <h2 class="h2 split-words">Wartość budujemy <span class="gold-text">w detalach</span></h2>
      <p class="lead rv">Renowację prowadzi własna marka grupy — Soffel Renovations. Projektujemy wnętrza z myślą o kupujących segmentu premium: naturalne materiały, oświetlenie liniowe, zabudowy na wymiar i łazienki w standardzie hotelowym.</p>
      <ul class="ticks rv" style="display:grid;gap:12px;color:var(--muted)">
        <li>Projekt wnętrza i kosztorys przed rozpoczęciem prac</li>
        <li>Własne ekipy wykończeniowe i stały nadzór</li>
        <li>Dokumentacja zdjęciowa każdego etapu dla inwestora</li>
      </ul>
      <div><a class="link-arrow" href="renowacje.html" style="--acc:#a76cff">Zobacz realizacje {I["arrow"]}</a></div>
    </div>
  </div>
  <div class="wrap" style="margin-top:clamp(50px,7vw,90px)">
    <div class="hscroll" data-lb>
      {"".join(f'<figure>{photo(n, sizes="360px")}</figure>' for n in ["kuchnia-wyspa","sypialnia-lustro","lazienka-kamien","korytarz-polki","lazienka-prysznic","kuchnia-salon","antresola","sypialnia-2"])}
    </div>
  </div>
</section>

<section class="paper sec">
  <div class="wrap">
    <div class="sec-head split">
      <div style="display:grid;gap:22px"><span class="eyebrow">Dlaczego Costa del Sol</span><h2 class="h2 split-words">Rynek, który przyciąga kupujących z całej Europy</h2></div>
      <p class="lead rv">Costa del Sol łączy klimat, infrastrukturę i stały popyt międzynarodowy. To otoczenie sprzyja zarówno sprzedaży odnowionych nieruchomości, jak i najmowi krótkoterminowemu.</p>
    </div>
    <div class="cards c4" data-stagger>
      <article class="card"><span class="ic">{I["sun"]}</span><h3>Klimat przez cały rok</h3><p>Region słynie z łagodnych zim i długiego sezonu, co przekłada się na popyt na najem także poza latem.</p></article>
      <article class="card"><span class="ic">{I["plane"]}</span><h3>Bliskość Polski</h3><p>Lotnisko w Maladze ma bezpośrednie połączenia z wieloma miastami w Polsce, a lot trwa kilka godzin.</p></article>
      <article class="card"><span class="ic">{I["users"]}</span><h3>Międzynarodowi kupujący</h3><p>Nieruchomości kupują tu klienci z całej Europy, co poszerza grono nabywców odnowionych lokali.</p></article>
      <article class="card"><span class="ic">{I["chart"]}</span><h3>Segment premium</h3><p>Marbella i okolice to jeden z najbardziej rozpoznawalnych rynków nieruchomości luksusowych w Hiszpanii.</p></article>
    </div>
    <p class="muted rv" style="margin-top:30px;font-size:14px">Miejsce na aktualne dane rynkowe od klienta: {ph("średnia cena m² w Marbelli")}, {ph("dynamika cen r/r")}, {ph("obłożenie najmu")}.</p>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head split">
      <div style="display:grid;gap:22px"><span class="eyebrow">Zespół</span><h2 class="h2 split-words">Ludzie stojący za <span class="gold-text">Soffel Group</span></h2></div>
      <div class="rv" style="display:grid;gap:22px;justify-items:start"><p class="lead">Każdą markę grupy prowadzi osoba odpowiedzialna za swój obszar — od inwestycji, przez sprzedaż, po wykonawstwo i opiekę nad nieruchomościami.</p><a class="link-arrow" href="o-nas.html">Poznaj zespół {I["arrow"]}</a></div>
    </div>
    <div class="team" data-stagger>
      {"".join(f'<div class="member" style="--c:{d["c"]}">{ph_img("Portret", "Soffel " + d["name"])}<span class="role">Soffel {d["name"]}</span><h3>{ph("Imię i nazwisko")}</h3><p>{ph("Stanowisko")}</p></div>' for d in DIVS)}
    </div>
  </div>
</section>

<section class="paper sec">
  <div class="wrap">
    <div class="sec-head center"><span class="eyebrow center">Pytania inwestorów</span><h2 class="h2 split-words">Najczęściej zadawane pytania</h2></div>
    {faq([
      ("Co się dzieje, jeśli nieruchomość nie sprzeda się od razu?", "Do momentu sprzedaży nieruchomość jest wynajmowana krótkoterminowo. Najmem, obsługą gości i sprzątaniem zajmują się marki grupy, a przychód z najmu jest uwzględniany w rozliczeniu projektu."),
      ("Czy muszę przyjeżdżać do Hiszpanii?", "Nie. Zakup, renowację, sprzedaż i najem prowadzi Soffel Group na miejscu. Inwestor otrzymuje raporty i dokumentację zdjęciową, a wizyta na miejscu jest możliwa, ale nie jest wymagana."),
      ("Ile trwa jeden projekt?", f"Czas projektu zależy od zakresu renowacji i sytuacji rynkowej. Typowy horyzont: {ph('do uzupełnienia, np. 6–12 miesięcy')}."),
      ("Jaki jest minimalny wkład?", f"Próg wejścia zależy od formy udziału. Dla inwestora indywidualnego: {ph()}, dla klubu współinwestorów: {ph()}."),
      ("Jak zabezpieczony jest kapitał inwestora?", f"Struktura prawna, sposób zabezpieczenia i zasady podziału zysku są opisane w umowie inwestycyjnej. {ph('Opis zabezpieczeń do uzupełnienia przez klienta')}"),
      ("Jak raportujecie postępy?", f"Inwestor otrzymuje regularne podsumowania postępu prac, kosztów i działań sprzedażowych. {ph('Częstotliwość i forma raportów do uzupełnienia')}"),
    ])}
  </div>
</section>

{contact("inv")}
'''
    page("index", "Soffel Group — inwestycje w nieruchomości na Costa del Sol | Marbella, Málaga",
         "Soffel Group: flip nieruchomości na Costa del Sol dla polskich inwestorów. Zakup, renowacja, sprzedaż, najem i sprzątanie — cztery obszary, jeden proces.",
         "group", body)

# ================================================================ INWESTYCJE
def build_inv():
    d = D["inv"]
    proc = [
        ("Rozmowa i profil inwestora", "Poznajemy oczekiwania co do kapitału, horyzontu czasowego i poziomu ryzyka. Przedstawiamy model współpracy i dokumenty."),
        ("Wybór nieruchomości", "Przedstawiamy wyselekcjonowane nieruchomości wraz z analizą: cena zakupu, szacowany budżet renowacji, wartość po remoncie i scenariusze sprzedaży."),
        ("Umowa i zakup", "Podpisujemy umowę inwestycyjną, a następnie przeprowadzamy zakup u notariusza w Hiszpanii wraz z kompletem formalności."),
        ("Renowacja", "Soffel Renovations realizuje projekt zgodnie z budżetem i harmonogramem. Inwestor otrzymuje dokumentację zdjęciową postępu prac."),
        ("Sprzedaż lub najem", "Soffel Properties prowadzi sprzedaż. Do momentu jej finalizacji nieruchomość jest wynajmowana krótkoterminowo."),
        ("Rozliczenie", "Po sprzedaży przedstawiamy pełne rozliczenie projektu i wypłacamy zysk zgodnie z warunkami umowy."),
    ]
    body = f'''
{sub_hero(d, ["Flip", '<span class="acc-text">nieruchomości</span>', "na Costa del Sol"], "Inwestujesz kapitał, my prowadzimy projekt: zakup, renowację, najem i sprzedaż. Zysk ze wzrostu wartości nieruchomości trafia do inwestorów po rozliczeniu projektu.", "Porozmawiajmy o inwestycji")}

{marquee(["Acquire", "Renovate", "Rent", "Sell", "Return"])}

<section class="sec" id="oferta">
  <div class="wrap">
    <div class="sec-head split">
      <div style="display:grid;gap:22px"><span class="eyebrow">Na czym polega flip</span><h2 class="h2 split-words">Kupujemy poniżej potencjału. <span class="acc-text">Sprzedajemy po renowacji.</span></h2></div>
      <p class="lead rv">Szukamy nieruchomości, których wartość można wyraźnie podnieść remontem i przemyślaną aranżacją. Zysk powstaje z różnicy między łącznym kosztem projektu a ceną sprzedaży odnowionej nieruchomości.</p>
    </div>
    <div class="facts" data-stagger>
      <div class="fact"><strong>{ph("— %")}</strong><span>Średni zwrot z projektu</span></div>
      <div class="fact"><strong>{ph("— mies.")}</strong><span>Typowy czas trwania</span></div>
      <div class="fact"><strong>{ph("—")}</strong><span>Zrealizowane projekty</span></div>
      <div class="fact"><strong><span data-count="4">4</span></strong><span>Obszary zaangażowane w projekt</span></div>
    </div>
  </div>
</section>

<section class="paper sec" id="model">
  <div class="wrap">
    <div class="sec-head split">
      <div style="display:grid;gap:22px"><span class="eyebrow">Przebieg współpracy</span><h2 class="h2 split-words">Sześć kroków od rozmowy do wypłaty zysku</h2></div>
      <p class="lead rv">Każdy etap ma właściciela w strukturze grupy, a inwestor zna jego zakres, koszt i termin.</p>
    </div>
    <ol class="proc">{"".join(f'<li class="rv"><h3>{t}</h3><p>{p}</p></li>' for t, p in proc)}</ol>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head center">
      <span class="eyebrow center">Formy udziału</span>
      <h2 class="h2 split-words">Wybierz model, który pasuje <span class="acc-text">do Twojego kapitału</span></h2>
    </div>
    <div class="cards" data-stagger>
      <article class="card"><span class="ic">{I["user1"]}</span><span class="k">Indywidualnie</span><h3>Jeden inwestor, jedna nieruchomość</h3><ul class="ticks"><li>Pełny udział w zysku projektu</li><li>Wpływ na wybór nieruchomości</li><li>Indywidualne raporty</li></ul><div class="feat"><span>Próg wejścia</span><strong>{ph()}</strong></div></article>
      <article class="card hl"><span class="badge">Elastyczny próg</span><span class="ic">{I["users"]}</span><span class="k">Współinwestycja</span><h3>Kilku inwestorów, jeden projekt</h3><ul class="ticks"><li>Niższy próg wejścia</li><li>Zysk proporcjonalny do wkładu</li><li>Wspólne raportowanie</li></ul><div class="feat"><span>Próg wejścia</span><strong>{ph()}</strong></div></article>
      <article class="card"><span class="ic">{I["bank"]}</span><span class="k">Fundusz</span><h3>Portfel kilku nieruchomości</h3><ul class="ticks"><li>Rozłożenie ryzyka</li><li>Kilka projektów jednocześnie</li><li>Struktura dla większego kapitału</li></ul><div class="feat"><span>Status</span><strong>{ph("w przygotowaniu")}</strong></div></article>
    </div>
  </div>
</section>

<section class="sec tint">
  <div class="wrap split">
    <div class="media wide rv-img">{ph_img("Willa lub apartament z portfela inwestycyjnego", "najlepiej zdjęcie przed / po")}</div>
    <div class="copy">
      <span class="eyebrow">Przejrzystość</span>
      <h2 class="h2 split-words">Inwestor wie, co dzieje się z kapitałem</h2>
      <div class="cards c2" style="gap:16px" data-stagger>
        <div class="card" style="padding:24px"><span class="ic">{I["doc"]}</span><h3 style="font-size:1.1rem">Umowa inwestycyjna</h3><p>{ph("Forma prawna i zabezpieczenia")}</p></div>
        <div class="card" style="padding:24px"><span class="ic">{I["eye"]}</span><h3 style="font-size:1.1rem">Raporty i zdjęcia</h3><p>Dokumentacja postępu prac na każdym etapie.</p></div>
        <div class="card" style="padding:24px"><span class="ic">{I["shield"]}</span><h3 style="font-size:1.1rem">Własność nieruchomości</h3><p>{ph("Na kogo zapisana jest nieruchomość")}</p></div>
        <div class="card" style="padding:24px"><span class="ic">{I["chart"]}</span><h3 style="font-size:1.1rem">Rozliczenie projektu</h3><p>Pełne zestawienie kosztów, przychodów i zysku.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="sec dark-faq">
  <div class="wrap">
    <div class="sec-head center"><span class="eyebrow center">FAQ</span><h2 class="h2 split-words">Pytania przed pierwszą inwestycją</h2></div>
    {faq([
      ("Czy inwestycja wiąże się z ryzykiem?", "Tak — jak każda inwestycja w nieruchomości. Ryzyko dotyczy m.in. czasu sprzedaży, kosztów renowacji i zmian cen na rynku. Ograniczamy je analizą przed zakupem, własnym wykonawstwem i najmem krótkoterminowym do czasu sprzedaży."),
      ("Czy mogę wybrać konkretną nieruchomość?", "Inwestor indywidualny ma wpływ na wybór nieruchomości. W modelu współinwestycji decyzję podejmujemy na podstawie analizy przedstawionej wszystkim uczestnikom projektu."),
      ("Jak opodatkowany jest zysk?", f"Kwestie podatkowe zależą od struktury inwestycji i rezydencji podatkowej inwestora. {ph('Opis do uzupełnienia — najlepiej we współpracy z doradcą podatkowym klienta')}"),
      ("Kiedy otrzymam zysk?", f"Zysk wypłacamy po sprzedaży nieruchomości i rozliczeniu projektu. {ph('Termin wypłaty od sprzedaży')}"),
    ], dark=True)}
  </div>
</section>

{contact("inv")}
{siblings("inv")}
'''
    page("inwestycje", "Soffel Investments — flip nieruchomości na Costa del Sol | Soffel Group",
         "Inwestycje we flipy nieruchomości w Marbelli i Maladze: zakup, renowacja, najem i sprzedaż z zyskiem. Dla jednego inwestora lub grupy współinwestorów.",
         "inv", body, "inv")

# ================================================================ NIERUCHOMOŚCI
def build_prop():
    d = D["prop"]
    listings = "".join(f'''<article class="listing">
        {ph_img("Zdjęcie oferty", "")}
        <div class="in"><span class="loc">{loc}</span><h3>{ph(t)}</h3><span class="price">{ph("— €")}</span>
        <div class="meta"><span>{ph("— m²")}</span><span>{ph("— sypialnie")}</span><span>{ph("— łazienki")}</span></div></div>
      </article>''' for loc, t in [("Marbella", "Willa z basenem"), ("Málaga", "Apartament z widokiem na morze"), ("Estepona", "Penthouse z tarasem")])
    body = f'''
{sub_hero(d, ["Kupno,", "sprzedaż", '<span class="acc-text">i zarządzanie</span>'], "Soffel Properties to agencja nieruchomości grupy. Pomagamy kupić i sprzedać nieruchomość na Costa del Sol, a po transakcji zajmujemy się jej najmem i bieżącą obsługą.", "Zapytaj o nieruchomość")}

{marquee(LOCS)}

<section class="sec" id="oferta">
  <div class="wrap">
    <div class="sec-head split">
      <div style="display:grid;gap:22px"><span class="eyebrow">Zakres usług</span><h2 class="h2 split-words">Agencja, która zna rynek <span class="acc-text">od środka</span></h2></div>
      <p class="lead rv">Jako część grupy, która sama inwestuje i remontuje, oceniamy nieruchomości nie tylko po cenie, ale też po stanie technicznym i potencjale wzrostu wartości.</p>
    </div>
    <div class="cards" data-stagger>
      <article class="card"><span class="ic">{I["search"]}</span><span class="k">01</span><h3>Zakup nieruchomości</h3><p>Wyszukiwanie ofert według Twoich kryteriów, oględziny, weryfikacja dokumentów i wsparcie przy negocjacjach oraz u notariusza.</p></article>
      <article class="card"><span class="ic">{I["key"]}</span><span class="k">02</span><h3>Sprzedaż nieruchomości</h3><p>Wycena, przygotowanie do sprzedaży, profesjonalne zdjęcia i promocja wśród kupujących lokalnych i zagranicznych.</p></article>
      <article class="card"><span class="ic">{I["calendar"]}</span><span class="k">03</span><h3>Zarządzanie najmem</h3><p>Obsługa najmu krótkoterminowego: ogłoszenia, kontakt z gośćmi, zameldowania, sprzątanie i rozliczenia z właścicielem.</p></article>
    </div>
  </div>
</section>

<section class="paper sec">
  <div class="wrap">
    <div class="sec-head split">
      <div style="display:grid;gap:22px"><span class="eyebrow">Zakup w Hiszpanii krok po kroku</span><h2 class="h2 split-words">Prowadzimy przez formalności</h2></div>
      <p class="lead rv">Zakup nieruchomości w Hiszpanii przez obcokrajowca wymaga kilku formalności. Zajmujemy się nimi razem z naszymi partnerami prawnymi.</p>
    </div>
    <ol class="proc">
      <li class="rv"><h3>Numer NIE</h3><p>Numer identyfikacyjny cudzoziemca, wymagany przy zakupie nieruchomości i otwarciu konta.</p></li>
      <li class="rv"><h3>Konto w hiszpańskim banku</h3><p>Rachunek do rozliczenia transakcji oraz późniejszych opłat związanych z nieruchomością.</p></li>
      <li class="rv"><h3>Rezerwacja i umowa przedwstępna</h3><p>Zabezpieczenie wybranej nieruchomości oraz ustalenie warunków i terminu transakcji.</p></li>
      <li class="rv"><h3>Akt notarialny i rejestracja</h3><p>Podpisanie aktu u notariusza i wpis do rejestru nieruchomości.</p></li>
    </ol>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head split">
      <div style="display:grid;gap:22px"><span class="eyebrow">Wybrane oferty</span><h2 class="h2 split-words">Nieruchomości w ofercie</h2></div>
      <p class="lead rv">Miejsce na aktualne oferty Soffel Properties. Po wdrożeniu oferty można podpiąć z CRM lub portalu nieruchomości.</p>
    </div>
    <div class="cards" data-stagger>{listings}</div>
  </div>
</section>

<section class="sec tint">
  <div class="wrap split">
    <div class="media rv-img">{ph_img("Apartament w najmie krótkoterminowym", "zdjęcie wnętrza przygotowanego dla gości")}</div>
    <div class="copy">
      <span class="eyebrow">Dla właścicieli</span>
      <h2 class="h2 split-words">Nieruchomość, która <span class="acc-text">zarabia</span> pod Twoją nieobecność</h2>
      <p class="lead rv">Przejmujemy obsługę najmu krótkoterminowego od A do Z, a sprzątanie i przygotowanie apartamentu realizuje Soffel Cleaning. Ty otrzymujesz miesięczne rozliczenie.</p>
      <ul class="ticks rv" style="display:grid;gap:12px;color:var(--muted)"><li>Ogłoszenia i polityka cenowa</li><li>Kontakt z gośćmi i zameldowania</li><li>Sprzątanie, pościel i drobne naprawy</li><li>Rozliczenie miesięczne {ph("model wynagrodzenia")}</li></ul>
    </div>
  </div>
</section>

{contact("prop", 'Szukasz <span class="acc-text">nieruchomości?</span>', "Napisz, czego szukasz lub co chcesz sprzedać. Przygotujemy propozycje ofert albo wycenę nieruchomości.", capital=False)}
{siblings("prop")}
'''
    page("nieruchomosci", "Soffel Properties — nieruchomości na Costa del Sol: kupno, sprzedaż, najem | Soffel Group",
         "Agencja nieruchomości Soffel Properties: zakup i sprzedaż nieruchomości w Marbelli, Maladze i na Costa del Sol oraz zarządzanie najmem krótkoterminowym.",
         "prop", body, "prop")

# ================================================================ RENOWACJE
def build_reno():
    d = D["reno"]
    gal = [("salon-1", "w"), ("lazienka-wanna", "t"), ("kuchnia-wyspa", ""), ("sypialnia-lustro", ""), ("lazienka-kamien", "t"),
           ("korytarz-polki", ""), ("kuchnia-salon", "w"), ("lazienka-prysznic", ""), ("antresola", ""), ("sypialnia-2", "t"),
           ("lazienka-3", ""), ("korytarz", ""), ("lazienka-4", ""), ("salon-2", "w")]
    gal_html = "".join(f'<figure class="{c}">{photo(n, sizes="(max-width:900px) 50vw, 33vw")}<figcaption>{PHOTOS[n]}</figcaption></figure>' for n, c in gal)
    body = f'''
{sub_hero(d, ["Projekt,", "remont", '<span class="acc-text">i wykończenie</span>'], "Soffel Renovations odnawia apartamenty i wille na Costa del Sol — zarówno dla projektów inwestycyjnych grupy, jak i dla właścicieli, którzy chcą podnieść standard swojej nieruchomości.", "Zapytaj o wycenę")}

{marquee(["Build", "Transform", "Improve", "Build", "Transform", "Improve"])}

<section class="sec" id="oferta">
  <div class="wrap">
    <div class="sec-head split">
      <div style="display:grid;gap:22px"><span class="eyebrow">Zakres prac</span><h2 class="h2 split-words">Jeden wykonawca <span class="acc-text">od projektu do odbioru</span></h2></div>
      <p class="lead rv">Prowadzimy prace kompleksowo, z jednym kosztorysem i jednym harmonogramem. Dzięki temu właściciel lub inwestor nie musi koordynować kilku firm.</p>
    </div>
    <div class="cards c4" data-stagger>
      <article class="card"><span class="ic">{I["ruler"]}</span><span class="k">01</span><h3>Projekt wnętrza</h3><p>Układ funkcjonalny, dobór materiałów, oświetlenia i zabudów oraz wizualizacje przed rozpoczęciem prac.</p></article>
      <article class="card"><span class="ic">{I["tool"]}</span><span class="k">02</span><h3>Remont generalny</h3><p>Instalacje, ściany działowe, sufity podwieszane i przygotowanie nieruchomości do wykończenia.</p></article>
      <article class="card"><span class="ic">{I["brush"]}</span><span class="k">03</span><h3>Wykończenie pod klucz</h3><p>Podłogi, łazienki, kuchnie, zabudowy na wymiar i oświetlenie — gotowe do zamieszkania lub sprzedaży.</p></article>
      <article class="card"><span class="ic">{I["home"]}</span><span class="k">04</span><h3>Home staging</h3><p>Aranżacja i wyposażenie, które przygotowują nieruchomość do sesji zdjęciowej i prezentacji kupującym.</p></article>
    </div>
  </div>
</section>

<section class="sec tint">
  <div class="wrap">
    <div class="sec-head split">
      <div style="display:grid;gap:22px"><span class="eyebrow">Realizacje</span><h2 class="h2 split-words">Wnętrza po <span class="acc-text">naszej renowacji</span></h2></div>
      <p class="lead rv">Wybrane realizacje zespołu Soffel Renovations. Kliknij zdjęcie, aby je powiększyć.</p>
    </div>
    <div class="gallery" data-lb>{gal_html}</div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head split">
      <div style="display:grid;gap:22px"><span class="eyebrow">Za kulisami</span><h2 class="h2 split-words">To, czego nie widać po odbiorze</h2></div>
      <p class="lead rv">Jakość wykończenia zaczyna się od etapu, który później znika za płytą i tynkiem: konstrukcji sufitów, instalacji i wentylacji.</p>
    </div>
    <div class="cards" data-lb data-stagger>
      {"".join(f'<figure class="media rv-img" style="aspect-ratio:3/4;border-radius:var(--radius);overflow:hidden;position:relative;cursor:zoom-in">{photo(n, sizes="(max-width:900px) 100vw, 33vw")}<span class="cap">{PHOTOS[n].replace("Etap prac: ","")}</span></figure>' for n in ["budowa-sufit","budowa-2","budowa-3"])}
    </div>
  </div>
</section>

<section class="paper sec">
  <div class="wrap">
    <div class="sec-head split">
      <div style="display:grid;gap:22px"><span class="eyebrow">Proces</span><h2 class="h2 split-words">Jak pracujemy</h2></div>
      <p class="lead rv">Stały proces pozwala dotrzymać budżetu i terminu, niezależnie od skali prac.</p>
    </div>
    <ol class="proc">
      <li class="rv"><h3>Oględziny i zakres</h3><p>Ocena stanu technicznego nieruchomości i ustalenie oczekiwań właściciela lub inwestora.</p></li>
      <li class="rv"><h3>Projekt i kosztorys</h3><p>Projekt wnętrza, dobór materiałów oraz szczegółowy kosztorys i harmonogram prac.</p></li>
      <li class="rv"><h3>Realizacja</h3><p>Prace prowadzone przez nasze ekipy pod stałym nadzorem, z dokumentacją zdjęciową postępu.</p></li>
      <li class="rv"><h3>Odbiór i sprzątanie</h3><p>Odbiór końcowy, sprzątanie poremontowe przez Soffel Cleaning i przekazanie nieruchomości.</p></li>
    </ol>
  </div>
</section>

{contact("reno", 'Zaplanujmy <span class="acc-text">renowację</span>', "Opisz nieruchomość i zakres prac. Umówimy oględziny i przygotujemy wstępny kosztorys.", capital=False)}
{siblings("reno")}
'''
    page("renowacje", "Soffel Renovations — remonty i wykończenia pod klucz na Costa del Sol | Soffel Group",
         "Soffel Renovations: projekt wnętrz, remont generalny i wykończenie pod klucz apartamentów i willi w Marbelli, Maladze i na Costa del Sol.",
         "reno", body, "reno")

# ================================================================ SPRZĄTANIE
def build_clean():
    d = D["clean"]
    body = f'''
{sub_hero(d, ["Czyste", '<span class="acc-text">i gotowe</span>', "na gości"], "Soffel Cleaning dba o nieruchomości w najmie krótkoterminowym i o domy właścicieli, którzy przebywają poza Hiszpanią. Sprzątamy, przygotowujemy apartamenty na przyjazd i pilnujemy ich stanu.", "Zapytaj o wycenę")}

{marquee(["Cleaner", "Brighter", "Spaces", "Cleaner", "Brighter", "Spaces"])}

<section class="sec" id="oferta">
  <div class="wrap">
    <div class="sec-head split">
      <div style="display:grid;gap:22px"><span class="eyebrow">Usługi</span><h2 class="h2 split-words">Standard hotelowy <span class="acc-text">w każdym apartamencie</span></h2></div>
      <p class="lead rv">Pracujemy według list kontrolnych, dzięki czemu każdy apartament jest przygotowany w ten sam sposób — niezależnie od tego, kto go sprząta.</p>
    </div>
    <div class="cards" data-stagger>
      <article class="card"><span class="ic">{I["sparkle"]}</span><span class="k">01</span><h3>Sprzątanie po najemcach</h3><p>Kompleksowe sprzątanie między pobytami gości, wymiana pościeli i ręczników, uzupełnienie podstawowych środków.</p></article>
      <article class="card"><span class="ic">{I["bed"]}</span><span class="k">02</span><h3>Przygotowanie na przyjazd</h3><p>Kontrola wyposażenia, przygotowanie łóżek i zestawów powitalnych oraz zdjęcia stanu apartamentu dla właściciela.</p></article>
      <article class="card"><span class="ic">{I["home"]}</span><span class="k">03</span><h3>Opieka nad nieruchomością</h3><p>Regularne wizyty pod nieobecność właściciela, wietrzenie, kontrola instalacji i zgłaszanie usterek.</p></article>
      <article class="card"><span class="ic">{I["tool"]}</span><span class="k">04</span><h3>Sprzątanie po remoncie</h3><p>Usuwanie pyłu i zabrudzeń budowlanych po zakończeniu prac, przygotowanie nieruchomości do sesji zdjęciowej.</p></article>
      <article class="card"><span class="ic">{I["calendar"]}</span><span class="k">05</span><h3>Sprzątanie regularne</h3><p>Stałe sprzątanie domów i apartamentów według ustalonego harmonogramu.</p></article>
      <article class="card"><span class="ic">{I["key"]}</span><span class="k">06</span><h3>Pranie i pościel</h3><p>{ph("Do potwierdzenia: obsługa pralni i wymiany tekstyliów")}</p></article>
    </div>
  </div>
</section>

<section class="sec tint">
  <div class="wrap split rev">
    <div class="media rv-img">{ph_img("Ekipa Soffel Cleaning przy pracy", "lub apartament przygotowany dla gości")}</div>
    <div class="copy">
      <span class="eyebrow">Dla właścicieli i zarządców</span>
      <h2 class="h2 split-words">Zdjęcie stanu po <span class="acc-text">każdym sprzątaniu</span></h2>
      <p class="lead rv">Po każdej wizycie właściciel otrzymuje potwierdzenie i zdjęcia apartamentu. Usterki lub braki w wyposażeniu zgłaszamy od razu, a drobne naprawy może przejąć Soffel Renovations.</p>
      <div class="facts" style="grid-template-columns:1fr 1fr" data-stagger>
        <div class="fact"><strong>{ph("—")}</strong><span>Obsługiwanych apartamentów</span></div>
        <div class="fact"><strong>{ph("— h")}</strong><span>Czas przygotowania między pobytami</span></div>
      </div>
    </div>
  </div>
</section>

<section class="sec dark-faq">
  <div class="wrap">
    <div class="sec-head center"><span class="eyebrow center">FAQ</span><h2 class="h2 split-words">Pytania o sprzątanie</h2></div>
    {faq([
      ("Na jakim obszarze działacie?", f"Obsługujemy nieruchomości na Costa del Sol, w okolicach Marbelli i Malagi. {ph('Dokładny obszar do uzupełnienia')}"),
      ("Czy mogę zamówić jednorazowe sprzątanie?", "Tak. Oprócz stałej obsługi najmu realizujemy także jednorazowe zlecenia, np. sprzątanie po remoncie lub przed sprzedażą."),
      ("Ile kosztuje sprzątanie apartamentu?", f"Cena zależy od metrażu, liczby sypialni i zakresu usług. {ph('Cennik lub stawka orientacyjna')}"),
    ], dark=True)}
  </div>
</section>

{contact("clean", 'Zamów <span class="acc-text">sprzątanie</span>', "Napisz, gdzie znajduje się nieruchomość i jakiej usługi potrzebujesz. Odezwiemy się z terminem i wyceną.", capital=False)}
{siblings("clean")}
'''
    page("sprzatanie", "Soffel Cleaning — sprzątanie apartamentów i najmu krótkoterminowego na Costa del Sol | Soffel Group",
         "Soffel Cleaning: sprzątanie po najemcach, przygotowanie apartamentów na przyjazd gości, sprzątanie po remoncie i opieka nad nieruchomością w Marbelli i Maladze.",
         "clean", body, "clean")

# ================================================================ O NAS
def build_about():
    team = [("inv", "Inwestycje"), ("prop", "Sprzedaż i najem"), ("reno", "Kierownik robót"), ("clean", "Koordynacja sprzątania"),
            ("inv", "Relacje z inwestorami"), ("prop", "Doradca klienta"), ("reno", "Projektant wnętrz"), ("clean", "Opieka nad nieruchomościami")]
    team_html = "".join(f'<div class="member" style="--c:{D[k]["c"]}">{ph_img("Portret", "zdjęcie członka zespołu")}<span class="role">Soffel {D[k]["name"]} · {r}</span><h3>{ph("Imię i nazwisko")}</h3><p>{ph("Krótki opis doświadczenia, 1–2 zdania")}</p></div>' for k, r in team)
    body = f'''
<section class="hero sub">
  {ribbons("h")}
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <nav class="breadcrumbs fade-up" aria-label="Okruszki"><a href="index.html">Soffel Group</a><span>/</span><span>O nas</span></nav>
      <span class="eyebrow fade-up">People | Property | Better Living</span>
      <h1 class="display"><span class="ln"><span>Ludzie,</span></span><span class="ln"><span>nieruchomości</span></span><span class="ln"><span class="gold-text">i lepsze życie</span></span></h1>
      <p class="lead fade-up d1">Soffel Group to cztery marki, które razem obejmują cały cykl życia nieruchomości na Costa del Sol. Łączymy polskie podejście do obsługi klienta z lokalną obecnością w Hiszpanii.</p>
      <div class="hero-cta fade-up d2"><a class="btn btn-primary" href="#zespol">Poznaj zespół {I["arrow"]}</a><a class="btn btn-ghost" href="#kontakt">Kontakt</a></div>
    </div>
    <div class="div-mark" aria-hidden="true"><span class="glow"></span><img src="img/s-green.webp" alt="" width="240" height="240"></div>
  </div>
</section>

<section class="sec">
  <div class="wrap split">
    <div class="copy">
      <span class="eyebrow">Nasza historia</span>
      <h2 class="h2 split-words">Z Polski na <span class="gold-text">Costa del Sol</span></h2>
      <p class="lead rv">{ph("Historia firmy: kiedy powstała, kto ją założył, skąd pomysł na działalność w Hiszpanii i jak rozwinęła się do czterech obszarów działalności.")}</p>
      <p class="muted rv">Działamy na Costa del Sol, w okolicach Marbelli i Malagi. Zamiast zlecać kolejne etapy zewnętrznym firmom, zbudowaliśmy własne kompetencje w inwestycjach, pośrednictwie, renowacjach i sprzątaniu. Dzięki temu odpowiadamy za cały proces i za jego wynik.</p>
    </div>
    <div class="stack-media rv">
      <div class="media rv-img parallax">{ph_img("Zdjęcie zespołu lub biura", "np. wspólne zdjęcie na tle nieruchomości")}</div>
      <div class="media b rv-img">{photo("kuchnia-salon", sizes="30vw")}</div>
    </div>
  </div>
</section>

<section class="sec tint">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">Wartości</span></div>
    <div class="values" data-stagger>
      <div class="value"><strong>People</strong><p>Relacje z inwestorami i klientami opieramy na przejrzystości. Każdy wie, kto odpowiada za jego projekt.</p></div>
      <div class="value"><strong>Property</strong><p>Wartość nieruchomości budujemy jakością renowacji, dobrym wyborem lokalizacji i dbałością o detale.</p></div>
      <div class="value"><strong>Better Living</strong><p>Tworzymy wnętrza, w których chce się mieszkać — dla kupujących, gości i właścicieli.</p></div>
    </div>
  </div>
</section>

<section class="sec" id="zespol">
  <div class="wrap">
    <div class="sec-head split">
      <div style="display:grid;gap:22px"><span class="eyebrow">Zespół</span><h2 class="h2 split-words">Poznaj ludzi <span class="gold-text">Soffel Group</span></h2></div>
      <p class="lead rv">Miejsce na zdjęcia i krótkie biogramy zespołu. Kolor podpisu wskazuje obszar, w którym pracuje dana osoba.</p>
    </div>
    <div class="team" data-stagger>{team_html}</div>
  </div>
</section>

<section class="paper sec">
  <div class="wrap">
    <div class="sec-head split">
      <div style="display:grid;gap:22px"><span class="eyebrow">Struktura grupy</span><h2 class="h2 split-words">Cztery marki, jedna odpowiedzialność</h2></div>
      <p class="lead rv">Każda marka ma własną specjalizację i własny zespół, a wszystkie pracują według wspólnych standardów.</p>
    </div>
    <div class="cards c4" data-stagger>
      {"".join(f'<a class="card" href="{x["url"]}" style="--acc:{x["c"]}"><img src="img/{x["img"]}.webp" alt="" width="56" height="56" loading="lazy" style="width:56px;height:56px;object-fit:contain"><span class="k" style="color:{x["c"]}">{x["tag"]}</span><h3>Soffel {x["name"]}</h3><p>{x["desc"]}</p><span class="link-arrow" style="color:#0f1b16">Więcej {I["arrow"]}</span></a>' for x in DIVS)}
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head split">
      <div style="display:grid;gap:22px"><span class="eyebrow">Galeria</span><h2 class="h2 split-words">Z naszych realizacji</h2></div>
      <p class="lead rv">{ph("Miejsce na zdjęcia z życia firmy: zespół na budowie, spotkania z inwestorami, nieruchomości w Hiszpanii.")}</p>
    </div>
    <div class="gallery" data-lb>
      <figure class="w">{photo("salon-2", sizes="50vw")}</figure>
      <figure class="t">{photo("lazienka-kamien", sizes="25vw")}</figure>
      <figure>{ph_img("Zespół na budowie")}</figure>
      <figure>{photo("sypialnia-2", sizes="25vw")}</figure>
      <figure class="w">{ph_img("Nieruchomość w Marbelli", "zdjęcie z zewnątrz")}</figure>
    </div>
  </div>
</section>

{contact("inv")}
'''
    page("o-nas", "O nas i zespół — Soffel Group | Nieruchomości na Costa del Sol",
         "Poznaj Soffel Group: cztery marki i zespół, który prowadzi inwestycje, sprzedaż, renowacje i sprzątanie nieruchomości w Marbelli i Maladze.",
         "group", body, "about")

if __name__ == "__main__":
    build_index(); build_inv(); build_prop(); build_reno(); build_clean(); build_about()

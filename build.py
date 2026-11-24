#!/usr/bin/env python3
"""Generate index.html — clone of the natsutamura link page, without any Linktree branding."""
import json, re, pathlib

BASE = pathlib.Path(__file__).parent
A = BASE / "assets"

brand = json.loads((A / "icons.json").read_text())

def tabler(name):
    svg = (A / f"icon-{name}.svg").read_text()
    svg = re.sub(r"<!--.*?-->", "", svg, flags=re.S)
    m = re.search(r"<svg.*?</svg>", svg, flags=re.S)
    return re.sub(r"\s+", " ", m.group(0))

def svg_from_brand(key, cls=""):
    paths = "".join(f'<path d="{d}" fill-rule="evenodd" clip-rule="evenodd"/>' for d in brand[key])
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">{paths}</svg>'

KEBAB = svg_from_brand("menu_ig").replace('viewBox="0 0 24 24"', 'viewBox="0 0 3 11"')

SOCIALS = [
    ("TikTok", "tiktok", "https://tiktok.com/@raybacabuku"),
    ("WhatsApp", "whatsapp", "https://api.whatsapp.com/send?phone=6285157677224"),
    ("Instagram", "instagram", "https://instagram.com/natsutamura"),
    ("Facebook", "facebook", "https://www.facebook.com/rayyplayid"),
    ("YouTube", "youtube", "https://www.youtube.com/channel/UCc9N1sfGO6BuGeyFGbUchfQ"),
]

ABOUT_TEXT = (
    "I am a graphic designer, graduated in a High School majoring in Visual Communication Design (DKV), "
    "who uses Adobe Illustrator and Photoshop. I have strong skills in image editing, typography, and layout. "
    "I am also accustomed to working on various types of projects, ranging from Logo &amp; Branding, Social Media, and UI/UX.\n"
    "I always strive to produce high-quality work that meets the needs of both clients and companies."
)

ROWS = [
    ("Order Form", "shopping-cart", "https://tally.so/r/w5x0PN", ""),
    ("Last.fm", "brand-lastfm", "https://www.last.fm/user/natsutamura", ""),
    ("Discord server", "brand-discord", "https://discord.gg/KY6Dqsw", '<span class="sub__ico">' + tabler("brand-discord") + "</span>Discord Server · Free to join"),
    ("Email", "mail", "mailto:raymut8@gmail.com", '<span class="sub__ico">' + tabler("mail") + "</span>Email · raymut8@gmail.com"),
    ("Github", "brand-github", "https://github.com/natsutamura", ""),
]

socials_html = "\n".join(
    f'        <a class="social" href="{url}" target="_blank" rel="noopener noreferrer" aria-label="{name}">{svg_from_brand(key)}</a>'
    for name, key, url in SOCIALS
)

rows_html = ""
for title, icon, url, sub in ROWS:
    sub_html = (
        f'\n          <span class="row__sub">{sub}</span>' if sub else ""
    )
    rows_html += f"""
        <div class="card row-card">
          <a class="row" href="{url}" target="_blank" rel="noopener noreferrer" aria-label="{title}">
            <span class="row__ico" aria-hidden="true">{tabler(icon)}</span>
            <span class="row__label">{title}</span>{sub_html}
          </a>
          <button class="kebab" type="button" aria-label="Opsi untuk {title}" data-share="{url}" data-title="{title}">{KEBAB}</button>
        </div>"""

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#0A0A0A">
<title>Ray — an ordinary content creator</title>
<meta name="description" content="Ray — an ordinary content creator. Graphic designer: logo &amp; branding, social media, UI/UX.">
<meta property="og:type" content="profile">
<meta property="og:title" content="Ray — an ordinary content creator">
<meta property="og:description" content="Graphic designer: logo &amp; branding, social media, UI/UX.">
<meta property="og:image" content="assets/avatar.jpg">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='16' fill='%230A0A0A'/%3E%3Ctext x='32' y='44' font-family='Inter,Arial' font-size='34' font-weight='600' fill='%23fff' text-anchor='middle'%3ER%3C/text%3E%3C/svg%3E">
<style>
@font-face {{
  font-family: "Inter";
  src: url("assets/inter-latin.woff2") format("woff2");
  font-weight: 100 900;
  font-display: swap;
}}
:root {{
  --bg: #0A0A0A;
  --line: #2A2A2A;
  --line-hover: #3E3E3E;
  --text: #FFFFFF;
  --text-soft: #EAEAEA;
  --radius: 8px;
}}
* {{ box-sizing: border-box; }}
html, body {{ margin: 0; padding: 0; }}
body {{
  background: #000;
  color: var(--text);
  font-family: "Inter", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  font-synthesis-weight: none;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-rendering: optimizeLegibility;
}}
img {{ display: block; max-width: 100%; }}
a {{ color: inherit; text-decoration: none; }}
button {{ font: inherit; color: inherit; }}

.page {{
  position: relative;
  width: 100%;
  max-width: 430px;
  min-height: 100vh;
  min-height: 100dvh;
  margin: 0 auto;
  padding: 0 14px 40px;
  background: var(--bg);
  display: flex;
  flex-direction: column;
}}
@media (min-width: 640px) {{
  body {{ background: #050505; }}
  .page {{
    min-height: calc(100vh - 40px);
    min-height: calc(100dvh - 40px);
    margin: 20px auto;
    border-radius: 16px;
  }}
  .row__label {{ font-size: 16px; }}
}}

/* ---------- top bar ---------- */
.topbar {{
  display: flex;
  align-items: center;
  justify-content: flex-end;
  height: 68px;
  padding: 14px 0;
}}
.iconbtn {{
  width: 40px; height: 40px;
  display: grid; place-items: center;
  border: 0; border-radius: 999px;
  background: rgba(255,255,255,.12);
  color: #fff; cursor: pointer;
  transition: background .15s ease, transform .15s ease;
}}
.iconbtn:hover {{ background: rgba(255,255,255,.22); }}
.iconbtn:active {{ transform: scale(.94); }}
.iconbtn svg {{ width: 20px; height: 20px; }}

/* ---------- profile head ---------- */
.head {{
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 36px;
  text-align: center;
}}
.avatar {{
  width: 96px; height: 96px;
  border-radius: 999px;
  object-fit: cover;
  background: #1a1a1a;
  box-shadow: 0 0 0 1px rgba(255,255,255,.13), 0 8px 24px rgba(0,0,0,.45);
}}
.name {{
  margin: 13px 0 0;
  font-size: 24px;
  font-weight: 600;
  line-height: 33px;
  letter-spacing: -.2px;
  color: var(--text-soft);
}}
.bio {{
  margin: 3px 0 0;
  font-size: 16px;
  font-weight: 500;
  line-height: 24px;
  color: var(--text-soft);
}}
.socials {{
  display: flex;
  justify-content: center;
  margin-top: 8px;
}}
.followers {{
  margin: 10px 0 0;
  display: inline-flex;
  align-items: center;
  height: 26px;
  padding: 4px 12px;
  border-radius: 999px;
  background: rgba(255,255,255,.1);
  color: var(--text);
  font-size: 12px;
  font-weight: 500;
  line-height: 1.4;
}}
.social {{
  width: 48px; height: 48px;
  display: grid; place-items: center;
  border-radius: 12px;
  color: var(--text-soft);
  transition: opacity .15s ease, transform .15s ease;
}}
.social:hover {{ opacity: .7; transform: translateY(-1px); }}
.social svg {{ width: 32px; height: 32px; fill: currentColor; }}

/* ---------- cards ---------- */
.cards {{
  margin-top: 28px;
  display: flex;
  flex-direction: column;
  gap: 14px;
}}
.card {{
  position: relative;
  width: 100%;
  border: 1px solid var(--line);
  border-radius: var(--radius);
  background: transparent;
  transition: border-color .15s ease, background .15s ease, transform .15s ease;
}}
.card:has(a:hover), .card:hover {{ border-color: var(--line-hover); }}
.card:active {{ transform: scale(.995); }}

/* link row */
.row {{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1px;
  min-height: 64px;
  padding: 12px 64px;
  letter-spacing: -.2px;
  text-align: center;
}}
.row__ico {{
  position: absolute;
  left: 8px; top: 50%;
  transform: translateY(-50%);
  width: 48px; height: 48px;
  display: grid; place-items: center;
  color: var(--text);
}}
.row__ico svg {{ width: 32px; height: 32px; display: block; }}
.row__label {{
  font-size: 14px;
  font-weight: 500;
  line-height: 1.2;
  color: var(--text);
  text-wrap: balance;
}}
.row__sub {{
  display: flex;
  align-items: center;
  gap: 4px;
  padding-bottom: 2px;
  font-size: 12px;
  line-height: 1.4;
  color: var(--text);
  opacity: .6;
  max-width: 100%;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}}
.sub__ico {{ display: inline-flex; }}
.sub__ico svg {{ width: 14px; height: 14px; }}

/* kebab */
.kebab {{
  position: absolute;
  right: 12px; top: 50%;
  transform: translateY(-50%);
  width: 24px; height: 24px;
  display: grid; place-items: center;
  border: 0; border-radius: 12px;
  background: transparent;
  color: var(--text);
  opacity: .5;
  cursor: pointer;
  transition: opacity .15s ease, background .15s ease;
}}
.kebab:hover {{ opacity: 1; background: rgba(255,255,255,.1); }}
.kebab svg {{ width: 3px; height: 11px; fill: currentColor; }}

/* ---------- about card ---------- */
.about {{ padding: 20px; text-align: left; }}
.about__title {{
  margin: 0 0 4px;
  font-size: 16px;
  font-weight: 500;
  line-height: 20px;
  color: var(--text);
}}
.about__text {{
  margin: 0;
  font-size: 14px;
  font-weight: 400;
  line-height: 20px;
  color: var(--text);
  white-space: pre-line;
  display: -webkit-box;
  -webkit-line-clamp: 9;
  -webkit-box-orient: vertical;
  overflow: hidden;
}}
.about.is-open .about__text {{ -webkit-line-clamp: unset; overflow: visible; }}
.about__more {{
  margin-top: 16px;
  padding: 0;
  border: 0;
  background: none;
  color: var(--text);
  font-size: 16px;
  font-weight: 400;
  line-height: 26px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}}
.about__more svg {{ width: 14px; height: 14px; transition: transform .2s ease; }}
.about.is-open .about__more svg {{ transform: rotate(180deg); }}
.about__cta {{
  display: none;
  margin-top: 16px;
  width: 100%;
  min-height: 44px;
  padding: 12px 16px;
  border: 1px solid var(--line);
  border-radius: var(--radius);
  background: rgba(255,255,255,.06);
  color: var(--text);
  font-size: 14px;
  font-weight: 500;
  text-align: center;
  cursor: pointer;
  transition: background .15s ease, border-color .15s ease;
}}
.about.is-open .about__cta {{ display: block; }}
.about__cta:hover {{ background: rgba(255,255,255,.12); border-color: var(--line-hover); }}
.about .kebab {{ top: 16px; transform: none; }}
.about__head {{ display: flex; align-items: flex-start; justify-content: space-between; gap: 12px; }}
.about__head .about__title {{ margin-bottom: 0; }}

/* ---------- media (instagram) card ---------- */
.media__frame {{
  display: flex;
  justify-content: center;
  aspect-ratio: 16 / 9;
  padding: 16px 16px 0;
  overflow: hidden;
  border-radius: var(--radius) var(--radius) 0 0;
}}
.media__frame img {{
  height: 100%;
  width: auto;
  aspect-ratio: 1 / 1;
  object-fit: cover;
  border-radius: 6px;
  outline: 1px solid rgba(255,255,255,.1);
  outline-offset: -1px;
  transition: transform .4s ease;
}}
.media:hover .media__frame img {{ transform: scale(1.02); }}
.media__chin {{
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  padding: 12px 32px;
  text-align: center;
}}
.media .kebab {{ top: 112px; transform: none; }}
.media__label {{ font-size: 14px; font-weight: 500; line-height: 1.2; }}
.media__sub {{
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 12px;
  line-height: 1.4;
  opacity: .6;
  margin: 0;
}}
.media__sub svg {{ width: 14px; height: 14px; fill: currentColor; }}
.pill {{
  margin-top: 4px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  height: 26px;
  padding: 4px 12px;
  border-radius: 999px;
  background: rgba(255,255,255,.14);
  font-size: 12px;
  font-weight: 500;
  color: #fff;
  transition: background .15s ease;
}}
.pill:hover {{ background: rgba(255,255,255,.24); }}

/* ---------- footer ---------- */
.foot {{
  margin-top: auto;
  padding-top: 56px;
  text-align: center;
  font-size: 12px;
  line-height: 1.6;
  color: rgba(255,255,255,.4);
}}
.foot a:hover {{ color: rgba(255,255,255,.7); }}

/* ---------- toast + menu ---------- */
.toast {{
  position: fixed;
  left: 50%;
  bottom: 28px;
  transform: translate(-50%, 16px);
  padding: 10px 16px;
  border-radius: 999px;
  background: rgba(255,255,255,.95);
  color: #000;
  font-size: 13px;
  font-weight: 500;
  opacity: 0;
  pointer-events: none;
  transition: opacity .2s ease, transform .2s ease;
  z-index: 60;
}}
.toast.is-on {{ opacity: 1; transform: translate(-50%, 0); }}

.menu {{
  position: absolute;
  right: 8px;
  z-index: 40;
  min-width: 168px;
  padding: 6px;
  border: 1px solid #333;
  border-radius: 10px;
  background: #161616;
  box-shadow: 0 12px 32px rgba(0,0,0,.6);
  display: none;
}}
.menu.is-on {{ display: block; }}
.menu button {{
  display: flex;
  align-items: center;
  gap: 8px;
  width: 100%;
  padding: 9px 10px;
  border: 0;
  border-radius: 6px;
  background: none;
  color: #fff;
  font-size: 13px;
  text-align: left;
  cursor: pointer;
}}
.menu button:hover {{ background: rgba(255,255,255,.08); }}

@media (prefers-reduced-motion: reduce) {{
  * {{ transition: none !important; animation: none !important; }}
}}
</style>
</head>
<body>
<div class="page">

  <div class="topbar">
    <button class="iconbtn" id="share-page" type="button" aria-label="Bagikan halaman">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M12 16V4"/><path d="m8 8 4-4 4 4"/><path d="M4 15v3a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-3"/>
      </svg>
    </button>
  </div>

  <header class="head">
    <img class="avatar" src="assets/avatar.jpg" alt="Ray" width="96" height="96">
    <h1 class="name">Ray</h1>
    <p class="bio">an ordinary content creator</p>
    <nav class="socials" aria-label="Media sosial">
{socials_html}
    </nav>
    <p class="followers">2K followers</p>
  </header>

  <main class="cards">

    <section class="card about" id="about">
      <div class="about__head">
        <h2 class="about__title">About Me</h2>
        <button class="kebab" type="button" aria-label="Opsi untuk About Me" data-share="#about" data-title="About Me">{KEBAB}</button>
      </div>
      <p class="about__text">{ABOUT_TEXT}</p>
      <button class="about__more" type="button" id="about-toggle" aria-expanded="false" aria-controls="about">More</button>
      <a class="about__cta" href="https://tally.so/r/w5x0PN" target="_blank" rel="noopener noreferrer">Start project with me!</a>
    </section>

    <section class="card media">
      <a class="media__frame" href="https://instagram.com/natsutamura" target="_blank" rel="noopener noreferrer" aria-label="Instagram">
        <img src="assets/ig-post.jpg" alt="Postingan Instagram terbaru" loading="lazy">
      </a>
      <div class="media__chin">
        <a class="media__label" href="https://instagram.com/natsutamura" target="_blank" rel="noopener noreferrer">Instagram</a>
        <p class="media__sub">{svg_from_brand("instagram")}<span>@natsutamura · 860 followers</span></p>
        <a class="pill" href="https://instagram.com/natsutamura" target="_blank" rel="noopener noreferrer">Follow on Instagram</a>
      </div>
      <button class="kebab" type="button" aria-label="Opsi untuk Instagram" data-share="https://instagram.com/natsutamura" data-title="Instagram">{KEBAB}</button>
    </section>
{rows_html}

  </main>

  <footer class="foot">© <span id="year">2026</span> Ray</footer>
</div>

<div class="toast" id="toast" role="status" aria-live="polite"></div>

<script>
(function () {{
  var toastEl = document.getElementById('toast');
  var toastTimer;

  function toast(msg) {{
    toastEl.textContent = msg;
    toastEl.classList.add('is-on');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () {{ toastEl.classList.remove('is-on'); }}, 1800);
  }}

  function copy(text) {{
    if (navigator.clipboard && navigator.clipboard.writeText) {{
      return navigator.clipboard.writeText(text).then(function () {{ return true; }}, function () {{ return false; }});
    }}
    return Promise.resolve(false);
  }}

  function sharePage(title, url) {{
    var data = {{ title: title || document.title, url: url || location.href }};
    if (navigator.share) {{
      navigator.share(data).catch(function () {{}});
      return;
    }}
    copy(data.url).then(function (ok) {{
      toast(ok ? 'Link disalin' : data.url);
    }});
  }}

  document.getElementById('share-page').addEventListener('click', function () {{
    sharePage(document.title, location.href);
  }});

  /* about expand */
  var about = document.getElementById('about');
  var toggle = document.getElementById('about-toggle');
  toggle.addEventListener('click', function () {{
    var open = about.classList.toggle('is-open');
    toggle.setAttribute('aria-expanded', String(open));
    toggle.textContent = open ? 'Less' : 'More';
  }});

  /* kebab menus */
  var openMenu = null;
  function closeMenu() {{
    if (openMenu) {{ openMenu.remove(); openMenu = null; }}
  }}
  document.addEventListener('click', function (e) {{
    if (openMenu && !openMenu.contains(e.target) && !e.target.closest('.kebab')) closeMenu();
  }});
  document.addEventListener('keydown', function (e) {{ if (e.key === 'Escape') closeMenu(); }});

  Array.prototype.forEach.call(document.querySelectorAll('.kebab'), function (btn) {{
    btn.addEventListener('click', function (e) {{
      e.preventDefault();
      e.stopPropagation();
      if (openMenu && openMenu.dataset.owner === btn.dataset.share) {{ closeMenu(); return; }}
      closeMenu();
      var target = btn.dataset.share;
      var url = target.charAt(0) === '#' ? location.href.split('#')[0] : target;
      var menu = document.createElement('div');
      menu.className = 'menu is-on';
      menu.dataset.owner = target;
      menu.innerHTML = '<button type="button" data-act="copy">Salin link</button>' +
                       '<button type="button" data-act="share">Bagikan</button>';
      menu.addEventListener('click', function (ev) {{
        var act = ev.target.getAttribute('data-act');
        if (!act) return;
        ev.stopPropagation();
        if (act === 'copy') copy(url).then(function (ok) {{ toast(ok ? 'Link disalin' : url); }});
        else sharePage(btn.dataset.title, url);
        closeMenu();
      }});
      btn.parentElement.appendChild(menu);
      var r = btn.getBoundingClientRect(), pr = btn.parentElement.getBoundingClientRect();
      menu.style.top = (r.bottom - pr.top + 6) + 'px';
      openMenu = menu;
    }});
  }});

  document.getElementById('year').textContent = new Date().getFullYear();
}})();
</script>
</body>
</html>
"""

(BASE / "index.html").write_text(HTML)
print("wrote", BASE / "index.html", len(HTML), "bytes")

import os
from flask import Flask, render_template

# Získa cestu k nadradenému priečinku (koreň projektu)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__,
            template_folder=os.path.join(BASE_DIR, 'templates'),
            static_folder=os.path.join(BASE_DIR, 'static'))
DATA = {
    "meno": "Alex Novák",
    "profesia": "Digitálny dizajnér & konzultant",
    "tagline": "Pomáham firmám aj jednotlivcom premeniť ich myšlienky na funkčné a vizuálne príťažlivé digitálne produkty.",
    "o_mne": "Vyše 8 rokov sa venujem dizajnu a digitálnym produktom. Spolupracujem s klientmi na weboch, aplikáciách a vizuálnej identite. Mojím cieľom je, aby každý projekt nebol len pekný, ale aj funkčný a zrozumiteľný pre používateľa.",
    "email": "alex@novak.sk",
    "telefon": "+421 900 123 456",
    "lokacia": "Bratislava, Slovensko",
    "sluzby": [
        {"nazov": "Web dizajn", "popis": "Návrh moderných, responzívnych webstránok na mieru — od wireframu po finálny dizajn."},
        {"nazov": "Konzultácie", "popis": "Pomôžem s UX, stratégiou a výberom technológií pre váš digitálny projekt."},
        {"nazov": "Branding", "popis": "Logo, vizuálna identita a jednotný štýl značky naprieč všetkými kanálmi."},
    ],
    "social": [
        {"nazov": "LinkedIn", "url": "#"},
        {"nazov": "GitHub", "url": "#"},
        {"nazov": "Instagram", "url": "#"},
    ],
    "recenzie": [
        {"text": "Výborné služby. Doporučujem.", "autor": "Klient", "typ": "firemná akcia"},
        {"text": "Super zvuk. Teším sa aj na budúce.", "autor": "Klient", "typ": "oslavy"},
        {"text": "Ďakujem za super spoluprácu.", "autor": "Klient", "typ": "podujatie"},
        {"text": "Dik za perfektný večer. Zvuk sa mi veľmi páčil.", "autor": "Klient", "typ": "svadba"},
    ],
    "partneri": ["DJ Laky", "Bratislavský country band", "SOELWE"],
}

# ---------- ROZCESTNÍK ----------

@app.route("/")
@app.route("/api")
def index():
    return """
    <!DOCTYPE html>
    <html lang="sk">
    <head>
        <meta charset="UTF-8">
        <title>Webvizitky — 11 konceptov</title>
        <style>
            body {
                font-family: system-ui, sans-serif;
                background: #0a0a0f;
                color: #f0f0f5;
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 40px;
                margin: 0;
            }
            .wrap { max-width: 900px; width: 100%; }
            h1 { font-size: 2.5rem; margin-bottom: 12px; letter-spacing: -0.03em; }
            p.sub { color: #8a8a95; margin-bottom: 40px; }
            .grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
                gap: 16px;
            }
            a.card {
                display: block;
                padding: 24px;
                background: #14141c;
                border: 1px solid #262630;
                border-radius: 12px;
                color: #f0f0f5;
                text-decoration: none;
                transition: all 0.2s;
            }
            a.card:hover {
                border-color: #22d3ee;
                transform: translateY(-3px);
                background: #1a1a24;
            }
            .num { color: #22d3ee; font-size: 0.8rem; font-weight: 600; letter-spacing: 0.1em; }
            .name { font-size: 1.2rem; font-weight: 600; margin: 8px 0 6px; }
            .desc { color: #8a8a95; font-size: 0.85rem; line-height: 1.5; }
        </style>
    </head>
    <body>
        <div class="wrap">
            <h1>Webvizitky</h1>
            <p class="sub">11 dizajnových konceptov — klikni na ktorýkoľvek</p>
            <div class="grid">
                <a class="card" href="/api/v1"><div class="num">01</div><div class="name">Aurora</div><div class="desc">Tmavé gradienty, tech</div></a>
                <a class="card" href="/api/v2"><div class="num">02</div><div class="name">Split Screen</div><div class="desc">50/50 split, energický</div></a>
                <a class="card" href="/api/v3"><div class="num">03</div><div class="name">Bento Grid</div><div class="desc">Mozaika dlaždíc</div></a>
                <a class="card" href="/api/v4"><div class="num">04</div><div class="name">Editorial</div><div class="desc">Magazín, krémový</div></a>
                <a class="card" href="/api/v5"><div class="num">05</div><div class="name">Glass</div><div class="desc">Priehľadné karty</div></a>
                <a class="card" href="/api/v6"><div class="num">06</div><div class="name">Typographic</div><div class="desc">Marquee, Bebas Neue</div></a>
                <a class="card" href="/api/v7"><div class="num">07</div><div class="name">Luxury</div><div class="desc">Zlaté línie, hotel</div></a>
                <a class="card" href="/api/v8"><div class="num">08</div><div class="name">Wellness</div><div class="desc">Organické tvary</div></a>
                <a class="card" href="/api/v9"><div class="num">09</div><div class="name">Tech Dark</div><div class="desc">Kód v pozadí</div></a>
                <a class="card" href="/api/v10"><div class="num">10</div><div class="name">Stage Lights</div><div class="desc">Svetelné lúče (ozvučenie)</div></a>
                <a class="card" href="/api/v11"><div class="num">11</div><div class="name">Sound Waves</div><div class="desc">Zvukové vlny (ozvučenie)</div></a>
            </div>
        </div>
    </body>
    </html>
    """

# ---------- ROUTES S /api PREDPONOU ----------

@app.route("/api/v1")
def v1(): return render_template("modern-a.html", data=DATA)

@app.route("/api/v2")
def v2(): return render_template("split.html", data=DATA)

@app.route("/api/v3")
def v3(): return render_template("bento.html", data=DATA)

@app.route("/api/v4")
def v4(): return render_template("editorial.html", data=DATA)

@app.route("/api/v5")
def v5(): return render_template("glass.html", data=DATA)

@app.route("/api/v6")
def v6(): return render_template("typographic.html", data=DATA)

@app.route("/api/v7")
def v7(): return render_template("luxury.html", data=DATA)

@app.route("/api/v8")
def v8(): return render_template("wellness.html", data=DATA)

@app.route("/api/v9")
def v9(): return render_template("tech-dark.html", data=DATA)

@app.route("/api/v10")
def v10(): return render_template("stage.html", data=DATA)

@app.route("/api/v11")
def v11(): return render_template("waves.html", data=DATA)

# ---------- FALLBACK (ak Vercel pošle cestu bez /api) ----------

@app.route("/v1")
def v1_fallback(): return render_template("modern-a.html", data=DATA)

@app.route("/v2")
def v2_fallback(): return render_template("split.html", data=DATA)

@app.route("/v3")
def v3_fallback(): return render_template("bento.html", data=DATA)

@app.route("/v4")
def v4_fallback(): return render_template("editorial.html", data=DATA)

@app.route("/v5")
def v5_fallback(): return render_template("glass.html", data=DATA)

@app.route("/v6")
def v6_fallback(): return render_template("typographic.html", data=DATA)

@app.route("/v7")
def v7_fallback(): return render_template("luxury.html", data=DATA)

@app.route("/v8")
def v8_fallback(): return render_template("wellness.html", data=DATA)

@app.route("/v9")
def v9_fallback(): return render_template("tech-dark.html", data=DATA)

@app.route("/v10")
def v10_fallback(): return render_template("stage.html", data=DATA)

@app.route("/v11")
def v11_fallback(): return render_template("waves.html", data=DATA)


if __name__ == "__main__":
    app.run(debug=True)
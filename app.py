from flask import Flask, render_template

app = Flask(__name__)

DATA = {
    "meno": "Alex Novák",
    "profesia": "Digitálny dizajnér & konzultant",
    "tagline": "...",
    "o_mne": "...",
    "email": "alex@novak.sk",
    "telefon": "+421 900 123 456",
    "lokacia": "Bratislava, Slovensko",
    "sluzby": [
        {"nazov": "Web dizajn", "popis": "..."},
        {"nazov": "Konzultácie", "popis": "..."},
        {"nazov": "Branding", "popis": "..."},
    ],
    "social": [
        {"nazov": "LinkedIn", "url": "#"},
        {"nazov": "GitHub", "url": "#"},
        {"nazov": "Instagram", "url": "#"},
    ],
    # ↓↓↓ TOTO PRIDAJ ↓↓↓
    "recenzie": [
        {"text": "Výborné služby. Doporučujem.", "autor": "Klient", "typ": "firemná akcia"},
        {"text": "Super zvuk. Teším sa aj na budúce.", "autor": "Klient", "typ": "oslavy"},
        {"text": "Ďakujem za super spoluprácu.", "autor": "Klient", "typ": "podujatie"},
        {"text": "Dik za perfektný večer. Zvuk sa mi veľmi páčil.", "autor": "Klient", "typ": "svadba"},
    ],
    "partneri": ["DJ Laky", "Bratislavský country band", "SOELWE"],
}

# ---------- ROUTES (všetky pred app.run) ----------

@app.route("/")
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
                <a class="card" href="/v1"><div class="num">01</div><div class="name">Aurora</div><div class="desc">Tmavé gradienty, tech</div></a>
                <a class="card" href="/v2"><div class="num">02</div><div class="name">Split Screen</div><div class="desc">50/50 split, energický</div></a>
                <a class="card" href="/v3"><div class="num">03</div><div class="name">Bento Grid</div><div class="desc">Mozaika dlaždíc</div></a>
                <a class="card" href="/v4"><div class="num">04</div><div class="name">Editorial</div><div class="desc">Magazín, krémový</div></a>
                <a class="card" href="/v5"><div class="num">05</div><div class="name">Glass</div><div class="desc">Priehľadné karty</div></a>
                <a class="card" href="/v6"><div class="num">06</div><div class="name">Typographic</div><div class="desc">Marquee, Bebas Neue</div></a>
                <a class="card" href="/v7"><div class="num">07</div><div class="name">Luxury</div><div class="desc">Zlaté línie, hotel</div></a>
                <a class="card" href="/v8"><div class="num">08</div><div class="name">Wellness</div><div class="desc">Organické tvary</div></a>
                <a class="card" href="/v9"><div class="num">09</div><div class="name">Tech Dark</div><div class="desc">Kód v pozadí</div></a>
                <a class="card" href="/v10"><div class="num">10</div><div class="name">Stage Lights</div><div class="desc">Svetelné lúče (ozvučenie)</div></a>
                <a class="card" href="/v11"><div class="num">11</div><div class="name">Sound Waves</div><div class="desc">Zvukové vlny (ozvučenie)</div></a>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
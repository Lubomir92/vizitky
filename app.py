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
    return render_template("modern-a.html", data=DATA)

# Staré verzie (modern-*)
@app.route("/a")
def a():
    return render_template("modern-a.html", data=DATA)

@app.route("/b")
def b():
    return render_template("modern-b.html", data=DATA)

@app.route("/c")
def c():
    return render_template("modern-c.html", data=DATA)

@app.route("/d")
def d():
    return render_template("modern-d.html", data=DATA)

# Nové koncepty (v1, v2, ...)
@app.route("/v1")
def v1():
    return render_template("modern-a.html", data=DATA)   # Aurora = staré A

@app.route("/v2")
def v2():
    return render_template("split.html", data=DATA)      # Split Screen

@app.route("/v3")
def v3():
    return render_template("bento.html", data=DATA)

@app.route("/v4")
def v4():
    return render_template("editorial.html", data=DATA)
@app.route("/v5")
def v5():
    return render_template("glass.html", data=DATA)

@app.route("/v6")
def v6():
    return render_template("typographic.html", data=DATA)
@app.route("/v7")
def v7(): return render_template("luxury.html", data=DATA)

@app.route("/v8")
def v8(): return render_template("wellness.html", data=DATA)

@app.route("/v9")
def v9(): return render_template("tech-dark.html", data=DATA)

@app.route("/v10")
def v10(): return render_template("stage.html", data=DATA)

@app.route("/v11")
def v11(): return render_template("waves.html", data=DATA)

if __name__ == "__main__":
    app.run(debug=True)
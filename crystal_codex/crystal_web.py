# crystal_codex/crystal_web.py

from flask import Flask, render_template_string, request
from crystal_codex.file_writer import load_codex

app = Flask(__name__)
codex = load_codex()

# HTML Template
TEMPLATE = """
<!doctype html>
<title>Crystal Codex Web</title>
<h1>🔮 Crystal Search</h1>
<form method="POST">
    Mood: <input name="mood">
    <input type="submit" value="Find My Crystal">
</form>

{% if result %}
    <h2>💎 Your Crystal: {{ result }}</h2>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        mood = request.form["mood"].lower()
        mood_map = {
            "sad": "rose quartz",
            "anxious": "amethyst",
            "tired": "carnelian",
            "confused": "fluorite",
            "happy": "citrine",
        }
        crystal_name = mood_map.get(mood)
        if crystal_name and crystal_name in codex:
            info = codex[crystal_name]
            result = f"{crystal_name.title()} — Chakra: {info['chakra']}, Color: {info['color']}, Element: {info['element']}, Effect: {info.get('effect', 'Unknown')}"
        else:
            result = "No matching crystal found for that mood."

    return render_template_string(TEMPLATE, result=result)

if __name__ == "__main__":
    app.run(debug=True)

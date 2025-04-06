import json
import os

def get_codex_path():
    return os.path.join(os.path.dirname(__file__), "codex.json")

def load_codex():
    with open(get_codex_path(), "r") as file:
        return json.load(file)

def save_codex(codex):
    with open(get_codex_path(), "w") as file:
        json.dump(codex, file, indent=4)

def recommend_crystal(mood):
    codex = {
        "sad": "rose quartz",
        "tired": "carnelian",
        "ok": "amethyst",
        "happy": "fluorite",
        "joyful": "citrine"
    }
    return codex.get(mood, "clear quartz")

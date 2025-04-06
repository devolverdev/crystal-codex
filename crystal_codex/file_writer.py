# crystal_codex/file_writer.py

import json

import os
print("📁 Running from:", os.getcwd())


def save_codex(data, filename="codex.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print("💾 Codex saved!")

def load_codex(filename="codex.json"):
    with open(filename, "r") as file:
        return json.load(file)


# crystal_codex/09 FileHandling.py

from crystal_codex.file_writer import save_codex, load_codex

test_data = {
    "fluorite": {
        "chakra": "third eye",
        "color": "green",
        "element": "air",
        "effect": "focus and clarity"
    }
}

save_codex(test_data)
loaded = load_codex()

print("🔍 Codex content:")
print(loaded)

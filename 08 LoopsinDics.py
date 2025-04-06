
import json  # built-in library


# Load from file
with open("codex.json", "r") as file:
    crystal_codex = json.load(file)

# Try it out
print("🔮 Welcome back to your Codex. Here’s what’s inside:\n")

for gem, info in crystal_codex.items():
    print("💎", gem.title())
    print("   Element:", info["element"])
    print("   Color:", info["color"])
    print("   Chakra:", info["chakra"])
    print("   Healing:", info["healing"])
    print()




##### 🌱 Your Crystal Codex
crystal_codex = {
    "rose quartz": {
        "element": "water",
        "color": "pink",
        "chakra": "heart",
        "healing": "opens the heart, promotes love and compassion"
    },
    "obsidian": {
        "element": "earth",
        "color": "black",
        "chakra": "root",
        "healing": "protects and grounds, absorbs negativity"
    },
    "amethyst": {
        "element": "air",
        "color": "purple",
        "chakra": "crown",
        "healing": "soothes the mind, aids spiritual awareness"
    },
    "citrine": {
        "element": "fire",
        "color": "gold",
        "chakra": "solar plexus",
        "healing": "boosts confidence, attracts prosperity"
    }
}

# 🌈 Ask the user for a search keyword
query = input("What are you seeking? (chakra, element, or healing word): ").lower()

# 📖 Search the codex
print("\n🔎 Searching the Codex for:", query)

found = False  # helps us know if we matched anything


for gem, info in crystal_codex.items():
    if (
        query in info["chakra"]
        or query in info["element"]
        or query in info["healing"]
    ):
        found = True
        print("\n💎", gem.title())
        print("   🌬️ Element:", info["element"])
        print("   🎨 Color:", info["color"])
        print("   🌀 Chakra:", info["chakra"])
        print("   🌿 Healing:", info["healing"])

if not found:
    print("\n🧘 No matching crystals found, but clarity is always with you.")


 ##Save to file
with open("codex.json", "w") as file:
    json.dump(crystal_codex, file, indent=4)

print("✅ Codex saved to codex.json!")




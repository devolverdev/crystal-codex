
###


chakras = {
    "heart": {
        "location": "center chest",
        "color": "pink",
        "gem": "rose quartz"
    },
    "crown": {
        "location": "head",
        "color": "purple",
        "gem": "obsidian"
    }
}

feel = input("What chakra do you feel like working with today? ").lower()

info = chakras.get(feel, {
    "location": "solar plexus",
    "color": "white",
    "gem": "turmaline"
})

print("🔮 Location:", info["location"])
print("🎨 Color:", info["color"])
print("✨ Gem:", info["gem"])



###


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
    },
    "fluorite": {
        "element": "air",
        "color": "green / purple",
        "chakra": "third eye",
        "healing": "clarifies thoughts, enhances intuition"
    },
    "carnelian": {
        "element": "fire",
        "color": "orange",
        "chakra": "sacral",
        "healing": "energizes the body, stimulates creativity"
    },
    "clear quartz": {
        "element": "ether",
        "color": "clear",
        "chakra": "all",
        "healing": "amplifies energy, programs intention"
    },
    "black tourmaline": {
        "element": "earth",
        "color": "black",
        "chakra": "root",
        "healing": "shields against negativity, stabilizes emotions"
    }
}
gem = input("Which gem are you drawn to? ").lower()

info = crystal_codex.get(gem, {
    "element": "ether",
    "color": "clear",
    "chakra": "all",
    "healing": "amplifies intention and opens space"
})

print("\n💎 Gem:", gem.title())
print("🌬️ Element:", info["element"])
print("🎨 Color:", info["color"])
print("🌀 Chakra:", info["chakra"])
print("🌿 Healing:", info["healing"])


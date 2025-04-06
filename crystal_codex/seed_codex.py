from crystal_codex.file_writer import save_codex

starter_codex = {
    "rose quartz": {
        "chakra": "heart",
        "color": "pink",
        "element": "water",
        "effect": "promotes love and emotional healing"
    },
    "amethyst": {
        "chakra": "crown",
        "color": "purple",
        "element": "air",
        "effect": "calms the mind and enhances intuition"
    },
    "obsidian": {
        "chakra": "root",
        "color": "black",
        "element": "earth",
        "effect": "blocks negativity and grounds your energy"
    },
    "citrine": {
        "chakra": "solar plexus",
        "color": "yellow",
        "element": "fire",
        "effect": "boosts confidence and attracts abundance"
    },
    "fluorite": {
        "chakra": "third eye",
        "color": "green",
        "element": "air",
        "effect": "enhances focus and clears mental fog"
    },
    "carnelian": {
        "chakra": "sacral",
        "color": "orange",
        "element": "fire",
        "effect": "increases motivation and creativity"
    },
    "clear quartz": {
        "chakra": "all",
        "color": "clear",
        "element": "light",
        "effect": "amplifies intentions and energies"
    },
    "lapis lazuli": {
        "chakra": "throat",
        "color": "deep blue",
        "element": "water",
        "effect": "encourages truth and communication"
    }
}

save_codex(starter_codex)
print("💎 Codex has been seeded with sacred stones!")

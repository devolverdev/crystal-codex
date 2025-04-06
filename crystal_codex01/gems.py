def recommend_crystal(mood):
    crystals = {
        "sad": "rose quartz",
        "tired": "carnelian",
        "ok": "amethyst"
    }
    return crystals.get(mood, "clear quartz")

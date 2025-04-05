### Dictionaries & Data Mapping


crystals = {
    "sad": "rose quartz",
    "tired": "carnelian",
    "ok": "amethyst",
    "happy": "fluorite",
    "joyful": "citrine"
}


mood = input("How do you feel at this moment in time? ").lower()

chosen = crystals.get(mood, "clear quartz")

if chosen == "clear quartz":
    print("💭 I sensed something unique... clear quartz brings clarity.")

print("🔮 Based on your energy, your crystal is:", chosen)




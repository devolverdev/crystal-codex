from crystal_codex.file_writer import load_codex, save_codex

codex = load_codex()  # ✅ This now loads from codex.json


mood = input("💫 How are you feeling today? ").lower()
affirmation = input("🌈 What’s your affirmation for today? ")

# Look up a matching crystal
crystal = codex.get(mood, {
    "element": "spirit",
    "chakra": "all",
    "color": "clear",
    "healing": "universal amplifier"
})

print("🔮 Your matched crystal:")
print("   💎", mood.title())
print("   🎨", crystal["color"])
print("   🌀", crystal["chakra"])
print("   🌿", crystal["healing"])

# Optional: Save new entries
add = input("Would you like to add a new crystal to the codex? (y/n) ")
if add == "y":
    name = input("Name of the crystal: ").lower()
    chakra = input("Chakra: ")
    color = input("Color: ")
    element = input("Element: ")
    healing = input("Healing properties: ")

    codex[name] = {
        "chakra": chakra,
        "color": color,
        "element": element,
        "effect": healing
    }

    save_codex(codex)  # 🧠 ← THIS saves it back to codex.json


    print(f"✅ Added {name.title()} to your codex!")

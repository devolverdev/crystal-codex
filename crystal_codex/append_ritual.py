from datetime import datetime  # ⏳ Time spell unlocked!
from crystal_codex.file_writer import (
    update_crystal,
    delete_crystal,
    save_codex,
    load_codex
)

# === Crystal Updates ===
def update_codex_entries():
    codex = load_codex()

    # Delete a crystal
    delete_crystal(codex, "Obsidian")

    # Update crystal effect
    update_crystal(codex, "Amethyst", "effect", "spiritual protection")

    # Save changes
    save_codex(codex)

# === Daily Ritual Journal ===
def write_daily_ritual():
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M")

    entry = input("✨ What are you grateful for today? ")
    entry2 = input("🌙 What's your mood crystal? ")

    # Start journal entry
    with open("myrituals.txt", "w") as journal:
        journal.write(f"\n📅 {timestamp}\n")
        journal.write("🔮 My Daily Log Entry:\n")
        journal.write("🙏 Gratitude: " + entry + "\n")
        journal.write("💎 Mood Crystal: " + entry2 + "\n")

    # Add ritual and affirmation
    gem = input("🔔 Which ritual are you using? ")
    affirmation = input("📣 What affirmation are you focusing on? ")

    with open("myrituals.txt", "a") as file:
        file.write(f"🌕 Ritual: {gem.title()} — ✨ {affirmation}\n")
        file.write("🌌───────────────────────\n")  # cute divider

    print("📖 Your ritual has been written to the sacred journal!")

    # Show full journal content
    print("\n🌠 Here’s what your journal says:")
    with open("myrituals.txt", "r") as journal:
        print(journal.read())

# === Optional Test Data Injection ===
def add_test_data():
    test_data = {
        "fluorite": {
            "chakra": "third eye",
            "color": "green",
            "element": "air",
            "effect": "focus and clarity"
        }
    }
    codex = load_codex()
    codex.update(test_data)
    save_codex(codex)
    print("🧪 Test crystal added:")
    print(codex)

# === Run if standalone ===
if __name__ == "__main__":
    update_codex_entries()
    write_daily_ritual()
    add_test_data()

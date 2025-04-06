# crystal_codex/09_FileHandling.py

from datetime import datetime
from crystal_codex.file_writer import (
    save_codex,
    load_codex,
    update_crystal,
    delete_crystal,
    backup_codex,
    restore_codex
)

# === 1. Codex Modifications ===
def modify_crystals():
    codex = load_codex()
    delete_crystal(codex, "Obsidian")
    update_crystal(codex, "Amethyst", "effect", "spiritual protection")
    save_codex(codex)

# === 2. Backup & Restore ===
def handle_backups():
    codex = load_codex()
    backup_codex(codex)
    restored = restore_codex()
    print("🧬 Restored Codex:")
    print(restored)

# === 3. Ritual Logging to TXT ===
def write_ritual_journal():
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M")

    gratitude = input("✨ What are you grateful for today? ")
    mood_crystal = input("🌙 What's your mood crystal? ")

    with open("myrituals.txt", "w") as journal:
        journal.write(f"\n📅 {timestamp}\n")
        journal.write("🔮 My Daily Log Entry:\n")
        journal.write(f"🙏 Gratitude: {gratitude}\n")
        journal.write(f"💎 Mood Crystal: {mood_crystal}\n")

    ritual = input("🔔 Which ritual are you using? ")
    affirmation = input("📣 What affirmation are you focusing on? ")

    with open("myrituals.txt", "a") as journal:
        journal.write(f"🌕 Ritual: {ritual.title()} — ✨ {affirmation}\n")
        journal.write("🌌───────────────────────\n")

    print("📖 Your ritual has been written to the sacred journal!")

    print("\n🌠 Journal contents:")
    with open("myrituals.txt", "r") as journal:
        print(journal.read())

# === 4. Optional: Add New Crystal (test injection) ===
def add_test_crystal():
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
    print("🧪 Fluorite added to codex.")

# === Run All if Called Directly ===
if __name__ == "__main__":
    modify_crystals()
    handle_backups()
    write_ritual_journal()
    add_test_crystal()

import json
import os

print("📁 Running from:", os.getcwd())

def save_codex(data, filename="codex.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print(f"💾 Codex saved to {filename}!")

def load_codex(filename="codex.json"):
    with open(filename, "r") as file:
        return json.load(file)

def update_crystal(codex, name, field, new_value):
    if name in codex:
        codex[name][field] = new_value
        print(f"✅ {name}'s {field} updated to: {new_value}")
    else:
        print("❌ Crystal not found.")

def delete_crystal(codex, name):
    if name in codex:
        del codex[name]
        print(f"🗑️ Crystal '{name}' has been removed.")
    else:
        print("⚠️ Crystal not found.")

def backup_codex(data, filename="codex_backup.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print(f"📦 Backup saved to {filename}!")

def restore_codex(filename="codex_backup.json"):
    with open(filename, "r") as file:
        return json.load(file)

# Optional test runner
if __name__ == "__main__":
    # 🔬 Optional: Run only if executing this file directly

    test_data = {
        "fluorite": {
            "chakra": "third eye",
            "color": "green",
            "element": "air",
            "effect": "focus and clarity"
        }
    }

    # Load → Update → Save
    codex = load_codex()
    codex.update(test_data)
    save_codex(codex)

    # Backup and restore
    backup_codex(codex)
    restored = restore_codex()
    
    print("🧬 Restored Codex:")
    print(restored)

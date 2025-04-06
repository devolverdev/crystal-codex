from crystal_codex.file_writer import load_codex, save_codex

codex = load_codex()

for name, data in codex.items():
    if "effect" not in data:
        data["effect"] = "✨ energy unknown – add me!"
        print(f"⚠️ Added default effect to: {name}")

save_codex(codex)
print("✅ Patch complete. All crystals now have an 'effect'.")

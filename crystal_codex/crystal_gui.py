import tkinter as tk
from tkinter import messagebox
import random
from crystal_codex.file_writer import load_codex

# 🧠 Mood to Crystal Mapping
mood_map = {
    "sad": "rose quartz",
    "anxious": "amethyst",
    "tired": "carnelian",
    "confused": "fluorite",
    "happy": "citrine",
    "strong": "tiger's eye",
    "peaceful": "clear quartz",
    "joyful": "citrine",
    "creative": "carnelian"
}

# 🌿 Load Crystal Codex
codex = load_codex()

# Validate 'effect' field presence
for name, info in codex.items():
    if "effect" not in info:
        print(f"⚠️ {name} is missing an 'effect' field!")

# ✨ Affirmation Generator
def get_affirmation():
    affirmations = [
        "I am grounded and glowing.",
        "Each breath brings me balance.",
        "Clarity flows through me today.",
        "I trust my intuition and path.",
        "Healing happens in beautiful layers."
    ]
    return random.choice(affirmations)

# 📝 Ritual Logging
def log_to_journal():
    mood = mood_var.get()
    crystal_name = mood_map.get(mood)
    crystal = codex.get(crystal_name, {})
    affirmation = affirm_label.cget("text").replace("🌟 Affirmation: ", "")

    with open("myrituals_gui.txt", "a") as journal:
        journal.write(f"\n🧘 Mood: {mood}\n")
        journal.write(f"💎 Crystal: {crystal_name}\n")
        journal.write(f"🌟 Affirmation: {affirmation}\n")
        journal.write("🌌 ───────────────────────\n")

    messagebox.showinfo("Ritual Logged", "📖 Your ritual has been logged to the journal!")

# 🔍 Crystal Search
def search_crystal():
    mood = mood_var.get()
    crystal_name = mood_map.get(mood)
    crystal = codex.get(crystal_name)

    if crystal:
        text = f"🔮 Mood: {mood.title()}\n"
        text += f"💎 Crystal: {crystal_name.title()}\n"
        text += f"🧘 Chakra: {crystal['chakra']}\n"
        text += f"🎨 Color: {crystal['color']}\n"
        text += f"🌬️ Element: {crystal['element']}\n"
        text += f"✨ Effect: {crystal.get('effect', 'Unknown')}"
    else:
        text = f"😔 No crystal found for mood: {mood}"

    result_label.config(text=text)
    affirmation = get_affirmation()
    affirm_label.config(text=f"🌟 Affirmation: {affirmation}")

# 🌈 GUI Setup
BG = "#faf3f3"
FG = "#5a4e7c"
FONT = ("Georgia", 12)

root = tk.Tk()
root.title("Crystal Codex GUI ✨")
root.configure(bg=BG)
root.geometry("450x450")

tk.Label(root, text="How do you feel today?", bg=BG, fg=FG, font=FONT).pack(pady=10)

mood_var = tk.StringVar()
mood_var.set("happy")  # Default mood

mood_options = list(mood_map.keys())
dropdown = tk.OptionMenu(root, mood_var, *mood_options)
dropdown.config(bg="#e0d4f7", font=FONT)
dropdown.pack()

tk.Button(root, text="🔍 Find My Crystal", command=search_crystal, bg="#e0d4f7", font=FONT).pack(pady=10)

result_label = tk.Label(root, text="", bg=BG, fg=FG, font=FONT, wraplength=380, justify="left")
result_label.pack(pady=10)

affirm_label = tk.Label(root, text="🌟 Affirmation: ", bg=BG, fg=FG, font=FONT, wraplength=360)
affirm_label.pack(pady=5)

tk.Button(root, text="📓 Log This Ritual", command=log_to_journal, bg="#f9e6ff", font=FONT).pack(pady=5)

root.mainloop()

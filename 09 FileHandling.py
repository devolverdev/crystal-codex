from datetime import datetime  # ⏳ Time spell unlocked!

# Get current date and time
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M")

# Prompt the user
entry = input("✨ What are you grateful for today? ")
entry2 = input("🌙 What's your mood crystal? ")

# Write the first entry with timestamp
with open("myrituals.txt", "w") as journal:
    journal.write(f"\n📅 {timestamp}\n")
    journal.write("🔮 My Daily Log Entry:\n")
    journal.write("🙏 Gratitude: " + entry + "\n")
    journal.write("💎 Mood Crystal: " + entry2 + "\n")

# Ritual + affirmation
gem = input("🔔 Which ritual are you using? ")
affirmation = input("📣 What affirmation are you focusing on? ")

# Append the ritual
with open("myrituals.txt", "a") as file:
    file.write(f"🌕 Ritual: {gem.title()} — ✨ {affirmation}\n")
    file.write("🌌───────────────────────\n")  # just a cute divider

print("📖 Your ritual has been written to the sacred journal!")


print("\n🌠 Here’s what your journal says:")

with open("myrituals.txt", "r") as journal:
    print(journal.read())

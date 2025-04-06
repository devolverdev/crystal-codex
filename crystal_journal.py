# crystal_journal.py

entry = input("✨ What's your crystal ritual today? ")

with open("journal.txt", "w") as journal:
    journal.write("🔮 Crystal Log Entry:\n")
    journal.write(entry + "\n")

print("📖 Your ritual has been written to the crystal journal.")

####

entry = input("🌙 What's your intention today? ")

with open("journal.txt", "a") as journal:
    journal.write("🌕 New Moon Intention:\n")
    journal.write(entry + "\n\n")

print("💫 Intention added to your sacred journal.")


####

gem = input("Which crystal are you using? ")
affirmation = input("What affirmation are you focusing on? ")

with open("journal.txt", "a") as file:
    file.write(f"💎 {gem.title()} - ✨ {affirmation}\n")

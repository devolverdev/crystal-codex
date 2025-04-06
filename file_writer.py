# file_writer.py ✨

entry = input("✨ What are you grateful for today? ")

with open("gratitude_journal.txt", "w") as file:
    file.write("💫 My Gratitude Entry\n")
    file.write(entry + "\n")

print("✅ Your entry was saved.")


# append_ritual.py 🌀

ritual = input("🌙 Add a moon ritual for tonight: ")

with open("gratitude_journal.txt", "a") as file:
    file.write("🌕 Ritual:\n")
    file.write(ritual + "\n")

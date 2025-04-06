from datetime import datetime

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def log_ritual(mood, crystal, affirmation):
    with open("crystal_journal.txt", "a") as file:
        file.write(f"🌿 Mood: {mood}\n")
        file.write(f"✨ Intention: {affirmation}\n")
        file.write(f"💎 Crystal: {crystal}\n")
        file.write(f"🕒 Time: {get_timestamp()}\n")
        file.write("-" * 30 + "\n")

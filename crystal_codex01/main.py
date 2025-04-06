from gems import recommend_crystal
from rituals import log_ritual

mood = input("💫 How are you feeling today? ").lower()
affirmation = input("🌈 Your affirmation for today: ")

chosen = recommend_crystal(mood)
log_ritual(mood, chosen, affirmation)

print("🌟 Ritual saved successfully!")



'''
┌──────────────────────┐
│      main.py         │ ◀────────────┐
│ (central control)    │              │
└──────────────────────┘              │
      │      │                        │
      ▼      ▼                        │
┌────────┐ ┌────────────┐             │
│ gems.py│ │ rituals.py │             │
│  💎    │ │  📜        │             │
└────────┘ └────────────┘             │
   │            │                    │
   ▼            ▼                    │
Recommend  →  Log rituals        Reads/writes
Crystal       to journal file   from: crystal_journal.txt
based on       with timestamp   ────────────────────────▶ 🗒️
mood input                     (append entries)
   ▲            ▲
   │            │
┌────────────┐  │
│ utils.py   │  │
│ 🛠️ timestamp│◀─┘
└────────────┘




🧠 What Each File Does


    File/	Purpose	/ Who Calls It
    
main.py	/Gets user input and controls flow	//You run this
gems.py	/Matches mood ➡ crystal	/Called by main.py
rituals.py	/Writes entry to a text file	/Called by main.py
utils.py	/Provides current time	/Used by rituals.py
crystal_journal.txt	/Final output file	/Updated via rituals.py

'''
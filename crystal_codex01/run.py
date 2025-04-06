# run.py

from crystal_codex01.rituals import log_ritual
from crystal_codex01.gems import recommend_crystal
from crystal_codex01.utils import get_timestamp

print("🌞 Welcome to your Crystal Ritual Companion")

mood = input("How do you feel today? ").lower()
affirmation = input("What’s your affirmation or intention? ")

crystal = recommend_crystal(mood)
log_ritual(mood, crystal, affirmation)

print("🪄 Your ritual has been recorded at:", get_timestamp())
print("💎 Crystal Selected:", crystal.title())

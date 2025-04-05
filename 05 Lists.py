crystals = ["amethyst", "rose quartz", "obsidian"]
# Accessing items
print(crystals[0])         # amethyst

# Adding an item
crystals.append("fluorite")

# Loop through the list
for stone in crystals:
    print("🔮", stone)


###


pouch = []

mood = input("How do you feel? ")

if mood == "sad":
    pouch.append("rose quartz")
elif mood == "tired":
    pouch.append("carnelian")
elif mood == "": 
    pouch.append("example")

print("Your healing pouch contains:", pouch)


### LOOP VARIABLE

crystals = ["amethyst", "rose quartz", "obsidian"]

for stone in crystals:
    print("Right now, stone is:", stone)



####

for crystal in crystals:
    print("🔮", crystal)

for item in crystals:
    print("✨", item)

for x in crystals:
    print("💎", x)


####

crystals = ["amethyst", "rose quartz", "obsidian"]

for stone in crystals:
    if stone == "rose quartz":
        print("💗", stone, "– Heart healer")
    else:
        print("🔮", stone)


print("💎 Your crystal today is:", crystals[1])

###

crystals = ["amethyst", "rose quartz", "obsidian"]

for stone in crystals:
    print("💎 Your crystal today is:", stone[0])


### CHALLENGE 3
crystals = ["rose quartz", "carnelian", "obsidian"]

pouch = []

mood = input("How do you feel? ").lower()

if mood == "sad":
    pouch.append("rose quartz")
elif mood == "tired":
    pouch.append("carnelian")
elif mood == "": 
    pouch.append("obsidian")

else:
    print("🧘‍♀️ No crystal added today. Take a deep breath.")


print("Your healing pouch contains:", pouch)


#######


import random

crystals = ["amethyst", "rose quartz", "citrine", "obsidian", "fluorite"]
affirmations = [
    "You are grounded and radiant.",
    "Your energy is protected and loved.",
    "You shine with clarity and purpose.",
    "You are aligned with your higher self.",
    "You bring peace to all you meet."
]
emojis = ["💎", "🌸", "🔮", "🌞", "🦋", "✨"]

chosen_crystal = random.choice(crystals)
chosen_affirmation = random.choice(affirmations)
chosen_emoji = random.choice(emojis)

print(f"{chosen_emoji} Today’s crystal is: {chosen_crystal}")
print(f"{chosen_emoji} Affirmation: {chosen_affirmation}")


###

gems = ["amber", "tigers eye", "obsidian"]
pouch = []

for i in range(3):
    mood = input("How do you feel? ").lower()

    if mood == "ok":
        print("💛 Adding amber")
        pouch.append("amber")
        print("You typed:", mood)
    elif mood == "strong":
        print("🐯 Adding tiger's eye")
        pouch.append("tigers eye")
        print("You typed:", mood)
    elif mood == "sad": 
        print("🖤 Adding obsidian")
        pouch.append("obsidian")
        print("You typed:", mood)
    else:
        print("🧘‍♀️ No crystal added today. Take a deep breath.")


print("👜 Your healing pouch contains:", pouch)

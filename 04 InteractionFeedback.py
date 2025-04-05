### Interaction & Feedback


### Inputs

name = input("What is your name? ")
print("Nice to meet you, " + name + "!")



####

name = input("What's your name? ")
mood = input("How are you feeling today? ")

print("Hi " + name + ", glad you're feeling " + mood + "!")



####


age = input("How old are you? ")
age = int(age)

if age < 18:
    print("You’re a young explorer!")
else:
    print("Wisdom mode: activated.")



#####


num = input("Give me a number: ")
num = int(num)
print("Doubled:", num * 2)


###

mood = input("How do you feel today? (happy/sad/ok): ")

if mood == "happy":
    print("🌞 Shine on, BRU!")
elif mood == "sad":
    print("🌧️ It's okay, storms pass.")
else:
    print("🌿 May your day be peaceful.")



####


hungry = input("Are you hungry? (yes/no): ")
tired = input("Are you tired? (yes/no): ")

if hungry == "yes" and tired == "yes":
    print("🍜 Eat something and nap!")
elif hungry == "yes" or tired == "yes":
    print("Take care of yourself.")
else:
    print("You’re good to go! 🚀")


### FIRST CRISTAL EXERCISE




# %%
purpose = input("What do you seek today? (healing/protection/clarity): ").lower()
emotion = input("How do you feel today? (anxious/drained/peaceful): ").lower()
chakra = input("Which chakra are you focusing on? (heart/root/crown): ").lower()

if purpose == "protection" and emotion == "anxious":
    print("Black Tourmaline is calling to you. Ground yourself and shield your energy.")
elif chakra == "heart" and emotion == "drained":
    print("Rose Quartz will help you recharge your heart space with love.")
elif purpose == "clarity" and chakra == "crown":
    print("Clear Quartz brings the mental clarity and amplification you need.")
else:
    print("Labradorite may guide you with intuition through this moment.")

import random

options = [
    "✨ Trust the process.",
    "💫 You are on the right path.",
    "🌙 Let stillness speak for you."
]

print(random.choice(options))


### OR :


# %%

def crystal_advice(purpose, emotion, chakra):
    if purpose == "protection" and emotion == "anxious":
        return "Black Tourmaline is calling to you."
    elif chakra == "heart" and emotion == "drained":
        return "Rose Quartz will recharge your heart."
    elif purpose == "clarity" and chakra == "crown":
        return "Clear Quartz brings clarity and focus."
    else:
        return "Labradorite may guide you."

# Later you call it:
print(crystal_advice(purpose, emotion, chakra))




##### 


password = ""

while password != "moonlight":
    password = input("Enter the secret word: ")

print("✨ Welcome, BRU. The circle is open.")


####


crystal = ""

while crystal != "amethyst":
    crystal = input("Name the guardian crystal: ")

print("🔮 The gateway opens to your vision.")



#####


#%

import time

print("🔮 Sensing your aura...")
time.sleep(1.5)

print("💎 Channeling your energy through Clear Quartz...")
time.sleep(2)

print("🌙 A vision appears:")
time.sleep(1)
print()
print("      ✨      ")
time.sleep(0.5)
print("     ✨✨     ")
time.sleep(0.5)
print("    ✨👁️✨    ")
time.sleep(0.5)
print("     ✨✨     ")
time.sleep(0.5)
print("      ✨      ")
time.sleep(1)

print()
print("📜 Message: You already hold the key to your own clarity.")

#%



#####


def show_vision(message):
    print("🌌 Opening the vision...")
    time.sleep(1.5)
    print()
    print("     ✨✨✨")
    time.sleep(0.3)
    print("    ✨👁️✨")
    time.sleep(0.3)
    print("     ✨✨✨")
    time.sleep(1)
    print()
    print("📜 Message:", message)


show_vision("Labradorite protects your journey today.")

###





###

mood = input("How do you feel today? (happy/drained/focused): ").lower() 

if mood == "happy":
    print("Go charge your stones outside!")
elif mood == "sad":
    print("Hold your Obsidian.")
else:
    print(" May your day be peaceful.")


    ###
if mood == "happy":
    print("Go charge your stones outside!")
elif mood == "drained":
    print("Hold your Obsidian.")
elif mood == "focused":
    print("Use your Fluorite to stay sharp.")
else:
    print("🌿 May your day be peaceful.")


###


while True:
    mood = input("How do you feel today? (happy/drained/focused or type 'exit'): ").lower()
    
    if mood == "exit":
        break
    elif mood == "happy":
        print("Go charge your stones outside!")
    elif mood == "drained":
        print("Hold your Obsidian.")
    elif mood == "focused":
        print("Use your Fluorite to stay sharp.")
    else:
        print("🌿 May your day be peaceful.")


###
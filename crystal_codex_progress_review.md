
# 🌈 Crystal Codex – Python Progress Review

This document reviews the modules BRU has completed so far in the Crystal Codex journey. Each module includes a concept summary and a hands-on exercise for reinforcement.

---

## ✅ 01 – Propositions & Logic
**Concept:** Logical operators like `and`, `or`, `not`.

**Exercise:**  
Write a program that takes in two boolean inputs (True/False) about your energy and focus, and suggests a ritual.

```python
energy = input("Do you feel energetic? (yes/no): ").lower() == "yes"
focus = input("Do you feel focused? (yes/no): ").lower() == "yes"

if energy and focus:
    print("🧘 You’re ready for a high-focus ritual with citrine.")
elif not energy and focus:
    print("💤 Restorative breathwork and amethyst recommended.")
else:
    print("🌿 Ground with smoky quartz first.")
```

---

## ✅ 02 – Variables
**Concept:** Store and label dynamic input from the user.

**Exercise:**  
Ask the user their mood and store it in a variable, then use it.

```python
mood = input("What's your mood today? ")
print("💫 Storing mood as:", mood)
```

---

## ✅ 03 – Functions
**Concept:** Reusable logic using `def`.

**Exercise:**
Create a function that takes a mood and returns a matching crystal.

```python
def get_crystal(mood):
    if mood == "tired":
        return "carnelian"
    elif mood == "sad":
        return "rose quartz"
    else:
        return "clear quartz"

print("🔮 Your crystal is:", get_crystal(input("How do you feel? ")))
```

---

## ✅ 04 – Interaction & Feedback
**Concept:** Use `input()` and return suggestions based on it.

**Exercise:**
Create a crystal matcher that uses multiple conditions.

```python
mood = input("How do you feel? ").lower()
if mood in ["happy", "joyful"]:
    print("✨ Fluorite to amplify joy!")
else:
    print("🪨 Obsidian to support you today.")
```

---

## ✅ 05 – Lists
**Concept:** Store and iterate through groups of crystals.

**Exercise:**
Loop through a list and print each item with an emoji.

```python
crystals = ["amethyst", "rose quartz", "obsidian"]
for gem in crystals:
    print("🔮", gem.title())
```

---

## ✅ 06 – Dictionaries
**Concept:** Key-value pair storage and retrieval.

**Exercise:**
Look up a crystal based on a user-supplied keyword.

```python
codex = {
    "amethyst": "clarity",
    "citrine": "joy",
    "obsidian": "protection"
}

gem = input("Which gem are you drawn to? ")
print("🌟 Its effect is:", codex.get(gem, "unknown crystal"))
```

---

## ✅ 07 – Nested Dictionaries
**Concept:** Multi-layered meaning and properties.

**Exercise:**
Access multiple pieces of data from a nested structure.

```python
gems = {
    "rose quartz": {"chakra": "heart", "color": "pink"},
    "amethyst": {"chakra": "crown", "color": "purple"}
}

choice = input("Choose your crystal: ").lower()
info = gems.get(choice, {})
print("💎 Info:", info.get("chakra", "unknown"), "-", info.get("color", "unknown"))
```

---

## ✅ 08 – Loops + Conditions
**Concept:** Iterate over structured data and apply logic.

**Exercise:**
Print crystals that match a chakra keyword.

```python
crystals = {
    "rose quartz": {"chakra": "heart"},
    "amethyst": {"chakra": "crown"},
    "carnelian": {"chakra": "sacral"}
}

focus = input("Which chakra are you balancing? ").lower()

for gem, info in crystals.items():
    if info["chakra"] == focus:
        print("🔮", gem)
```

---

You’re doing amazing, BRU! 🌟 Let’s keep going strong.

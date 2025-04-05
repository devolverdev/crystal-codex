#LEARNING PYTHON#


#1 PROPOSITIONS

drank_coffee = True
napolitana_eating = True
joint_burning = False

#2 NEGATION ¬P

is_raining = True
print(not is_raining)   # Output: False

is_hungry = False
print(not is_hungry)  


# %%
print('que linda brunilda today')

## EXAMPLES

# %%
# Some propositions
sunny = False
warm = True

# Negation
print("Is it NOT sunny?", not sunny)

# Logical AND
print("Is it sunny AND warm?", sunny and warm)

# Logical OR
print("Is it sunny OR warm?", sunny or warm)

# Combined expression
print("Is it NOT sunny AND warm?", not sunny and warm)

# %%

## EXAMPLE 2 - Conjunction (∧) — “AND”

sunny = True
has_energy = True

if sunny and has_energy:
    print("Go hiking")
else:
    print("Stay home")
# %%

## EXAMPLE 3 - Disjunction (∨) — “OR”

tired = False
bored = False

if tired or bored:
    print("Watch a movie")
else:
    print("Go out for a walk")

## EXAMPLE 4 - Implication (→) — “IF...THEN”

has_homework = True
studied = False

if has_homework:
    if studied:
        print("Commitment kept")
    else:
        print("Y bue")


## EXAMPLE 5 - Biconditional (↔) — “IFF” (If and only if)

sunny = True
go_outside = True

if sunny == go_outside:
    print("Biconditional holds")
else:
    print("Mismatch in logic")



# 🧠 Level 2 – Functions in Python  
 
## ✅ What Is a Function?


### 💡 Real-Life Analogy:



 

## 📦 Python Syntax

 
def greet():
    print("Que Onda!") 

greet()


## 🎛️ Functions With Input

##You can give a function **parameters** — values it needs to do its job:


def greet(name):
    print("Hi", name)


##Calling:

greet("Bruna")






## 🔁 Functions With Loops Inside

##You can mix what you know:


def countdown(n):
    for i in range(n, 0, -1):  # counts backwards
        print(i, "Mississippi")
    print("Time’s up!")
    print("Se termino!")


##Call it:

countdown(5)

## 🎯 Functions That Give Back Results (Return)


def add(x, y):
    return x + y

sum = add(3, 5)
print("Result:", sum)

###
def make_soup(ingredient1, ingredient2):
    return ingredient1 + " con " + ingredient2 + " tipo sopita"

my_lunch = make_soup("ramencito", "ajitama")
print(my_lunch)

###


def mifunc(a,b):
    return a + b

variable = mifunc("hola"," perra")

print(variable)



###

def shout(word):
    return word.upper() + "!!!"

print(shout("awanta"))        # calls the function
print(shout)                 # just prints info *about* the function

###


## 🧪 Function Practice Exercises


def greet_user(name, age):
    message = "Hello, " + name + "! You are " + str(age) + " years old."
    return message

# simulate filling out the form
user_name = "Bruna"
user_age = 38

response = greet_user(user_name, user_age)
print(response)

####

def age_comment(name, age):
    if age < 48:
        return "👶 " + name + ", you're quite young!"
    elif age < 60:
        return "🔥 " + name + ", you’re just getting started!"
    else:
        return "🌟 " + name + ", your wisdom shines!"

# Fill-in
user_name = "BRU"
user_age = 38

print(age_comment(user_name, user_age))

### TYPE CONVERSION TO STRING

age = 31
print("My age is " + str(age))

pi = 3.14
print("Pi is about " + str(pi))


###

# Start with a number
num = 10

# Convert to string
text = str(num)
print("This is now text:", text)

# Convert text back to number
back_to_num = int(text)
print("Back to number:", back_to_num)

# Now try math
print(back_to_num + 5)



### 🔧 Exercise 1: Define & Call


def say_hello():
    print("Good morning!")


##Then call: `say_hello()`



### 🎛 Exercise 2: Function with a parameter


def announce_weather(weather):
    print("Today is", weather)


## Call it with `"sunny"`, `"cloudy"`, etc.


### 🔁 Exercise 3: Loop inside function


def blink(times):
    for i in range(times):
        print("💡 Blink", i + 1)


print (blink(2))
 

### ➕ Exercise 4: Return result


def square(n):
    return n * n


###

print("9 squared is", square(9))



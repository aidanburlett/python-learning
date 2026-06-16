# ---------------------------------------
# VARIABLES
# ---------------------------------------

# Variables store data in memory.
name = "Aidan"
age = 18
height = 5.9
is_student = True

print(name)
print(age)
print(height)
print(is_student)


# ---------------------------------------
# STRINGS
# ---------------------------------------

greeting = "Hello, world!"

# Concatenation
message = greeting + " My name is " + name
print(message)

# f-strings (recommended)
better_message = f"My name is {name} and I am {age} years old."
print(better_message)

# String methods
print(greeting.upper())
print(greeting.lower())
print(len(greeting))


# ---------------------------------------
# INTEGERS
# ---------------------------------------

x = 10
y = 3

print(x + y)
print(x - y)
print(x * y)
print(x // y)  # integer division
print(x % y)   # remainder


# ---------------------------------------
# FLOATS
# ---------------------------------------

a = 3.14
b = 2.5

print(a + b)
print(a * b)
print(a / b)


# ---------------------------------------
# BOOLEANS
# ---------------------------------------

is_tall = True
is_short = False

print(is_tall)
print(is_short)

# Boolean expressions
print(5 > 2)
print(10 == 10)
print(3 != 4)


# ---------------------------------------
# IF / ELSE
# ---------------------------------------

temperature = 75

if temperature > 80:
    print("It's hot outside.")
elif temperature > 60:
    print("It's warm outside.")
else:
    print("It's cold outside.")


# ---------------------------------------
# FOR LOOPS
# ---------------------------------------

# Loop through a range of numbers
for i in range(5):
    print(f"Loop number: {i}")

# Loop through a list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")


# ---------------------------------------
# WHILE LOOPS
# ---------------------------------------

count = 0

while count < 3:
    print(f"Count is {count}")
    count += 1


# ---------------------------------------
# PRINT STATEMENTS
# ---------------------------------------

print("This is a print statement.")
print("You can print numbers:", 123)
print("You can print multiple things:", name, age, is_student)


# ---------------------------------------
# INPUT() EXAMPLES
# ---------------------------------------

# Uncomment these lines if you want to test input()

# user_name = input("What is your name? ")
# print(f"Hello, {user_name}!")

# user_age = input("How old are you? ")
# print(f"You are {user_age} years old.")

# number = int(input("Enter a number: "))
# print(f"Your number times 2 is {number * 2}")

# Function with parameters
def paramtersFunction(par1, par2):
  print(f"You selected {par1} and {par2}.")

paramtersFunction(10, 20)

# Function returning values
def returnFunction(val1, val2):
  return val1 + val2

returnFunction(1, 2)

# List iteration
def print_animals(animals_list):
  for animal in animals_list:
    print(f"I like {animal}")

animals = ["dog", "cat", "bird"]
print_animals(animals)

# Dictionary iteration
def print_student_scores(scores):
  for name, score in scores.items():
    print(f"{name} scored {score}")

student_scores = {
  "Aidan": 95,
  "Sarah": 88,
  "Michael": 76
}

print_student_scores(student_scores)

# Script
# Ask user for 3 favorite tools
# Store in list
# Print them

def get_favorite_tools():
  tools = []

  for i in range(3):
    tool = input(f"Enter favorite tool #{i + 1}: ")
    tools.append(tool)

  print("\nYour favorite tools are:")
  for t in tools:
    print(f"- {t}")

get_favorite_tools()

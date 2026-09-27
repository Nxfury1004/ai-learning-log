# 3-1 Names: store a few friends' names, print each one
names = ["Priya", "Arjun", "Meera"]

for name in names:
    print(name)

# 3-2 Greetings: same list, but a personalized message per name
print()
for name in names:
    print(f"Hello, {name}, would you like to learn some Python today?")

transportation = ["car", "bike", "bus", "train"]
for vehicle in transportation:
    print(f"I would like to own a {vehicle}.")
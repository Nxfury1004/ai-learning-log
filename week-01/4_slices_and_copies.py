my_foods = ["charles", "martina", "michael", "florence", "eli"]
first_3 = my_foods[:3]
print("The first three items in the list are:")
for food in first_3:
    print(food)
middle_3 = my_foods[1:4]
print("\nThe middle three items in the list are:")
for food in middle_3:
    print(food)
last_3 = my_foods[-3:]
print("\nThe last three items in the list are:")
for food in last_3:
    print(food)
friend_foods = my_foods[:]
my_foods.append("cannoli")
friend_foods.append("ice cream")
print("\nMy favorite foods are:")
for food in my_foods:
    print(food)
print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)

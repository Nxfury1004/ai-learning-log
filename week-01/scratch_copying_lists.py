# the WRONG way to copy a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods          # this does NOT make a copy!

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("my_foods:", my_foods)
print("friend_foods:", friend_foods)
print("same object?", my_foods is friend_foods)

print("\n--- the RIGHT way ---")
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]        # a full slice -- builds a real new list

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("my_foods:", my_foods)
print("friend_foods:", friend_foods)
print("same object?", my_foods is friend_foods)

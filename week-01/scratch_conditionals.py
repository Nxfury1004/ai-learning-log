car = 'bmw'
print(car == 'bmw')        # equality: True
print(car == 'audi')       # equality: False

print('Audi'.lower() == 'audi')   # case-insensitive comparison

print(car != 'audi')       # inequality: True

age = 19
print(age < 21, age <= 21, age > 21, age >= 21)

age_0, age_1 = 22, 18
print(age_0 >= 21 and age_1 >= 21)   # both must be true -> False
print(age_0 >= 21 or age_1 >= 21)    # either true -> True

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)     # True
print('pepperoni' in requested_toppings)     # False

banned_users = ['andrew', 'carolina', 'david']
print('marie' not in banned_users)           # True

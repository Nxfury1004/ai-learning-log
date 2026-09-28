# 1. a LIST of dicts -- e.g. a roster of aliens, each with its own attributes
aliens = [
    {'color': 'green', 'points': 5},
    {'color': 'yellow', 'points': 10},
    {'color': 'red', 'points': 15},
]
for alien in aliens:
    print(alien['color'], alien['points'])

print()

# 2. a DICT whose values are LISTS -- e.g. pizza toppings per person
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
for topping in pizza['toppings']:
    print("topping:", topping)

print()

# 3. a DICT of DICTS -- e.g. multiple users, keyed by username
users = {
    'aeinstein': {'first': 'albert', 'last': 'einstein', 'location': 'princeton'},
    'mcurie':    {'first': 'marie', 'last': 'curie', 'location': 'paris'},
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    print(f"  Full name: {user_info['first'].title()} {user_info['last'].title()}")
    print(f"  Location: {user_info['location'].title()}")

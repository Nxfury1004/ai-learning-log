foods = ('rice', 'dal', 'paneer', 'roti', 'salad')

print("The buffet offers:")
for food in foods:
    print(food)

# the menu changes -- this is fine, we're rebinding `foods` to a whole new tuple
foods = ('noodles', 'dal', 'paneer', 'soup', 'salad')

print("\nThe revised buffet offers:")
for food in foods:
    print(food)

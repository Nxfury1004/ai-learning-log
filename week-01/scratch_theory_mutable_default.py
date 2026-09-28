def add_item(item, basket=[]):   # DANGER: mutable default argument
    basket.append(item)
    return basket

cart1 = add_item("apple")
print("cart1:", cart1)

cart2 = add_item("banana")   # a supposedly fresh call, no basket given
print("cart2:", cart2)       # you'd expect just ['banana'] -- but watch:

print("same object?", cart1 is cart2)

print("\n--- the fix ---")

def add_item_fixed(item, basket=None):
    if basket is None:
        basket = []          # a brand new list, created fresh on THIS call
    basket.append(item)
    return basket

cart3 = add_item_fixed("apple")
cart4 = add_item_fixed("banana")
print("cart3:", cart3)
print("cart4:", cart4)
print("same object?", cart3 is cart4)

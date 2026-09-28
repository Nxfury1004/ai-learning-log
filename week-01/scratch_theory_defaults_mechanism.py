def add_item(item, basket=[]):
    basket.append(item)
    return basket

print("defaults tuple:", add_item.__defaults__)   # the actual default list object, visible

add_item("apple")
add_item("banana")

print("defaults tuple AFTER calls:", add_item.__defaults__)   # it MUTATED -- same object
print("id at start would match id now:", id(add_item.__defaults__[0]))

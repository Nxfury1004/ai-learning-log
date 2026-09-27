motorcycles = ['honda', 'yamaha', 'suzuki']

del motorcycles[0]
print("after del:", motorcycles)
# 'honda' is just gone now -- we never captured it anywhere

motorcycles = ['honda', 'yamaha', 'suzuki']
first = motorcycles.pop(0)
print("after pop:", motorcycles)
print("what we popped:", first)
# same removal, but 'honda' is still usable via `first`

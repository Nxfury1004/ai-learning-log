a = [1, 2, 3]
b = [1, 2, 3]      # a different list object, but same contents
c = a              # c is literally the same object as a (same label idea from ch.2)

print(a == b)   # True -- same contents
print(a is b)   # False -- two different objects in memory
print(a is c)   # True -- c and a point at the exact same object

# classic gotcha: small integers are cached/interned by CPython, so this can
# mislead you into thinking `is` works for value comparison. It doesn't --
# never rely on it for anything except None, and identity checks.
x = 256
y = 256
print(x is y)   # True on most Pythons (small int cache) -- but this is an
                 # implementation detail, NOT something to depend on

x = 257
y = 257
print(x is y)   # often False -- same value, but outside the cached range

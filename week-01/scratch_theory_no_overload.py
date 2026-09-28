def greet(name):
    print(f"Hello, {name}!")

def greet(name, greeting):   # this does NOT overload -- it replaces the function above
    print(f"{greeting}, {name}!")

greet("Om", "Hi")   # works
greet("Om")         # fails -- the single-arg version no longer exists at all

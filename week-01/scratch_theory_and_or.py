print(0 or "default")        # 0 is falsy -> evaluate and return the right side
print("hello" or "default")  # "hello" is truthy -> short-circuits, returns left side
print("hello" and "world")   # left is truthy -> keep going, return right side
print("" and "world")        # left is falsy -> short-circuits, returns left side ("")
print(3 and 5)                # both truthy -> returns the LAST evaluated operand: 5

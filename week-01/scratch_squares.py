# the "long" way
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print("loop version:", squares)

# same result, one line -- a list comprehension
squares_comp = [value**2 for value in range(1, 11)]
print("comprehension:", squares_comp)

# simple stats
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("min:", min(digits), "max:", max(digits), "sum:", sum(digits))

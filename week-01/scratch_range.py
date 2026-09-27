for value in range(1, 5):
    print(value)
print("---")

# range(1, 6) to actually include 5 -- range's second arg is exclusive
for value in range(1, 6):
    print(value)
print("---")

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))   # step of 2
print(even_numbers)

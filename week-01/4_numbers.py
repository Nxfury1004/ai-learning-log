print("Numbers from 1 to 20 are:")
for i  in range(1, 21):
    print(i)
print("Odd numbers between 1 and 20 are:")
for i in range(1, 21, 2):
    print(i)
print("Cubes of numbers from 1 to 10 are:")
for i in range(1, 11):
    print(i ** 3)
print("Cubes of numbers from 1 to 10 using list comprehension are:")
print([i ** 3 for i in range(1, 11)])
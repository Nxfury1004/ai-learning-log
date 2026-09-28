class Dog:
    def __init__(self, name):
        self.name = name

my_dog = Dog("Willie")
print(my_dog.__dict__)

my_dog.favorite_toy = "tennis ball"   # never declared in the class at all
print(my_dog.__dict__)
print(my_dog.favorite_toy)

# and it's PER-INSTANCE -- a second Dog doesn't get this attribute
other_dog = Dog("Lucy")
print(other_dog.__dict__)

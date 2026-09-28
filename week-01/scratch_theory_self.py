class Dog:
    def __init__(self, name):
        self.name = name

    def sit(self):
        print(f"{self.name} is now sitting.")

my_dog = Dog("Willie")

my_dog.sit()          # the normal way
Dog.sit(my_dog)        # EXACTLY equivalent -- this is what the sugar expands to

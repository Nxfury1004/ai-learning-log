class Animal:
    def speak(self):
        print("Animal.speak")

class Swimmer(Animal):
    def speak(self):
        print("Swimmer.speak")
        super().speak()

class Walker(Animal):
    def speak(self):
        print("Walker.speak")
        super().speak()

class Duck(Swimmer, Walker):
    def speak(self):
        print("Duck.speak")
        super().speak()

d = Duck()
d.speak()

print()
print("Method Resolution Order:")
for cls in Duck.__mro__:
    print(" ", cls.__name__)

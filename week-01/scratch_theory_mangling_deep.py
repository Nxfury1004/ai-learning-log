class Widget:
    def show_mangling(self):
        __local = "not even an attribute, just a local variable"
        print(locals())   # look at the ACTUAL name Python stored this under

w = Widget()
w.show_mangling()

print()

# mangling happens once, at class-definition time, regardless of inheritance depth
class Base:
    def __init__(self):
        self.__secret = "base's secret"

    def reveal_from_base(self):
        return self.__secret        # compiler rewrites this to self._Base__secret

class Derived(Base):
    def __init__(self):
        super().__init__()
        self.__secret = "derived's DIFFERENT secret"   # a totally separate slot!

    def reveal_from_derived(self):
        return self.__secret        # compiler rewrites this to self._Derived__secret

d = Derived()
print("base's view:", d.reveal_from_base())
print("derived's view:", d.reveal_from_derived())
print("both coexist:", d.__dict__)

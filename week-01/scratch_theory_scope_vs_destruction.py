import gc

class Resource:
    def __init__(self, name):
        self.name = name
        print(f"  [{name}] acquired")

    def __del__(self):
        print(f"  [{self.name}] destroyed")

def simple_case():
    r = Resource("simple")
    # r goes out of scope here; refcount drops to 0 -> CPython destroys it immediately

def cycle_case():
    a = Resource("cycle")
    a.self_ref = a   # the object now references itself: refcount can never reach 0
    # a goes out of scope here, but the object is still referenced by itself

print("simple_case():")
simple_case()
print("  (function returned)")

print("\ncycle_case():")
cycle_case()
print("  (function returned) <- notice: no 'destroyed' line yet")

print("\nforcing garbage collection:")
gc.collect()
print("  (gc.collect() done)")

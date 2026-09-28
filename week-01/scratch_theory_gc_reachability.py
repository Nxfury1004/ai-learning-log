import gc

class Node:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print(f"  [{self.name}] destroyed")

# 1. a live object: still referenced by a global name
alive = Node("alive")

# 2. a live object that is part of a cycle, but still reachable from a global
alive_cycle = Node("alive_cycle")
alive_cycle.me = alive_cycle

# 3. cyclic garbage: a cycle with no outside reference
def make_garbage():
    g = Node("garbage_cycle")
    g.me = g
make_garbage()

print("before gc.collect():")
found = gc.collect()
print(f"gc.collect() returned {found} (number of unreachable objects it found)")

print("\nafter gc.collect(), still alive:")
print("  alive       ->", alive.name)
print("  alive_cycle ->", alive_cycle.name)

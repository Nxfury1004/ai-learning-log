good = {(0, 0): "origin", (1, 1): "diagonal"}   # tuple keys: fine, tuples are immutable
print(good)

bad = {[0, 0]: "origin"}   # list keys: this will fail

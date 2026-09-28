d = {'a': 1, 'b': 2}
keys_view = d.keys()

print(type(keys_view))   # dict_keys, not list
print(keys_view)

d['c'] = 3   # mutate the dict AFTER grabbing the view
print(keys_view)   # the view already shows 'c' -- it's live, not a snapshot

# iterating a dict directly iterates its KEYS -- `for k in d` is shorthand for `for k in d.keys()`
for key in d:
    print("bare iteration gives key:", key)

# keys() behaves like a set (since keys must be unique) -- supports set algebra
d2 = {'b': 20, 'd': 4}
print("shared keys:", d.keys() & d2.keys())     # intersection
print("all keys:", d.keys() | d2.keys())        # union

# to get a real, independent snapshot, convert explicitly
snapshot = list(d.keys())
print(type(snapshot), snapshot)

def mutate(lst):
    lst.append(99)   # MUTATES the object the caller's variable points to

def rebind(lst):
    lst = [1, 2, 3]  # just moves the LOCAL label `lst` -- caller's variable untouched

original = [1, 2, 3]
mutate(original)
print("after mutate():", original)   # caller sees the change -- same object was modified

original = [1, 2, 3]
rebind(original)
print("after rebind():", original)   # caller sees NOTHING -- only the local label moved

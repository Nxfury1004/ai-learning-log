d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    if key == 'b':
        del d['b']   # mutating the dict while iterating its live view

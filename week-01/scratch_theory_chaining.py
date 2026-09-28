x = 5
print(1 < x < 10)     # Python: this means (1 < x) and (x < 10) -- True

# In C++, `1 < x < 10` would compile but mean ((1 < x) < 10):
# (1 < 5) evaluates to bool 'true' (i.e. 1), then `1 < 10` -> true.
# It "works" by accident there, but for a DIFFERENT reason, and breaks
# for other values -- e.g. in C++, `10 < x < 1` becomes (10<5)<1 -> 0<1 -> true(!)
# even though 10 < x < 1 should obviously be nonsense/false.
print(10 < x < 1)     # Python correctly says False: (10 < 5) is False, short-circuits

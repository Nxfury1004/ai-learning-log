print(-7 % 3)    # Python: 2  (result takes the sign of the DIVISOR)
print(7 % -3)    # Python: -2
# In C++, -7 % 3 gives -1 and 7 % -3 gives 1 (result takes the sign of the DIVIDEND).
# Python's % is defined via floor division; C++'s is defined via truncating division.
print(7 % 3)     # Python: 1
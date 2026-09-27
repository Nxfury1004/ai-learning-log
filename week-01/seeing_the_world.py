places = ["Tokyo", "Cairo", "Reykjavik", "Wellington", "Marrakesh"]

print("original list:", places)

print("\nsorted (alphabetical), original untouched:", sorted(places))
print("still original after sorted():", places)

print("\nsorted (reverse alphabetical), original untouched:", sorted(places, reverse=True))
print("still original after sorted():", places)

places.reverse()
print("\nafter reverse():", places)
places.reverse()
print("after reverse() again (back to original):", places)

places.sort()
print("\nafter sort() (permanent, alphabetical):", places)

places.sort(reverse=True)
print("after sort(reverse=True) (permanent, reverse alphabetical):", places)

guests = ["Ada Lovelace", "Alan Turing", "Grace Hopper"]

for guest in guests:
    print(f"Hi {guest}, you're invited to dinner!")

# 3-5: Alan can't make it -- swap him for someone else
print(f"\n{guests[1]} can't make it to dinner.")
guests[1] = "Margaret Hamilton"

print()
for guest in guests:
    print(f"Hi {guest}, you're invited to dinner!")

# 3-6: found a bigger table -- room for 3 more guests
print("\nGood news, I found a bigger table!")
guests.insert(0, "Katherine Johnson")     # new first guest
guests.insert(2, "Radia Perlman")         # new guest in the middle
guests.append("Hedy Lamarr")              # new last guest

print()
for guest in guests:
    print(f"Hi {guest}, you're invited to dinner!")

# 3-7: table fell through, only room for 2 -- pop guests until 2 remain
print("\nBad news, the bigger table won't arrive in time. Only 2 people can come.")

while len(guests) > 2:
    apologized_to = guests.pop()
    print(f"Sorry {apologized_to}, I can't invite you to dinner.")

for guest in guests:
    print(f"{guest}, you're still invited!")

del guests[0]
del guests[0]
print(f"\nGuest list is now: {guests}")
print(f"Number of guests left: {len(guests)}")

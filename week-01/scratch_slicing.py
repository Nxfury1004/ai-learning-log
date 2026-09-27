players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[0:3])   # first 3: indices 0,1,2 (stops before 3)
print(players[1:4])   # martina through florence
print(players[:4])    # start omitted -> from the beginning
print(players[2:])    # end omitted -> through the end
print(players[-3:])   # last 3, using a negative index

print("\nlooping through a slice:")
for player in players[:3]:
    print(player.title())

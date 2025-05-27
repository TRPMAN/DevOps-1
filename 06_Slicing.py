"""city1="Manchester United"

print(city1[0])
print(city1[1])
print(city1[2])

print(city1[-1])
print(city1[-2])
print(city1[-3])

# Slicing String
print(city1[3:7])
print(city1[:])
print(city1[:10])
print(city1[11:])"""

# Slicing Tuple (same as list)
"""football_club = ("ManU","ManCity","Barcelona","Real Madrid","Bayern Munich","Napoli")
print(football_club[1])
print(football_club[3])
print(football_club[-2])

print(football_club[1:6])
print(football_club[1:6][:4])
print(football_club[1:6][:4][1:])
print(football_club[1:6][:4][1:][0])"""

# Slicing Dictionary
europe_cup = {"Germany":"Bayern Munich","Spain":("Barcelona","Real Madrid"),"English":["ManCity","Liverpool","Arsenal"]}
print(europe_cup["Germany"])
print(europe_cup["Spain"])
print(europe_cup["English"])

print(europe_cup["Spain"][0])
print(europe_cup["English"][:2][1])

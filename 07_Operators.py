# Arithmetic Op
madrid = 15
barca = 5

total_ucl = madrid + barca
print(total_ucl)

total_ucl = madrid - barca
print(total_ucl)

total_ucl = madrid * barca
print(total_ucl)

# / will get float
total_ucl = madrid / barca
print(total_ucl)

total_ucl = barca % madrid
print(total_ucl)

total_ucl = madrid ** barca
print(total_ucl)

# Comparison Op
liver = 20
arsenal = 13

club = (liver > arsenal)
print(club)

club = (liver < arsenal)
print(club)

club = (liver == arsenal)
print(club)

club = (liver != arsenal)
print(club)

club = (liver >= arsenal)
print(club)

club = (liver <= arsenal)
print(club)

# Assignment Op
mbappe = 31
haaland = 22

mbappe += haaland # mbappe = mbappe + haaland
print(mbappe)

mbappe -= haaland # mbappe = mbappe - haaland
print(mbappe)

# Logical Op
manu = 20
chelsea = 6
spur = 2
newcastle = 4

premier = (manu > chelsea) or (spur > newcastle)
print(premier)

premier = (manu > chelsea) and (spur > newcastle)
print(premier)

premier = not(manu < chelsea)
print(premier)

#Membership Op
football_club = ("Spur","ManCity","Barcelona","Real Madrid","Bayern Munich","Napoli")

europa = "Manu" in football_club
print(europa)

topteam = "ManCity" in football_club
print(topteam)

trophies = "Barcelona" not in football_club
print(trophies)

# Identity Op
same = manu is liver
print(same)

same = manu is not chelsea
print(same)


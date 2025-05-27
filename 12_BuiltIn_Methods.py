# String Build in Methods
message = "manchester united won premier league 20 times"
print(message)
print(message.capitalize())
messageCap = message.capitalize()
print(messageCap)

# dir() func : show build in function that you can use on that Datatype
"""
print(dir(message))
print(dir([]))
print(dir(()))
print(dir({}))
"""

"""print(message.upper())
print(message.islower())
print(message.isupper())

print(message.find("won"))
print(message.find("20"))"""

"""cham = ("5","4","15","0","1")
print(".".join(cham))
print("-".join(cham))
print("/".join(cham))"""

UCL = ["Mancity","Barca","Madrid","Napoli","Spur","Liverpool"]
print(UCL)

UCL.append("Chelsea")
print(UCL)

UCL.extend(["Bayern","Newcastle"])
print(UCL)

UCL.insert(1,"Inter Milan")
print(UCL)

UCL.pop()
print(UCL)

UCL.pop(1)
print(UCL)

europe_cup = {"Germany":"Bayern Munich","Spain":("Barcelona","Real Madrid"),"English":["ManCity","Liverpool","Arsenal"]}
print(europe_cup.keys())
print(europe_cup.values())
europe_cup.clear()
print(europe_cup)
europe_cup["Germany"] = "Bayern Munich"
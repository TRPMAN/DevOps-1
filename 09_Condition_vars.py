usr_team = input("""
Hello We want you to enter your favorite football team
Enter your favorite team : """)
print(usr_team)

UCL = ["Mancity","Barca","Madrid","Napoli","Spur"]
Europa = ("Betis","Villa","Forest","Bilbao")
usr1 = {"name":"Dembele","team":"PSG","id": 1}
usr2 = {"name":"TAa","team":"Liverpool","id": 2}

# Check in DB
if usr_team in UCL:
    print(f"Your favorite team ({usr_team}) is in UCL")
elif usr_team in Europa:
    print(f"Your favorite team ({usr_team}) is in Europa")
elif (usr_team in usr1.values()) or (usr_team in usr2.values()):
    print(f"Your favorite team ({usr_team}) is the same as My friend's")
else:
    print(f"Your favorite team ({usr_team}) is not in UCL and Europa")
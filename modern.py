import random
def premier(team,champion):
    print(f"{team} have {champion} premier league")
    if (champion >= 20) :
        print(f"{team} won premier league equal or more than Manchester United")
    elif (champion >= 10) and (champion < 20):
        print(f"{team} won premier league less than Manchester United")
    elif (champion >= 1) and (champion < 10):
        print(f"{team} won premier league less than Manchester City")
    else:
        print(f"{team} never won premier league")

# Variable Length Arguments
def price(min_order, *args):
    print(f"You offer {min_order} euro for Lamine Yamal")
    print(args)
    for item in args:
        print(f"You also offer {item}")

# Variable Length Arguments **kwargs
def offer(*args, **kwargs):
    print(args)
    print(kwargs)
    min = sum(args) + random.randint(0,180)
    print(min)
    player = random.choice(list(kwargs.values()))
    print(f"You need to spend {min}M euro to get {player}")
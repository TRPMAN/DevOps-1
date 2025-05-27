# Defining Func
def add(arg1, arg2):
    total = arg1 + arg2
    return total

output = add("Messi", "Ronaldo")
print(output)

def sum(arg):
    x = 0
    for i in arg:
        x += i
    return x

output = sum([20,30,40])
print(output)

# Default Argument
def greeting(name="Pedri"):
    return f"Hello, {name}!"

output = greeting()
print(output)

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

premier("Barcelona",0)

# Variable Length Arguments
def price(min_order, *args):
    print(f"You offer {min_order} euro for Lamine Yamal")
    print(args)
    for item in args:
        print(f"You also offer {item}")

price("100M","200M","300M")

# Variable Length Arguments **kwargs
import random
def offer(*args, **kwargs):
    print(args)
    print(kwargs)
    min = sum(args) + random.randint(0,180)
    print(min)
    player = random.choice(list(kwargs.values()))
    print(f"You need to spend {min}M euro to get {player}")

offer(5,10,20,35,Bayern="Musiala",Madrid="Mbappe",Barcelona="Lamine Yamal",ManCity="De Bruyne")
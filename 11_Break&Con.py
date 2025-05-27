# Break
"""
for i in "ManchesterCity":
    print(i)
    if i == "t":
        print("Break")
        break
print("Out of loop")
"""

# Continue
"""
for i in "ManchesterCity":
    if i == "t":
        print("continue")
        continue
    print(i)
print("Out of loop")
"""

# Example
import random
UCL = ["Mancity","Barca","Madrid","Napoli","Spur","Liverpool","Chelsea","Arsenal","Inter Milan","Atletico Madrid","Bayern"]
random.shuffle(UCL)
# print(UCL)

Champion = random.choice(UCL)
# print(Champion)

for cham in UCL:
    print("-------------------------")
    print(f"Checking Team: {cham}")
    if cham == Champion:
        print(f"Champion is {cham}")
        print("-------------------------")
        break
    print(f"{cham} is not Champion this year")
    print("-------------------------")
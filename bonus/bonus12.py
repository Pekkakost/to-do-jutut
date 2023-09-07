feet_inches = input("Enter feet as inches: ")

def confert(feet_inches):
    parts=feet_inches.split(" ")

    feet=float(parts[0])
    inches=float(parts[1])
    meters=feet*0.3048 +inches *0.0254
    return meters

result = confert(feet_inches)

if result< 1:
    print("You are too small")

else:
    print("You can go to slide")

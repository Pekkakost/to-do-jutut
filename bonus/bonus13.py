feet_inches = input("Enter feet as inches: ")

def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}

def convert(feet, inches):  # You need to pass feet and inches as arguments to the function.
    meters = feet * 0.3048 + inches * 0.0254
    return meters

parsed = parse(feet_inches)
result = convert(parsed["feet"], parsed["inches"])  # Use parsed["feet"] and parsed["inches"] to access the values.
print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} meters")

if result < 1:
    print("you are too small")
else:
    print("You can use slide")
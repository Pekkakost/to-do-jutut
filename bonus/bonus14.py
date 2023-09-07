from bonus.converters14 import convert
from bonus.parsers import parse

feet_inches = input("Enter feet as inches: ")

feet_inches = input("Enter feet as inches: ")

parsed = parse(feet_inches)
result = convert(parsed["feet"], parsed["inches"])  # Use parsed["feet"] and parsed["inches"] to access the values.
print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} meters")

if result < 1:
    print("you are too small")
else:
    print("You can use slide")

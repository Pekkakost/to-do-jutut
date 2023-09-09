def strength(password):
    result = {}

    if len(password) > 8:
        result["lenght"] = True

    else:
        result["Lenght"] = False

    digit = False
    uppercase = False

    for i in password:
        if i.isdigit():
            digit = True

        if i.isupper():
            uppercase = True

    result["digits"] = digit
    result["uppercase"] = uppercase

    if all(result.values()):
        print("password strong")
    else:
        print("password weak")

if __name__ == "__main__":
    password="juomalasi234TT"
    strength(password)
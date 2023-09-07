try:
    width=float(input("Enter retsangle width: "))
    lenght = float(input("Enter retangle lenght: "))
    if width == lenght:
        exit("it looks like it is square")
    area = width*lenght
    print(area)
except ValueError:
    print("Enter a number")



def get_average():

    with open("data.txt","r") as file:
        data = file.readlines()

    values = []
    for line in data[1:]:
        try:
            value = float(line)
            values.append(value)
        except ValueError:
            # Skip lines that cannot be converted to floats
            continue
        average=sum(values)/len(values)

    return average


average=get_average()
print(average)
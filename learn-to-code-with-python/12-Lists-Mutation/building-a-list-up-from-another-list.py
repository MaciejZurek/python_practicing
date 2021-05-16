powerball_numbers = [4, 8, 15, 16, 23, 42]

def squares(numbers):
    sqrt = []
    for element in numbers:
        sqrt.append(element ** 2)

    return sqrt

print(squares(powerball_numbers))

def convert_to_floats(numbers):
    table = []
    for element in numbers:
        table.append(float(element))

    return table

print(convert_to_floats(powerball_numbers))
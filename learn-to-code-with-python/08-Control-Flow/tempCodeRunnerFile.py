def positive_or_negative(value):
    if value > 0:
        return "Positive!"
    elif value < 0:
        return "Negative!"
    else:
        return "It's zero!"

number = int(input("Wprowadz liczbe: "))
print(positive_or_negative(number))
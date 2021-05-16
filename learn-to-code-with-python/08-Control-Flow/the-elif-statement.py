# def positive_or_negative(value):
#     if value > 0:
#         return "Positive!"
#     elif value < 0:
#         return "Negative!"
#     else:
#         return "It's zero!"

# number = int(input("Wprowadz liczbe: "))
# print(positive_or_negative(number))
def calculator(operation, a, b):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiple":
        return a * b    
    elif operation == "divide":
        return a / b
    else:
        print("There is no such an operation!")

operacja = str(input("Co chcesz zrobic? "))
num1 = int(input("Pierwszy skladnik: "))
num2 = int(input("Drugi skladnik: "))

print(calculator(operacja, num1, num2))

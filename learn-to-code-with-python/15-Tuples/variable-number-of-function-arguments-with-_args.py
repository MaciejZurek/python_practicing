def accept_stuff(*args): # pozwala na wrzucenie wielu argumentow, args to krotka
    print(type(args))
    print(args)

accept_stuff(1, 2, 3, 4)

def my_max(*numbers):
    greatest = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest = number
    return greatest

print(my_max(1,3 , 5, -12,123))


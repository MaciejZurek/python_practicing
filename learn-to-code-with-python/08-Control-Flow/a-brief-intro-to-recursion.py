# def countdown_from(number):
#     start = number
#     while start > 0:
#         print(start)
#         start -= 1
# countdown_from(5)

def countdown_from(number):
    if number <= 0:
        return
    print(number)
    countdown_from(number - 1)

countdown_from(5)
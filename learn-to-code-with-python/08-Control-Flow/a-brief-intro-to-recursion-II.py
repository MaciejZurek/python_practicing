# def reverse(str):
#     start_index = 0
#     last_index = len(str) - 1
#     reversed_string = ""

#     while last_index >= start_index:
#         reversed_string += str[last_index]
#         last_index -= 1
#     return reversed_string

def reverse(str):
    if len(str) <= 1: # it's already reversed
        return str

    return str[-1] + reverse(str[:-1])


print(reverse("maciek")) # warts

# straw
# w + reverse(stra)
# wa + reverse(str)
# war + reverse(st)
# wart + reverse(s)
# warts
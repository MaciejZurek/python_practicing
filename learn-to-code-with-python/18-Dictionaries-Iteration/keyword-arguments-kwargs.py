def length(word):
    return len(word)

print(length("Hello"))
print(length(word = "Hello"))

# print(length()) # Error
# print(length(something = "Hello")) # Error

def collect_keyword_arguments(**kwargs): # ** oznacza, ze oczekujemy nieokreslonej ilosci parametrow; kwargs to slownik
    print(kwargs)
    print(type(kwargs)) # class 'dict'

    for key, value in kwargs.items():
        print(f"The key is {key} and the value is {value}.")

collect_keyword_arguments(a = 2, b = 3, c = 5)

def args_and_kwargs(a, b, *args, **kwargs): # *args bedzie krotka, ktora zawiera wszystkie inne parametry poza a i b
    print(f"The total of your regular arguments a and b is {a + b}.")
    print(f"The total of your args tuple is {sum(args)}.")
    
    dict_total = 0
    for value in kwargs.values():
        dict_total += value
    print(f"The to tal of your kwargs values is {dict_total}.")
args_and_kwargs(1, 2, 3, 4, 5, 6, x = 8, y = 9, z = 10)



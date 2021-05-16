numbers = [3, 4, 5, 6, 7]

squares = [number ** 2 for number in numbers]
print(squares)

rivers = ["Amazon", "Nile", "Yangtze"]
lengths = [len(river) for river in rivers]
print(lengths)

expressions = ["lol", "rotfl", "lmao"]
uppercases_expressions = [expression.capitalize() for expression in expressions]
print(uppercases_expressions)
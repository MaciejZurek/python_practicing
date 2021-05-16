metals = ["gold", "silver", "platinum", "palladinum"]

print(list(filter(lambda metal: len(metal) > 5, metals)))
print(list(filter(lambda el: "p" in el, metals)))

print(list(map(lambda element: element.count("l"), metals)))

print(list(map(lambda word: word.replace("s", "$"), metals)))
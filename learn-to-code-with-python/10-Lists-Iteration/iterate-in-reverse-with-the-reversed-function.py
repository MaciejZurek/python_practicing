the_simpsons = ["Homer", "Marge", "Bart", "Lisa", "Maggie"]

print(the_simpsons[::-1])

for char in the_simpsons[::-1]:
    print(f"{char} has a total of {len(char)} characters.")

print(reversed(the_simpsons))
print(type(reversed(the_simpsons))) # generator object

for char in reversed(the_simpsons): # laduje za kazda iteracja jeden element listy, a nie cala liste od razu, dobre przy duzych listach
    print(f"{char} has a total of {len(char)} characters.")


students = ["Bob", "Sally", "Sue"]
athletes = students
nerds = ["Bob", "Sally", "Sue"]

# == sprawdza czy zmienne wskazuja na takie same obiekty (moga byc rozne)
print(students == athletes)
print(students == nerds)

# is sprawdza czy zmienne pokazuja na ten sam obiekt w pamieci komputera
print(students is athletes)
print(students is nerds)

# z immutable objectem:

a = 5
b = a
c = 5

print(a is c) # w pamieci komputera to ten sam obiekt
print(a is b)
print(b is c)
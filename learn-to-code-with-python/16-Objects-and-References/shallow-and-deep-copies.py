import copy

numbers = [2, 3, 4]
a = [1, numbers, 5]

# rozne sposoby na zrobienie kopii
b = a[:]
b = a.copy()
b = copy.copy(a)

print(a == b)
print(a is b) # dwa rozne obiekty w pamieci komputera, zmienne juz nie wskazuja na jeden obiekt
print(a[1] is b[1]) # to dalej ten sam obiekt, bo zrobione jest shallow copy, a nie deep copy
a[1].append(100)
print(b)

b = copy.deepcopy(a)

print(a[1] is b[1]) # teraz to inne obiekty, zrobione z deepcopy
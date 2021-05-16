# immutable objects:

a = 3
b = a # teraz a i b pokazuja na jeden obiekt

a = 5 # teraz tworzy sie nowy obiekt (5), a b dalej wskazuje na 3

# mutable objects:

a = [1,2,3]
b = a

a[1] = 5
print(b) # jak mamy do czynienia z lista, a i b wskazuja ciagle na ta liste (bo jest mutable), mamy dwie zmienne do jednego obiektu

b.append(6)
print(a)
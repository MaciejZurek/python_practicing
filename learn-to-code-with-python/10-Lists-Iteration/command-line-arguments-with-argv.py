import sys

print(sys.argv)
print(type(sys.argv))

suma = 0

for element in sys.argv[1:]:
    suma += len(element)

print(suma)
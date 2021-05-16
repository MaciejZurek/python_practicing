def mult_and_sum(l):
    suma = 0
    for ind, val in enumerate(l):
        suma = suma + (ind - 1) * val

    return suma

print(mult_and_sum([1, 2, 3, 4, 5]))
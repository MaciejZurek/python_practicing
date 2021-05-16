a = {1, 2, 4}
b = {1, 2, 3, 4, 5}

# subset is a part of a larger group

print(a.issubset(b))
print(a < b)
print(a <= b)
print(b <= a)
print(b.issubset(a))

print(b.issuperset(a))
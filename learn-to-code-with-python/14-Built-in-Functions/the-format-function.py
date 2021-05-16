number = 0.123456789

print(format(number, "f"))
print(type(format(number, "f"))) # format zwraca string
print(format(number, ".2f"))

print(format(0.5, "f"))
print(format(0.5, "%"))
print(format(0.5, ".2%"))
print(format(8123123, ","))
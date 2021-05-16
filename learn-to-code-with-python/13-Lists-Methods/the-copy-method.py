units = ["meter", "kilogram", "candela", "second", "ampere", "kelvin", "mole"]

more_units = units.copy()

print(more_units == units)

units.remove("kelvin")
print(units)
print(more_units)

even_more_units = units[:] # kopia

print(even_more_units)
print("fast" in "breakfast")
print("fast" in "dinner")

meals = ["breakfast", "lunch", "dinner"]

print("lunch" in meals)

test_scores = [99.0, 35.0, 23.5]

print(99.0 in test_scores)
print(99 in test_scores)
print(26 not in test_scores)

if 100 not in test_scores:
    print("That value is not in there")
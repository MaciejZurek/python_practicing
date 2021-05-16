errands = ["Go to the gym", "Grab lunch", "Get promoted at work", "Sleep"]

print(enumerate(errands)) # generator object

for index, errand in enumerate(errands, 1):
    print(f"{errand} is number {index} on my list of things to do today.")


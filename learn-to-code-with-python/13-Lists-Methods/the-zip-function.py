breakfasts = ["Eggs", "Cereal", "Banana"]
lunches = ["Sishi", "Chicken Teryiaki", "Soup"]
dinners = ["Steak", "Meatballs", "Pasta"]

print(zip(breakfasts, lunches, dinners)) # zwraca zip object, adres
print(type(zip(breakfasts, lunches, dinners)))
print(list(zip(breakfasts, lunches, dinners))) # zwraca krotki

for breakfast, lunch, dinner in zip(breakfasts, lunches, dinners):
    print(f"My meal for today was: {breakfast}, {lunch} and {dinner}.")


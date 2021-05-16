print("winter".islower()) # sprawdza i zwraca True/False w zaleznosci od tego czy wszystkie znaki sa male
print("winter 12$1#!".islower())
print("Winter".islower())

print("SUMMER".isupper()) # sprawdza i zwraca True/False w zaleznosci od tego czy wszystkie znaki sa wielkie

print("Summer Winter".istitle()) # sprawdza czy wyrazy zaczynaja sie od wielkich liter

print("alpha".isalpha()) # sprawdza czy wszystkie znaki sa literami
print("alpha ".isalpha())

print("51".isnumeric()) # sprawdza czy wszystkie znaki sa numerami
print("al102".isnumeric())

print("Area51".isalnum()) # sprawdza czy wszystkie znaki sa literami lub numerami
print("Area 51".isalnum())

print(" ".isspace()) # sprawdza czy znak jest spacja
print(" 5 ".isspace())
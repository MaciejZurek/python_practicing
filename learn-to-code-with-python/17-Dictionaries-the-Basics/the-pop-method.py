years = [1991, 1995, 2000, 2007]

years.pop(1)
print(years)

release_dates = {
    "Python": 1991,
    "Ruby": 1995,
    "Java": 1995,
    "Go": 2007
}

year = release_dates.pop("Java") # zwraca usunieta wartosc
print(release_dates)
print(year)

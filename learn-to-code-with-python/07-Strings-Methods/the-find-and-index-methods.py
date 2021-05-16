browser = "Google Chrome"

print(browser.find("C")) # zwraca pierwszy najblizszy element podany jako argument i zwraca indeks
print(browser.find("Ch")) # zwraca poczatek szukanego substringa
print(browser.find("o"))

print(browser.find("z"))
print(browser.find("o", 2)) # podajemy indeks od ktorego szukamy substringa

print("Ch" in browser)

print(browser.index("C")) # dziala podobnie do .find ale jesli substring nie istnieje wywala IndexError
print(browser.rfind("o")) # dziala jak .find tylko zwraca indeks ostatniego pojawienia substringa w stringu
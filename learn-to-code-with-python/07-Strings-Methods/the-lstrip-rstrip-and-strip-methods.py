empty_space = "    content       "

print(empty_space.rstrip().lstrip()) # usuawaja puste przestrzenie z lewej i prawej strony

website = "www.python.org"

print(website.lstrip("w")) # usuwa znaki z lewej jakie chcemy
print(website.rstrip("org"))

print(website.strip("worg.")) # usuwa z poczatku i konca
story = "once upon a time"

print(story.capitalize()) # robi wielka litere z poczatku stringa
print(story.title()) # robi wielka litere z poczatku kazdego wyrazu w stringu
print(story.upper()) # robi wielkie litery z kazdego znaku w stringu

hello = "HELLO"

print(hello.lower()) # robi male litery wszystkich znakow stringa

print("HeLlO".swapcase()) # zamienia wielkie litery na male, male na wielkie

# kazda metoda daje nam nowe obiekty

print("BENJAMIN FRANKLIN".lower().title())

story = story.title()
print(story)
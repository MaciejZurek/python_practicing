# add and update methods are used to add elements to a set once it is created

disney_characters = {
    "Mickey Mouse",
    "Minnie Mouse",
    "Elsa"
}

disney_characters.add("Ariel") # adds "Ariel" to the set but on the random position - sets are not sequences
print(disney_characters) 
disney_characters.add("Elsa") 
print(disney_characters) 

# updates may add multiple elements to set

disney_characters.update(["Donald Duck", "Goofy"]) # accepts any iterable object
print(disney_characters) 

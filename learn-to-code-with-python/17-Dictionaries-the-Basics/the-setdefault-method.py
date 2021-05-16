film_directors = {
    "The Godfather": "Francis Ford Coppola",
    "The Rock": "Michael Bay",
    "Goodfellas": "Martin Scorsese"
}

print(film_directors.get("The Rock"))
film_directors.setdefault("Bad Boys", "Michael Bay")

print(film_directors)
sports_team_rosters = {
    "New England Patriots": ["Tom Brady", "Rob Gronkowski", "Julian Edelman"],
    "New York Giants": ["Eli Manning", "Odell Beckham"]
}

sports_team_rosters["Pitsburg Steelers"] = ["Ben Riasdnasd", "Antonio Brown"] # dodanie pary key-value

print(sports_team_rosters)
sports_team_rosters["New York Giants"] = ["Eli Manning"]

video_game_options = {}
video_game_options = dict() # stworzenie nowego pustego slownika

video_game_options["subtitles"] = True
video_game_options["difficulty"] = "Medium"
video_game_options["volume"] = 7

print(video_game_options)

video_game_options["difficulty"] = "Hard" # nadpisanie wartosci w slowniku
video_game_options["subtitles"] = False

print(video_game_options)

words = ["danger", "beware", "danger"]

def count_words(slowa):
    counts = {}
    for word in slowa:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print(count_words(words))
languages = ["Python", "Java Script", "Ruby"]

lenghts = {language: len(language) for language in languages}

print(lenghts)

word = "supercalifragilisticexpialidocious"

letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)

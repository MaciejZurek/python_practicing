# remove and discard are used to remove elements from the set
# remove will rise an exception while trying to remove an element which is not in the set, discard will just move on

agents = {
    "mulder",
    "Scully",
    "Doggett",
    "Reyes"
}

agents.remove("Doggett")

print(agents)

# agents.remove("aaa") # KeyError

agents.discard("mulder")

print(agents)

agents.discard("aaa") # nothing happens


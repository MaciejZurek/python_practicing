def modify_list(l):
    a = l[-1]
    del l[-1]
    l[-1] = str(l[-1]) + " i " + str(a)
    return l


spam = ["jablka", "banany", "tofu", "koty"]

print(modify_list(spam))
print(modify_list([]))
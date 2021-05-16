# difference method returns a set of elements that are not in the given

candy_bars = {"Mily Way", "Snickers", "100 Grand"}
sweet_things = {"aaa", "bb", "Snickers"}

print(candy_bars.difference(sweet_things)) # \
                                            # these two are not equal!
print(sweet_things.difference(candy_bars)) # /

print(candy_bars - sweet_things)

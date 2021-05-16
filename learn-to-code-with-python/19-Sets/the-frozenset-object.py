# frozenset is an immutable set

mr_freeze = frozenset([1,2,3,2])
print(mr_freeze)

# mr_freeze.add(4) # method doesn't exist for frozen set

regular_set = {1,2,3}
# print({ regular_set : "Some value"}) # TypeError - unhashable type 'set', because is mutable
print({ mr_freeze : "Some value"}) # can be a key because is immutable
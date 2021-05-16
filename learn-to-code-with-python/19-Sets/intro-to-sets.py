# sets may contain only immutable objects e.g. numbers, tuples, strings

stocks = {"MSFT", "FB", "IBM", "FB"}

print(stocks) # duplicate delated

prices = {1, 2, 3, 4, 5, 3, 4, 2}

print(prices)

# set comprehension
squares ={x**2 for x in [-5, -4, -3, 3, 4, 5]} # duplicates will be removed
print(squares)
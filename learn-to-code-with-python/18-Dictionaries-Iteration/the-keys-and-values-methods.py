crypto_currency_prices = {
    "Bitcoin": 400000,
    "Ethereum": 7000,
    "Litecoin": 10
}

# print(crypto_currency_prices.keys())
# print(type(crypto_currency_prices.keys())) # to nie lista!

# print(crypto_currency_prices.values())
# print(type(crypto_currency_prices.values())) # to nie lista!, ale obiekt gotowy do iteracji

for currency in crypto_currency_prices.keys():
    print(currency)

print("Bitcoin" in crypto_currency_prices.keys())
print(len(crypto_currency_prices.keys()))
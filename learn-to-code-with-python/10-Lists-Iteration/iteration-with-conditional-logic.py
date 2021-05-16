values = [3, 6, 9, 12, 15, 18, 21, 24]
other_values = [5, 10, 15, 20, 25, 30]

def odds_sum(numbers):
    sum = 0
    for number in numbers:
        if number % 2 != 0:
            sum += number
        else:
            continue
    return sum


print(odds_sum(values)) # 48
print(odds_sum(other_values)) # 45
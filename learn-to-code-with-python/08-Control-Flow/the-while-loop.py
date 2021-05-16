# count = 0

# while count <= 5:
#     print(count)
#     count += 1

# print(count)

invalid_value = True

while invalid_value:
    user_value = int(input("Enter value above 10: "))
    if user_value > 10:
        print(f"Thanks, {user_value} is good!")
        invalid_value = False
    else:
        print(f"{user_value} is not good! Try again!")
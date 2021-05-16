# college_courses = {
#     "History": "Mr. Washington",
#     "Math": "Mr. Newton",
#     "Science": "Mr. Einstein"
# }

# for key, value in college_courses.items(): # iteration object
#     print(f"The course {key} is being taught by {value}!")

def sum_of_values(d, l):
    suma = 0
    for key, value in d.items():
        if key in l:
            suma += value
    return suma


my_dict = { "a": 5, "b": 3, "c": 10 }

print(sum_of_values(my_dict, ["a"]))           # => 5
print(sum_of_values(my_dict, ["a", "c"]))       # => 15
print(sum_of_values(my_dict, ["a", "c", "b"]))  # => 18
print(sum_of_values(my_dict, ["z"]))            # => 0
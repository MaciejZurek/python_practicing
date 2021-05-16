flight_prices = {
    "Chicago": 199,
    "San Francisco": 499,
    "Denver": 295
}

print(flight_prices["Chicago"])
print(flight_prices["Denver"])
# print(flight_prices["Seattle"]) # KeyError: key does not exist

gym_membership_packages = {
    29: ["Machines"],
    49: ["Machines", "Vitamin Suplements"],
    79: ["Machines", "Vitamin Suplements", "Sauna"]
}

print(gym_membership_packages[29])
print(gym_membership_packages.get(29, ["Basic Dumbbells"]))
print(gym_membership_packages.get(20, ["Basic Dumbbells"]))
print(gym_membership_packages.get(20))


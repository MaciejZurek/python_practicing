def display_inventory(inventory):
    print("Inwentarz:")
    item_total = 0
    for k, v in inventory.items():
        print(f"{v} {k}")
        item_total += v

    print("Calkowita liczba przedmiotow: " + str(item_total))

def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item not in inventory:
            inventory[item] = 1
        else:
            inventory[item] += 1
    return inventory

dragon_loot = ["zlote monety", "sztylet", "zlote monety", "zlote monety", "ruby"]
inv = {
    "lina": 1,
    "pochodnia": 6,
    "zlote monety": 42,
    "sztylet": 1,
    "strzala": 12
}
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
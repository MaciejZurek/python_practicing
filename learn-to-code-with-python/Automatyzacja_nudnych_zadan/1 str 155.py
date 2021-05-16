def displayInventory(inventory):
    print("Inwentarz:")
    item_total = 0
    for k, v in inventory.items():
        print(f"{v} {k}")
        item_total += v

    print("Calkowita liczba przedmiotow: " + str(item_total))

inv = {
    "lina": 1,
    "pochodnia": 6,
    "zlote monety": 42,
    "sztylet": 1,
    "strzala": 12
}

displayInventory(inv)
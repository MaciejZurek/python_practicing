def image_from_list(l):
    for kolumna in range(len(l[0])):
        print("\n")
        for wiersz in range(len(l)):
            print(l[wiersz][kolumna], end = " ")




grid = [[".", ".", ".", ".", ".", "."],
        [".", "0", "0", ".", ".", "."],
        ["0", "0", "0", "0", ".", "."],
        ["0", "0", "0", "0", "0", "."],
        [".", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "."],
        ["0", "0", "0", "0", ".", "."],
        [".", "0", "0", ".", ".", "."],
        [".", ".", ".", ".", ".", "."]]

image_from_list(grid)
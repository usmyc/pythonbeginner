number_grid = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print(number_grid[1][3])

for i in number_grid:
    for j in i:
        j += 1
        print(j)

from random import shuffle, randint
from time import sleep

def print_table(list):
    for i in list:
        for j in i:
            print(str(j) + ((length - len(str(j))) * " "), end = "")
        print()

width, height = int(int(input("Rows: ")), input("Columns: "))
length, grid = len(str(width * height)) + 2, list(range(1, (width * height) + 1))
shuffle(grid)
unique = grid.copy()

grid, unique = [grid[i:i+width] for i in range(0, len(grid), width)], [unique[i:i+width] for i in range(0, len(unique), width)]

row, col = randint(0, height - 1), randint(0, width - 1)
random_number = grid[row][col]

print_table(grid)
grid[row][col] = "O"
input("Press enter to hide the table.")
for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        if i != row or j != col:
            grid[i][j] = "X"

c = 5.0
while c > 0:
    if c == 5.00: print("\033[F\x1b[2K" * (height + 1) + "Get ready in 5.00 second(s)!")
    else: print(f"\033[FGet ready in {c} second(s)!")
    c -= 0.01
    sleep(0.01)

print("\033[F\x1b[2K" * (height), end = "")
print_table(grid)

if int(input("Enter O: ")) == random_number: print("\033[F\x1b[2K" * (height + 1) + f"You Won!!!\nthe number is {random_number}")
else: print("\033[F\x1b[2K" * (height + 1) + f"Sorry, the number is {random_number}\n")
print("This is the main table:")
print_table(unique)

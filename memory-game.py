from random import shuffle, randint
from time import sleep

def print_table(list):
    for i in list:
        for j in i:
            print(str(j) + ((length - len(str(j))) * " "), end = "")
        print()

width, height = int(input("Width: ")), int(input("Height: "))
length, grid = len(str(width * height)) + 2, list(range(1, (width * height) + 1))
shuffle(grid)
unique = grid.copy()

grid = [grid[i:i+width] for i in range(0, len(grid), width)]
unique = [unique[i:i+width] for i in range(0, len(unique), width)]

row, col = randint(0, height - 1), randint(0, width - 1)
random_number = grid[row][col]

print_table(grid)
grid[row][col] = "X"
input("Press enter to hide the table.")
for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        if i != row or j != col:
            grid[i][j] = "O"

for i in range(5, 0, -1):
    if i == 5: print("\033[F\x1b[2K" * (height + 1) + "Get ready in 5 second(s)!")
    else: print(f"\033[FGet ready in {i} second(s)!")
    sleep(1)
print("\033[F\x1b[2K" * (height), end = "")
print_table(grid)

answer = int(input("Enter X: "))
if answer == random_number: print("\033[F\x1b[2K" * (height + 1) + f"You Won!!!\nthe number is {random_number}")
else: print("\033[F\x1b[2K" * (height + 1) + f"Sorry, the namber is {random_number}\n")
print("This is the main table:")
print_table(unique)

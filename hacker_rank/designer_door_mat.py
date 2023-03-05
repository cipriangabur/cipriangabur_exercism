# Enter your code here. Read input from STDIN. Print output to STDOUT
# r, c = input().split()
r, c = '7', '21'
rows, cols = int(r), int(c)
pattern = ".|."
welcome = 'WELCOME'
half_row = int(rows / 2)
for row in range(rows):
    if row == half_row:
        print(welcome.center(cols, '-'))
    elif row < half_row:
        print((pattern * (2 * row + 1)).center(cols, '-'))
    else:
        print((pattern * (rows - 2 * (row - half_row))).center(int(cols), '-'))

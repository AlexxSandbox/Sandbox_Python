height = int(input())
block = '#'
if height > 0:
    for i in range(height):
        row = block + block*2*i
        new_row = row.center((height * 2) - 1, ' ')
        print(new_row)



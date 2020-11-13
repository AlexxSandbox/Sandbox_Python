""" Генератор списка """
# create new list 1*1, 2*2, 3*3
list_numbers = [1, 2, 3]
new_list = [x * x for x in list_numbers]
print(new_list)


# create new list with converting str to floatА
list_strings = ['8.9', '8.7', '9.2']
new_list = [float(num) for num in list_strings]
print(new_list)


# odd numbers
numbers = [4, 8, 15, 16, 23, 42, 108]
odd_list = [x for x in numbers if x % 2 == 1]
print(odd_list)


# conditions with if
text = ["function", "is", "a", "synonym", "of", "occupation"]
words_tion = [word for word in text if word.endswith("tion")]
print(words_tion)


# if - else
old_list = [8, 13, -7, 4, -9, 2, 10]
new_list = [num if num >= 0 else 0 for num in old_list]
print(new_list)


# make field for tic-tak-toe
game_field = [i for i in '123456789']
print(game_field)
new_field = []
for i in range(3):
    new_field.append(game_field[i*3:3+i*3])
move = [int(i) for i in input().split(' ')]  # input x_y
new_field[move[1]*-1][move[0] - 1] = 'X'
print(new_field)


# several variables
z = [(x, y) for x in range(3) for y in range(3) if y >= x]
print(z)

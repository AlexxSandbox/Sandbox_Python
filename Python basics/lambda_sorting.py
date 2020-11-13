""" Sorting with lambda func - integers """
items = [(0, 50, 60), (1, 20, 20), (2, 20, 10), (3, 20, 7), (4, 30, 40)]
sort_items = sorted(items, key=lambda x: (x[2], x[1]))
# [(3, 20, 7), (2, 20, 10), (1, 20, 20), (4, 30, 40), (0, 50, 60)]
sort_items_2 = sorted(items, key=lambda x: (-x[1], x[2]))
# [(0, 50, 60), (4, 30, 40), (3, 20, 7), (2, 20, 10), (1, 20, 20)]
sort_items_3 = sorted(items, key=lambda x: (-x[2], x[1]))
# [(0, 50, 60), (4, 30, 40), (1, 20, 20), (2, 20, 10), (3, 20, 7)]


""" Sorting with lambda func - string  """
items_2 = [['9', '21'],['3', '6'],['0', '17'],['1', '1'],['9', '20'],['18', '19']]
sort_1 = sorted(items_2, key=lambda x: (int(x[1]), int(x[0])))
# [['1', '1'], ['3', '6'], ['0', '17'], ['18', '19'], ['9', '20'], ['9', '21']]
sort_2 = sorted(items_2, key=lambda x: (-int(x[0]), int(x[1])))
# [['18', '19'], ['9', '20'], ['9', '21'], ['3', '6'], ['1', '1'], ['0', '17']]
sort_3 = sorted(items_2, key=lambda x: (-int(x[1]), int(x[0])))
# [['9', '21'], ['9', '20'], ['18', '19'], ['0', '17'], ['3', '6'], ['1', '1']]


def max_num(array):
    """ Find max number it will be made using some numbers """
    max_len = len(str(max([int(x) for x in array]))) + 1
    result = sorted(array, key=lambda x: int((x*max_len)[:max_len]))
    return result


print(*max_num(['57', '575', '576']), sep='')  # 57557576
print(*max_num(['831', '828', '82']), sep='')  # 82828831

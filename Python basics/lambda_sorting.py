# items = [(0, 50, 60), (1, 20, 20), (2, 20, 10), (3, 20, 7), (4, 30, 40)]
# sort_items = sorted(items, key=lambda x: (x[2], x[1]))
# sort_items_2 = sorted(items, key=lambda x: (-x[1], x[2]))
# sort_items_3 = sorted(items, key=lambda x: (-x[2], x[1]))
#
# print(sort_items)
# print(sort_items_2)
# print(sort_items_3)
# print('\n')
#
# items_2 = [['9', '21'],['3', '6'],['0', '17'],['1', '1'],['9', '20'],['18', '19']]
# sort_1 = sorted(items_2, key=lambda x: (int(x[1]), int(x[0])))
# sort_2 = sorted(items_2, key=lambda x: (-int(x[0]), int(x[1])))
# sort_3 = sorted(items_2, key=lambda x: (-int(x[1]), int(x[0])))
#
# print(sort_1)
# print(sort_2)
# print(sort_3)

item_3 = ['57', '575', '576']
item_4 = ['831', '828', '82']
len = len(str(max([int(x) for x in item_3]))) + 1
sort_3 = sorted(item_3, key=lambda x: int((x*len)[:len]))
print(sort_3)

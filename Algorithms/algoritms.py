import math


def quadro_func(numm):
    """y = ax2 + bx + c"""
    a, x, b, c = numm.split(' ')
    print(int(a) * int(x) ** 2 + int(b) * int(x) + int(c))


def dec_to_bin(numm, bin_num = []):
    """ Перевод десятичного числа в бинарный - 1 вариант"""
    numm_ost = numm % 2
    bin_num.append(numm_ost)
    numm_cel = numm // 2
    if numm_cel <= 1:
        bin_num.append(numm_cel)
        print(bin_num[::-1])
    else:
        dec_to_bin(numm // 2)


def dec_to_bin_2(numm):
    """ Перевод десятичного числа в бинарный - 2 вариант"""
    bin_num = ''
    numm_cel = numm // 2
    numm_ost = numm % 2
    bin_num += str(numm_ost)
    while numm_cel > 1:
        numm = numm // 2
        numm_ost = numm % 2
        bin_num += str(numm_ost)
        numm_cel = numm // 2
    bin_num += str(numm_cel)
    print(bin_num[::-1])


def max_students(guests, k):
    """
    Выведите k чисел (id вуза) через пробел, отсортированные по убыванию,
    начиная от максимального количества гостей от вуза на конференции.
    """
    limit = int(k)
    journal = guests.split()
    school = {a: 0 for a in journal}
    answer = []

    for record in journal:
        if record in school:
            school[record] += 1

    school = {id: counter for id, counter in sorted(school.items(), key=lambda item: item[1], reverse=True)}

    for id in school:
        answer.append(id)

    print(' '.join(answer[:limit]))


def num_to_str(str_number, int_number):
    """ Списочная форма """
    x = str_number.replace(' ', '')
    k = int_number
    sum = int(x) + int(k)
    print(str(sum).replace('', ' ').lstrip())


def anagramma(word_1, word_2):
    """ Анаграммы """
    word_1 = [letter for letter in word_1]
    word_2 = [letter for letter in word_2]

    if len(word_1) == len(word_2):
        word_1 = sorted(word_1)
        word_2 = sorted(word_2)
        if word_1 == word_2:
            return 'True'
        else:
            return 'False'


def bin_add():
    """ Сложение двоичных чисел """
    num_1 = input()
    num_2 = input()
    result = ''
    ost = 0

    max_len = max(len(num_1), len(num_2))
    num_2 = num_2.zfill(max_len)
    num_1 = num_1.zfill(max_len)

    for i in range(max_len-1, -1, -1):
        r = ost
        r += 1 if num_1[i] == '1' else 0
        r += 1 if num_2[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
        ost = 0 if r < 2 else 1

    if ost != 0:
        result = '1' + result

    print(result.zfill(max_len))


def zero_delete(goals):
    """ Убрать ноли """
    goals = goals.split()
    clear_goals = []
    for goal in goals:
        if goal != '0':
            clear_goals.append(goal)
    print(' '.join(clear_goals))


def extra_letter(word_1, word_2):
    """ Лишняя буква """
    letters_1 = [letter for letter in word_1]
    letters_2 = [letter for letter in word_2]
    garbage = set()
    for letter in letters_2:
        if letters_1.count(letter) != letters_2.count(letter):
            garbage.add(letter)
    print(' '.join(garbage))


def log_4(number):
    """ Степень четырех """
    answer = math.log(number, 4)
    if answer == int(answer):
        return True
    else:
        return False


def degree(num):
    while num != 1:
        if num % 4 != 0:
            return False
        num = num / 4
    return True


def excess_one(num, bin_num=[]):
    """ Количество единиц в бинарном числе """
    num_ost = num % 2
    bin_num.append(num_ost)
    num_cel = num // 2
    if num_cel <= 1:
        bin_num.append(num_cel)
        print(bin_num[::-1].count(1))
    else:
        excess_one(num // 2)


def launch():
    """ Обеды """
    coupons = input().split()
    staff = {a: 0 for a in coupons}

    for coupon in coupons:
        if coupon in staff:
            staff[coupon] += 1

    for man, count in staff.items():
        if 2 < count or count == 1:
            print(man)


def check_unique():
    """ База данных - проверка уникальности записей """
    records = input().split()
    id = {a: 0 for a in records}

    for record in records:
        if record in id:
            id[record] += 1

    for id, count in id.items():
        if count > 1:
            print(id)


def quicksort(array):
    """ Вывод результатов """
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        sort_array = quicksort(less) + [pivot] + quicksort(greater)

    return sort_array


def user_count(server_1, guests_1, guests_2, server_2):
    """ И снова Вася """
    server_1 = server_1.split()
    guests_1 = int(guests_1)
    server_2 = server_2.split()
    server_1 = server_1[:guests_1] + server_2
    server_1 = [int(i) for i in server_1]
    server_1.sort()
    server_1 = [str(i) for i in server_1]
    return ' '.join(server_1)


def hobbies():
    """ Кружки """
    trenings = []
    q = int(input())
    for i in range(q):
        trening = input()
        if trening not in trenings:
            trenings.append(trening)

    for trening in trenings:
        print(trening)


def monitoring():
    """ Мониторинг """
    row = int(input())
    coll = int(input())
    matrix = []
    tr_matrix = []

    for i in range(row):
        matrix.append(input().split())

    for j in range(coll):
        pr_matrix = []
        for i in range(row):
            pr_matrix.append(matrix[i][j])
        tr_matrix.append(pr_matrix)

    for row in tr_matrix:
        print(' '.join(row))


def find_longest(s):
    """ Подстроки """
    maxlen = 0
    longest = ""
    for i in range(0,len(s)):
        subs = s[i:]
        chars = set()
        for j,c in enumerate(subs):
            if c in chars:
                break
            else:
                chars.add(c)
        else:
            j+=1
        if j>maxlen:
            maxlen=j
            longest=s[i:i+j]
    return longest

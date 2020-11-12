# about generator
num_gen = (x * x for x in range(5))  # syntax
print(num_gen)  # <generator object <genexpr> at 0x0329B4F8>
for i in num_gen:
    print(i)  # 0 1 4 9 16

for i in num_gen:
    print(i)  # nothing - generator is end, not in memory


# custom generator
class Multifilter:
    """ Custom generator with filter """

    def judge_half(pos, neg):
        return pos >= neg

    def judge_any(pos, neg):
        return pos >= 1

    def judge_all(pos, neg):
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        for i in self.iterable:
            pos, neg = 0, 0
            for f in self.funcs:
                if f(i):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                yield i


def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)]

print(list(Multifilter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]
print(list(Multifilter(a, mul2, mul3, mul5, judge=Multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]
print(list(Multifilter(a, mul2, mul3, mul5, judge=Multifilter.judge_all)))
# [0, 30]


# itertools
import itertools
import operator


# summ elements (1, 2*1, 3*2, ..., n*n - 1)
print(list(itertools.accumulate(range(1, 10), operator.mul)))
# [1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

waltz = itertools.cycle(['и раз', 'и два', 'и три'])
print(next(waltz))  # и раз
print(next(waltz))  # и два

nums = range(10)
squares = map(pow, nums, itertools.repeat(2))
print(list(squares))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

colors = ['белый', 'жёлтый', 'синий', 'красный']
for item in itertools.combinations(colors, 3):
    print(item)

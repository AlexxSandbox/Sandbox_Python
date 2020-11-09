class ExtendedStack(list):
    def sum(self):
        a = self.pop()
        b = self.pop()
        self.append(a + b)

    def sub(self):
        a = self.pop()
        b = self.pop()
        self.append(a - b)

    def mul(self):
        a = self.pop()
        b = self.pop()
        self.append(a * b)

    def div(self):
        a = self.pop()
        b = self.pop()
        self.append(a // b)


def test():
    stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
    stack.div()
    assert stack.pop() == 2
    stack.sub()
    assert stack.pop() == 6
    stack.sum()
    assert stack.pop() == 7
    stack.mul()
    assert stack.pop() == 2
    assert len(stack) == 0


test()

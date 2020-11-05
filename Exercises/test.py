class Buffer:

    def __init__(self):
        self.buffer = []
        self.count = 0

    def add(self, *args):
        for arg in args:
            self.buffer.append(arg)
            self.count += 1
            if self.count == 5:
                print(sum(self.buffer))
                self.buffer.clear()
                self.count = 0

    def get_current_part(self):
        return self.buffer

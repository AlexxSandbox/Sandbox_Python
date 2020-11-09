import time


class Loggable:
    """ Добавление штампа времени к выводу"""
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    """ Переопределение метода append """
    def append(self, item):
        # super(LoggableList, self).append(item)
        list.append(self, item)
        self.log(item)


def test():
    x = LoggableList([1, 2, 4, 5])
    x.append(6)
    assert len(x) == 5


test()

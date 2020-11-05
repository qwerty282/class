class OddEvenSeparator():
    def __init__(self):
        self.lst = []

    def add_number(self, number):
        self.lst.append(number)

    def even(self):
        return list(filter(lambda x: x % 2 == 0, self.lst))

    def odd(self):
        return list(filter(lambda x: x % 2 != 0, self.lst))

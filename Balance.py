class Balance:
    def __init__(self):
        self.right = 0
        self.left = 0

    def add_right(self, a):
        self.right += a

    def add_left(self, b):
        self.left += b

    def result(self):
        if self.left == self.right:
            print('=')
        elif self.left > self.right:
            print('L')
        else:
            print('R')

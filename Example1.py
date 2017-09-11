def add (x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x/y

def modulo(x, y):
    return x % y



class SimpleMath:
    'SimpleMath class'
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __del__(self):
        print('SimpleMath instance was destroyed.')


    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        return self.x / self.y

    def modulo(self):
        return self.x % self.y


    def __repr__(self):
        return self.x + ' ' + self.y




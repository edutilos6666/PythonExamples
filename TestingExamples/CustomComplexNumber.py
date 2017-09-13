class CustomComplexNumber:
    def __init__(self, re = None, im = None):
        self.re = re
        self.im = im

    def __add__(self, other):
        ret = CustomComplexNumber()
        ret.re = self.re + other.re
        ret.im = self.im + other.im

        return ret


    def __sub__(self, other):
        ret = CustomComplexNumber()
        ret.re = self.re - other.re
        ret.im = self.im - other.im

        return ret

    def __mul__(self, other):
        ret = CustomComplexNumber()
        ret.re = self.re*other.re - self.im*other.im
        ret.im = self.re*other.im + self.im*other.re

        return ret


    def multiply_by_factor(self, factor):
        ret = CustomComplexNumber()
        ret.re = self.re * factor
        ret.im = self.im  * factor

        return ret


    def __repr__(self):
        return "{0} + i*({1})".format(self.re, self.im)
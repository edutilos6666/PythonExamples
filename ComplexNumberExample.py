import math
class ComplexNumber:
    def __init__(self, re = 0, im = 0):
        self.re = re
        self.im = im

    def add(self, other):
        ret = ComplexNumber()
        ret.re = self.re + other.re
        ret.im = self.im + other.im
        return ret



    def subtract(self, other):
        ret = ComplexNumber()
        ret.re = self.re - other.re
        ret.im = self.im - other.im
        return ret


    def multiply(self, other):
        ret = ComplexNumber()
        ret.re = self.re*other.re - self.im*other.im
        ret.im = self.re*other.im + self.im*other.re
        return ret


    def multiply_by_factor(self, factor):
        ret = ComplexNumber()
        ret.re = self.re * factor
        ret.im = self.im* factor
        return ret

    def divide(self, other):
        ret = ComplexNumber()
        factor = math.pow(other.re, 2) + math.pow(other.im, 2)
        temp = ComplexNumber(other.re, -other.im)
        ret = self.multiply(temp)
        ret = ret.divide_by_factor(factor)
        return ret

    def divide_by_factor(self, factor):
        ret = ComplexNumber()
        ret.re = self.re / factor
        ret.im = self.im / factor
        return ret


    # operator overloading
    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.subtract(other)

    def __mul__(self, other):
        return self.multiply(other)

    def __truediv__(self, other):
        return self.divide(other)



    def __str__(self):
        return str(self.re) + '+ i*' + str(self.im)


import unittest
from TestingExamples.SimpleMath import SimpleMath
from TestingExamples.CustomComplexNumber import CustomComplexNumber



class TestSimpleMath(unittest.TestCase):
    def setUp(self):
        self.sm = SimpleMath()
        self.a = 10.0
        self.b = 3.0

    def test_add(self):
        res = self.sm.add(self.a, self.b)
        self.assertEqual(13.0, res)


    def test_multiply(self):
        res = self.sm.multiply(self.a, self.b)
        self.assertEqual(30.0, res)


    def test_subtract(self):
        res = self.sm.subtract(self.a, self.b)
        self.assertEqual(7.0, res)

    def test_divide(self):
        res = self.sm.divide(self.a, self.b)
        self.assertEqual(10/3, res)






class TestCustomComplexNumber(unittest.TestCase):
    def setUp(self):
        self.cn1 = CustomComplexNumber(3, 3)
        self.cn2 = CustomComplexNumber(2, 2)

    def test_add(self):
        res = self.cn1 + self.cn2
        self.assertEqual(5, res.re)
        self.assertEqual(5, res.im)

    def test_subtract(self):
        res = self.cn1 - self.cn2
        self.assertEqual(1, res.re)
        self.assertEqual(1, res.im)

    def test_multiply(self):
        res = self.cn1 * self.cn2
        self.assertEqual(0 , res.re)
        self.assertEqual(12, res.im)

    def test_multiply_by_factor(self):
        res = self.cn1.multiply_by_factor(10)
        self.assertEqual(30, res.re)
        self.assertEqual(30, res.im)



if __name__ == "__main__":
    unittest.main()

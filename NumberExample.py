import math
import random

def example2():
    'random methods'
    print('random.random() = ', random.random())
    print('random.randint(10, 1000) =', random.randint(10, 1000))
    print('random.randrange(10, 1000) =', random.randrange(10, 1000))
    print('random.randrange(10, 1000, 2) = ', random.randrange(10, 1000, 2))
    print('random.randrange(10, 1000, 3) = ', random.randrange(10, 1000, 3))
    numbers =  [1, 2,3, 4, 5, 6, 7, 8, 9]
    names = ["foo", "bar", "bim", "pako", "edu"]
    print('numbers = ', numbers)
    print('names = ', names)
    print('random.choice(numbers) = ', random.choice(numbers))
    print('random.choice(names) = ', random.choice(names))
    print('random.uniform(10, 1000) = ', random.uniform(10, 1000))
    random.shuffle(numbers)
    random.shuffle(names)
    print('numbers after shuffle = ', numbers)
    print('names after shuffle = ', names)
    print()

def example1():
    'math methods'
    str = '100'
    n = int(str)
    f = float(str)
    print('int(str) = ',n)
    print('float(str) = ', f)
    print('math.pi = ', math.pi)
    print('math.e = ', math.e)
    print('math.sin(math.pi/3) = ', math.sin(math.pi/3))
    print('math.cos(math.pi/3) = ', math.cos(math.pi/3))
    print('math.tan(math.pi/3) = ', math.tan(math.pi/3))
    print('math.asin(0.5) = ', math.asin(0.5))
    print('math.acos(0.5) = ', math.acos(0.5))
    print('math.atan(0.5) = ', math.atan(0.5))
    print('math.ceil(0.6) = ', math.ceil(0.6))
    print('math.floor(0.6) = ', math.floor(0.6))
    print('math.fabs(-0.5) = ', math.fabs(-0.5))
    print('math.factorial(10) = ', math.factorial(10))
    print('math.log(64, 2) = ', math.log(64, 2))
    print('math.log2(64) = ', math.log2(64))
    print('math.log10(1000) = ', math.log10(1000))
    print('math.log1p(e**4) = ', math.log1p(math.e**4))
    print('math.pow(10, 3) = ', math.pow(10, 3))
    print()


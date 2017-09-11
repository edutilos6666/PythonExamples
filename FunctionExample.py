def example4():
    'params with optional values'
    def arithmetic_ops(x = 10 , y = 3):
        res_add = x + y
        res_subtract = x - y
        res_multiply = x * y
        res_divide = x / y
        res_modulo = x % y
        return (res_add, res_subtract, res_multiply, res_divide, res_modulo)

    res_add, res_subtract, res_multiply, res_divide, res_modulo = arithmetic_ops()
    print("res_add = ", res_add)
    print("res_subtract = ", res_subtract)
    print("res_multiply = ", res_multiply)
    print("res_divide = ", res_divide)
    print("res_modulo = ", res_modulo)
    print()

def example3():
    'function returns multiple values'
    def arithmetic_ops(x, y):
        res_add = x +y
        res_subtract = x - y
        res_multiply = x * y
        res_divide = x /y
        res_modulo = x % y
        return (res_add, res_subtract , res_multiply, res_divide , res_modulo)

    res_add, res_subtract , res_multiply, res_divide , res_modulo = arithmetic_ops(10, 3)
    print("res_add = ", res_add)
    print("res_subtract = ", res_subtract)
    print("res_multiply = ", res_multiply)
    print("res_divide = ", res_divide)
    print("res_modulo = ", res_modulo)
    print()


def example2():
    'lambda example'
    add = lambda x , y : x + y
    subtract = lambda x ,y  : x -y
    multiply = lambda x, y : x * y

    def arithmetic_statistics(x, y, fn_add, fn_subtract , fn_multiply , fn_divide):
        print("add = ", fn_add(x,y))
        print("subtract = ", fn_subtract(x,y))
        print("multiply = ", fn_multiply(x,y))
        print("divide = ", fn_divide(x,y))

    arithmetic_statistics(10.0, 3.0, add, subtract , multiply , lambda x, y : x/y)
    print()


def example1():
    'vararg example'
    def get_average(*numbers):
        sum = 0
        for n in numbers:
            sum += n
        return sum / len(numbers)


    def get_max(*numbers):
        ret = numbers[0]
        for n in numbers:
            if ret < n:
                ret = n

        return ret


    def get_min(*numbers):
        ret = numbers[0]
        for n in numbers:
            if ret > n:
                ret = n

        return ret

    avg = get_average(10, 20, 30, 40, 50)
    res_max = get_max(10, 20, 30, 40, 50)
    res_min = get_min(10, 20, 30, 40, 50)
    print("avg = ", avg)
    print("res_max = ", res_max)
    print("res_min = ", res_min)
    print()
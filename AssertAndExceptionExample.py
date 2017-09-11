def example2():
    'custom exception example'
    class CustomDivideByZeroException(Exception):
        def __init__(self, message):
            super(CustomDivideByZeroException, self).__init__(message)

    def safe_divide(n1, n2):
        if n2 == 0:
            raise CustomDivideByZeroException("n2 is zero")
        else:
            ret = n1 / n2
        return ret

    try:
        ret = safe_divide(10, 3)
        print("10 / 3 = ", ret)
    except CustomDivideByZeroException as err:
        print(err)
    finally:
        print("finally block for the first safe_divide()")

    try:
        ret = safe_divide(10, 0)
        print("10/3 = ", ret)
    except CustomDivideByZeroException as err:
        print(err)
    finally:
        print("finally block for the second safe_divide()")

    print()

def example1():
    'assert example'
    id, name , age, wage, active = 1, "foo", 10, 100.0, True
    assert (id == 1), "id is not 1"
    assert (name == "foo") , "name is not foo"
    assert (age>= 10 and age <= 100) , "age is not in [10,100]"
    assert(wage >=100.0 and wage <= 1000.0), "wage is not in [100.0, 1000.0]"
    assert (active == True) , "active is not True"
    print("All asserts passed.")
    print()
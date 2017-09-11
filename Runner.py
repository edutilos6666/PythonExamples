import Example1
import InheritanceExample
import WorkerExample
import ComplexNumberExample
import OperatorOverloadingExample
import OperatorsExample
import DecisionMakingExample
import LoopExample
import NumberExample
import StringExample
import ListExample
import TupleExample
import DictExample
import DateTimeExample
import FunctionExample
import IOExample
import AssertAndExceptionExample
import RegexpExample
import MysqlClientExample


def test_Example1():
    x, y = 10.0, 3.0
    res_add = Example1.add(x, y)
    res_subtract = Example1.subtract(x, y)
    res_multiply = Example1.multiply(x,y)
    res_divide = Example1.divide(x,y)
    res_modulo = Example1.modulo(x,y)

    print('add = ', res_add)
    print('subtract = ', res_subtract)
    print('multiply = ', res_multiply)
    print('divide = ', res_divide)
    print('modulo = ', res_modulo)

    print('<<SimpleMath>>')
    sm = Example1.SimpleMath(x, y)
    res_add = sm.add()
    res_subtract = sm.subtract()
    res_multiply = sm.multiply()
    res_divide = sm.divide()
    res_modulo = sm.modulo()

    print('add = ', res_add)
    print('subtract = ', res_subtract)
    print('multiply = ', res_multiply)
    print('divide = ', res_divide)
    print('modulo = ', res_modulo)

    #getattr, hasattr , setattr , delattr
    print('hasattr(x) = ', hasattr(sm, 'x'))
    print('getattr(x) = ', getattr(sm, 'x'))
    setattr(sm , 'x', 100)
    print('getattr(x) after setattr(x, 100) = ',getattr(sm, 'x'))
    delattr(sm , 'x')
    print('hasattr(x) after delattr(x) = ', hasattr(sm, 'x'))


    # __dict__ , __doc__ , __name__,  __module__, __bases__
    print('dict = ', Example1.SimpleMath.__dict__)
    print('doc = ', Example1.SimpleMath.__doc__)
    print('name = ', Example1.SimpleMath.__name__)
    print('module = ', Example1.SimpleMath.__module__)
    print('bases = ', Example1.SimpleMath.__bases__)


def test_InheritanceExample():
    cf1 = InheritanceExample.CustomFile('foo.read')
    cf2 = InheritanceExample.CustomFile('foo.write')
    cf3 = InheritanceExample.CustomFile('foo.exe')
    cf4 = InheritanceExample.CustomFile('foo.read.write.exe')

    print('<< ',  cf1.fileName, ' infos >>')
    print('readable = ', cf1.is_readable())
    print('writable = ', cf1.is_writable())
    print('executable = ', cf1.is_executable())
    cf1.read()
    cf1.write()
    cf1.execute()
    print()

    print('<< ',  cf2.fileName, ' infos >>')
    print('readable = ', cf2.is_readable())
    print('writable = ', cf2.is_writable())
    print('executable = ', cf2.is_executable())
    cf2.read()
    cf2.write()
    cf2.execute()
    print()

    print('<< ',  cf3.fileName, ' infos >>')
    print('readable = ', cf3.is_readable())
    print('writable = ', cf3.is_writable())
    print('executable = ', cf3.is_executable())
    cf3.read()
    cf3.write()
    cf3.execute()
    print()

    print('<< ',  cf4.fileName, ' infos >>')
    print('readable = ', cf4.is_readable())
    print('writable = ', cf4.is_writable())
    print('executable = ', cf4.is_executable())
    cf4.read()
    cf4.write()
    cf4.execute()
    print()



def test_InheritanceExample2():
    book = InheritanceExample.Book('title1', 100.0)
    book.display()
    print(book)

    print()
    novel = InheritanceExample.Novel('title2', 200.0, 'author2')
    novel.display()
    print(novel)



def test_WorkerExample():
    workerDAO = WorkerExample.WorkerDAOImpl()
    workerDAO.save(WorkerExample.Worker(1, "foo", 10, 100.0, True))
    workerDAO.save(WorkerExample.Worker(2, "bar", 20, 200.0, False))
    workerDAO.save(WorkerExample.Worker(3, "bim", 30, 300.0 , True))
    all = workerDAO.find_all()
    print('<<all workers>>')
    for w in all:
        print(w)

    print()
    workerDAO.update(1, WorkerExample.Worker(1, "new_foo", 66, 666.6, False))
    one = workerDAO.find_by_id(1)
    print('one = ', one)

    workerDAO.remove(1)
    all = workerDAO.find_all()
    print('<<all workers after remove by 1>> ')
    for w in all:
        print(w)

    print()


def test_ComplexNumberExample():
    cn1 , cn2 = ComplexNumberExample.ComplexNumber(3,3) , ComplexNumberExample.ComplexNumber(2,2)
    cn_add = cn1.add(cn2)
    cn_subtract = cn1.subtract(cn2)
    cn_multiply = cn1.multiply(cn2)
    cn_multiply_by2 = cn1.multiply_by_factor(2)
    cn_divide = cn1.divide(cn2)
    cn_divide_by2 = cn1.divide_by_factor(2)
    print('cn1 = ' + str(cn1))
    print('cn2 = '+ str(cn2))
    print('cn1 + cn2 = ' + str(cn_add))
    print('cn1 - cn2 = '+ str(cn_subtract))
    print('cn1 * cn2 = ' + str(cn_multiply))
    print('cn1 * 2 = ' + str(cn_multiply_by2))
    print('cn1 / cn2 = '+ str(cn_divide))
    print('cn1 / 2 = '+ str(cn_divide_by2))
    print()
    print('cn1 + cn2 = ' + str(cn1+cn2))
    print('cn1 - cn2 = ' + str(cn1-cn2))
    print('cn1 * cn2 = ' + str(cn1*cn2))
    print('cn1 / cn2 = ' + str(cn1/cn2))




def test_OperatorOverloadingExample():
    b1 = OperatorOverloadingExample.Box(3,3,3)
    b2 = OperatorOverloadingExample.Box(2,2,2)
    print('b1 = ', str(b1))
    print('b2 = ', str(b2))
    print('b1 + b2 = ' , str(b1+ b2))
    print('b1 - b2 = ', str(b1 -b2))
    print('b1 * b2 = ', str(b1*b2))
    print('b1 / b2 = ', str(b1/b2))
    print('b1 % b2 = ', str(b1%b2))
    print('b1 == b2 = ', str(b1 == b2))
    print('b1 != b2 = ', str(b1 != b2))
    print('b1 < b2 = ', str(b1 < b2))
    print('b1 <= b2 = ', str(b1 <= b2))
    print('b1 > b2 = ', str(b1 > b2))
    print('b1 >= b2 = ', str(b1 >= b2))



def test_OperatorsExample():
    OperatorsExample.arithmeticOps()
    OperatorsExample.comparisonOps()
    OperatorsExample.logicalOps()



def test_DecisionMakingExample():
    DecisionMakingExample.example1()



def test_LoopExample():
    LoopExample.example1()
    LoopExample.example2()
    LoopExample.example3()
    LoopExample.example4()


def test_NumberExample():
    NumberExample.example1()
    NumberExample.example2()


def test_StringExample():
    StringExample.example1()
    StringExample.example2()
    StringExample.example3()
    StringExample.example4()


def test_ListExample():
    ListExample.example1()
    ListExample.example2()
    ListExample.example3()



def test_TupleExample():
    TupleExample.example1()


def test_DictExample():
    DictExample.example1()


def test_DateTimeExample():
    DateTimeExample.example1()
    DateTimeExample.example2()
    DateTimeExample.example3()
    DateTimeExample.example4()
    DateTimeExample.example5()
    DateTimeExample.example6()
    DateTimeExample.example7()
    DateTimeExample.example8()
    DateTimeExample.example9()

def test_FunctionExample():
    FunctionExample.example1()
    FunctionExample.example2()
    FunctionExample.example3()
    FunctionExample.example4()


def test_IOExample():
    # IOExample.example1()
    IOExample.example2()



def test_AssertAndExceptionExample():
    AssertAndExceptionExample.example1()
    AssertAndExceptionExample.example2()


def test_RegexpExample():
    RegexpExample.example1()
    RegexpExample.example2()
    RegexpExample.example3()


def test_MysqlClientExample():
    MysqlClientExample.example1()
    MysqlClientExample.example2()


def main():
    # test_Example1()
    # test_InheritanceExample()
    # test_InheritanceExample2()
    # test_WorkerExample()
    # test_ComplexNumberExample()
    # test_OperatorOverloadingExample()
    # test_OperatorsExample()
    # test_DecisionMakingExample()
    # test_LoopExample()
    # test_NumberExample()
    # test_StringExample()
    # test_ListExample()
    # test_TupleExample()
    # test_DictExample()
    # test_DateTimeExample()
    # test_FunctionExample()
    # test_IOExample()
    # test_AssertAndExceptionExample()
    # test_RegexpExample()
    test_MysqlClientExample()

if __name__ == '__main__':
    main()



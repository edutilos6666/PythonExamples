
def example3():
    n1 = [10 , 20, 30]
    n2 = [20 , 30, 40]
    print("n1 = ", n1)
    print("n2 = ", n2)
    res = True if(n1 > n2) else False
    print("n1 > n2 = ", res)
    res = True if(n1 < n2) else False
    print("n1 < n2 = ", res)
    n1.extend(n2)
    print("n1 (after extend) = ", n1)
    n1.reverse()
    print("n1 (after reverse) = ", n1)
    n1.sort()
    print("n1 (after sort) = ", n1)
    print()



def example2():
    numbers = [10, 20, 30, 40]
    numbers.insert(1, "foo")
    print("numbers (after insert 1, foo) = ", numbers)
    numbers.remove(30)
    print("numbers (after remove 30) = ", numbers)
    names = ["edu", "tilos", "pako"]
    names.extend(numbers)
    print("names = ", names)
    numbers = [10, 20, 10, 30, 10]
    print("numbers.count(10) = ", numbers.count(10))
    numbers = [10, 20, 30, 40]
    print("numbers[1:3] = ", numbers[1:3])
    print("numbers[:3] = ", numbers[:3])
    print("numbers[3:] = ", numbers[3:])
    print("numbers.pop() = ", numbers.pop())
    print("numbers = ",numbers)
    del numbers[1]
    print("numbers (after del numbers[1]) = ", numbers)
    print()


def example1():
    numbers = []
    numbers.append(10)
    numbers.append(20)
    numbers.append(30)
    numbers.append(40)
    max(numbers)
    min(numbers)
    len(numbers)
    sum(numbers)
    avg = sum(numbers)/len(numbers)
    print("numbers = ", numbers)
    print("numbers = ", end= "")
    for n in numbers:
        print(n, end = ", ")
    print()
    print("max(numbers) = ", max(numbers))
    print("min(numbers) = ", min(numbers))
    print("len(numbers) = ", len(numbers))
    print("sum(numbers) = ", sum(numbers))
    print()
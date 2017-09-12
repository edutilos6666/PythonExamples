import math
import copy
import os , sys
import glob
import re

def example5():
    """os.listdir()"""
    # os.getenv("PYTHONPATH")
    path = sys.path
    for p in path:
        for dirpath , dirnames, filenames in os.walk(p):
            for fp in filenames:
                # print(fp)
                name ,ext = os.path.splitext(fp)
                # print(name, " and ", ext)
                # if(re.match("fake.*", name)):
                #     print(name)
                if(re.match(".*site.*", name)):
                    print(name)



    print()


def example4():
    """quicksort"""

    def concatenate(less, pivot , more):
        print(less, pivot, more)
        ret = copy.copy(less)
        ret.append(pivot)
        ret.extend(more)
        return ret

    def quicksort(arr):
        less , more = [], []
        if(len(arr) < 2):
            return arr
        pivot = arr[len(arr)//2]
        for el in arr:
            if el  < pivot :
                less.append(el)
            elif el > pivot :
                more.append(el)

        return concatenate(quicksort(less), pivot, quicksort(more))


    arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
    print("quicksort(arr) = ", quicksort(arr))
    print()



def example3():
    """fibonacci sequence"""
    arr = [1,1]
    def fibo(n):
        for i in range(n+1):
            if i > 1:
                arr.append(arr[i-1]+arr[i-2])

    def fibo_recursive(n):
        if n == 0 or n == 1 : return 1
        return fibo_recursive(n-1) + fibo_recursive(n-2)

    fibo(10)
    print("arr = ", arr)
    ret = fibo_recursive(10)
    print("fibo_recursive = ", ret)
    print()




def example2():
    def print_varargs(*args , **kwargs):
        print("args = ", args)
        print("kwargs = ", kwargs)

    print_varargs(10, "foo", True, 100.0, x = 10 , y = 20 , z = "deko")
    print()

def example1():
    def partial1(i):
        return 4*(i**2) / (4*(i**2)-1)

    def calculate_pi_wallis(upper_bound = 1000):
        prod = 1
        for i in range(upper_bound):
            partial_res = partial1(i+1)
            prod *=  partial_res

        prod *= 2
        return prod


    print("upper_bound = 1000 , pi = ", calculate_pi_wallis())
    print("upper_bound = 1000000, pi = ", calculate_pi_wallis(10**6))

    print()





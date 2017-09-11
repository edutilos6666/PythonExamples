def arithmeticOps(n1 = 10.0 , n2 = 3.0):
    res_add = n1 + n2
    res_subtract = n1 - n2
    res_multiply = n1 * n2
    res_divide = n1 / n2
    res_divide_floor = n1 // n2
    res_modulo = n1 % n2
    res_exponent = n1 ** n2
    print('<< arithmetic ops for ', str(n1), ' , ', str(n2), ' >>')
    print('n1 + n2 = ', str(res_add))
    print('n1 - n2 = ', str(res_subtract))
    print('n1 * n2 = ', str(res_multiply))
    print('n1 / n2 = ', str(res_divide))
    print('n1 // n2 = ', str(res_divide_floor))
    print('n1 % n2 = ', str(res_modulo))
    print('n1 ** n2 = ' , str(res_exponent))
    print()


def comparisonOps(n1 = 10.0, n2 = 3.0):
    res_eq = n1 == n2
    res_ne = n1 != n2
    res_lt = n1 < n2
    res_le = n1 <= n2
    res_gt = n1 > n2
    res_ge = n1 >= n2
    print('<< comparison ops for ', str(n1), ' , ', str(n2), ' >>')
    print('n1 == n2 = ', str(res_eq))
    print('n1 != n2 = ', str(res_ne))
    print('n1 < n2 = ', str(res_lt))
    print('n1 <= n2 = ', str(res_le))
    print('n1 > n2 = ', str(res_gt))
    print('n1 >= n2 = ', str(res_ge))
    print()



def logicalOps(n1 = True, n2 = False):
    res_and = (n1 and n2)
    res_or = (n1 or n2)
    res_not_n1 = (not n1)
    res_not_n2 = (not n2)
    print('<< logical ops for ', str(n1), ' , ', str(n2), ' >>')
    print('n1 and n2 = ', str(res_and))
    print('n1 or n2 = ', str(res_or))
    print('not n1 = ', str(res_not_n1))
    print('not n2 = ', str(res_not_n2))
    print()




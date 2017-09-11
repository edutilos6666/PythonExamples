def example1():
    'while example'
    i = 0
    while i <10 :
        print('number = ', str(i))
        i += 1

    print()


def example2():
    'for example'
    str = 'foobar'
    for ch in str:
        print(ch, end = ' , ')
    print()

    names = ['foo', 'bar', 'bim', 'pako']
    for name in names:
        print(name, end = ' , ')
    print()

    people = {'foo':10 , 'bar':20, 'bim':30 , 'pako':40}
    for (k,v) in people.items():
        print(k , ' => ', v)
    print()


def example3():
    'break keyword'
    count = 0
    while count < 10 :
        if count == 5 : break
        print('count = ', count)
        count += 1

    print()


def example4():
    'continue keyword'
    count = 0
    while count < 10:
        count += 1
        if count == 5 : continue
        print('count = ', count)

    print()
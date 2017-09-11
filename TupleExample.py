def example1():
    'tuple is immutable like string'
    p1 = (1, "foo", 10, 100.0, True)
    id, name, age, wage, active = p1
    print("id = ", id)
    print("name = ", name)
    print("age = ", age)
    print("wage = ", wage)
    print("active = ", active)

    p1 = (1, "foo")
    p2 = (10, 100.0, True)
    p3 = p1 + p2
    print("p3 = ", p3)
    print("id = %d , name = %s , age = %d , wage = %g , active = %r" %(p3[0], p3[1], p3[2],p3[3],p3[4]))
    pattern = "id = {0}, name = {1}, age = {2}, wage = {3}, active = {4}"
    print(pattern.format(p3[0],p3[1],p3[2],p3[3],p3[4]))

    p3 = (10, 20 , 30, 40, 50)
    print("max(p3) = ", max(p3))
    print("min(p3) = ", min(p3))
    print("len(p3) = ", len(p3))
    print("sum(p3) = ", sum(p3))
    avg = sum(p3) / len(p3)
    print("avg = %g" % (avg))

    props = dict()
    k1 = (10, 20)
    k2 = (20, 30)
    k3 = (30, 40)
    props[k1] = "foo"
    props[k2] = "bar"
    props[k3] = "bim"

    print("<<printing props>>")
    for (k,v) in props.items():
        print("%r => %s" % (k,v))

    print()


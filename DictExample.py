def example1():
    d1 = {}
    d1["foo"] = 10
    d1["bar"] = 20
    d1["bim"] = 30
    d1["pako"] = 40
    print("d1 = ", d1)
    del d1["pako"]
    print("d1 = ", d1)
    keys = d1.keys()
    values = d1.values()
    items = d1.items()
    print("<< keys >>")
    for key in keys:
        print(key)
    print("<< values >>")
    for value in values:
        print(value)
    print("<< items >>")
    for item in items:
        print(item)


    d1 = {"foo":10 , "bar":20}
    d2 = {"bim":30}
    d3 = {"pako":40}
    d1.update(d2)
    d1.update(d3)
    print("<<d1 after update>>")
    for k,v in d1.items():
        print("%s => %d" % (k,v))

    print()


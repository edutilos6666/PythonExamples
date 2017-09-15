import json



def example4():
    """Custom class"""
    class Person:
        def __init__(self, id, name, age):
            self.id , self.name, self.age = id , name, age

        def __repr__(self):
            return "Person({0},{1},{2})".format(self.id, self.name, self.age)


    def from_json(kwargs):
        ret = Person(kwargs["id"], kwargs["name"], kwargs["age"])
        return ret

    p1 = Person(1, "foo", 10)
    ret1 = json.dumps(p1.__dict__)
    print(ret1)

    # list
    p2 = Person(2, "bar", 20)
    p3 = Person(3, "bim", 30)

    l = [p1, p2, p3]
    l2 = []
    for p in l:
        l2.append(p.__dict__)

    ret2 = json.dumps(l2)
    print(ret2)

    # loading json
    p1_restored = from_json(json.loads(ret1))
    print(p1_restored)
    print()
    l_restored = json.loads(ret2)
    for p in l_restored:
        print(from_json(p))


def example3():
    """json.dumps() and json.loads() """
    data = [
        {"id": 1, "name": "foo", "age": 10},
        {"id": 2 , "name": "bar", "age": 20},
        {"id": 3, "name": "bim", "age":30}
    ]

    ret = json.dumps(data, indent = 4* ' ', sort_keys=True)
    print(ret)

    print()
    data2 = json.loads(ret)
    for row in data2:
        print(row["id"], row["name"], row["age"])




def example2():
    """json.load()"""
    with open("example1.txt") as f:
        data = json.load(f)
        print(data["id"], data["name"], data["age"], data["wage"], data["active"])

    with open("example2.txt") as f:
        data = json.load(f)
        for row in data:
            print(row["id"], row["name"], row["age"])



def example1():
    """json.dump()"""
    data = {"id": 1, "name" : "foo", "age": 10, "wage": 100.0 , "active": True}

    with open("example1.txt", "w") as f:
        json.dump(data, f)


    with open("example2.txt", "w") as f:
        row1 = {"id": 1, "name": "foo", "age": 10}
        row2 =  {"id": 2 , "name": "bar", "age": 20}
        row3  = {"id": 3, "name": "bim", "age": 30}
        data = [
            row1, row2, row3
        ]

        json.dump(data, f)





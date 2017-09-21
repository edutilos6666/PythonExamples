from pymongo import MongoClient



class Person:
    def __init__(self, id, name, age, wage, active):
        self.id = id
        self.name = name
        self.age = age
        self.wage = wage
        self.active = active


    def __repr__(self):
        return "Person({0},{1},{2},{3},{4})".format(
            self.id, self.name, self.age, self.wage, self.active
        )



def person_from_dict(props):
    return Person(props["id"], props["name"], props["age"], props["wage"], props["active"])

def example1():
    client = MongoClient("localhost", 27017)
    db = client.pymongo_db
    db.people.drop()
    people = db.people
    people.insert_one(Person(1, "foo", 10, 100.0, True).__dict__)
    one = people.find_one()
    print(person_from_dict(one))
    people.insert_many([
      Person(2, "bar", 20, 200.0, False).__dict__,
        Person(3, "bim", 30, 300.0, True).__dict__,
        Person(4, "pako", 40, 400.0, False).__dict__
    ])

    print("<<all people>>")
    for p in people.find():
        print(person_from_dict(p))

    print("<<all people with name = foo>>")
    for p in people.find({"name": "foo"}):
        print(person_from_dict(p))

    print("<<all people with age > 10>>")
    for p in people.find({"age": {"$gt": 10}}):
        print(person_from_dict(p))

    people.replace_one(Person(1, "foo", 10, 100.0, True).__dict__,
                       Person(1, "new_foo", 66, 666.6, False).__dict__)

    one = people.find_one({"id": 1})
    print("person after replace = {0}".format(person_from_dict(one)))

    people.update_one({"id": 1}, {"$set": {"name": "old_foo",
                                           "age": 55,
                                           "wage": 555.5,
                                           "active": True}})
    one = people.find_one({"id": 1})
    print("person after update = {0}".format(person_from_dict(one)))


    people.delete_one({"id": 1})
    print("<<people after delete_one>>")
    for p in people.find():
        print(person_from_dict(p))


example1()



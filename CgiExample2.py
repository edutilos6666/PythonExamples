#! /usr/bin/python3



class Person:
    def __init__(self,id, name, age, wage, active):
        self.id = id
        self.name = name
        self.age = age
        self.wage = wage
        self.active = active

    def __str__(self):
        pattern = "Person({0},{1},{2},{3},{4})"
        return pattern.format(self.id, self.name, self.age, self.wage, self.active)



class PersonDAO:
    def save(self, p):
        pass
    def update(self, id, newP):
        pass

    def remove(self, id):
        pass

    def find_by_id(self,id):
        pass

    def find_all(self):
        pass


class PersonDAOImpl(PersonDAO):
    def __init__(self):
        self.container = dict()

    def save(self, p):
        self.container[p.id] = p

    def update(self, id, newP):
        del self.container[id]
        self.container[id] = newP

    def remove(self, id):
        del self.container[id]

    def find_by_id(self, id):
        return self.container[id]

    def find_all(self):
        ret = []
        for k , v in self.container.items():
            ret.append(v)
        return ret

def generate_data():
    dao = PersonDAOImpl()
    dao.save(Person(1, "foo", 10, 100.0, True))
    dao.save(Person(2, "bar", 20, 200.0, False))
    dao.save(Person(3, "bim", 30, 300.0, True))
    dao.save(Person(4, "pako", 40, 400.0, False))
    return dao


def generate_html_table():
    dao = generate_data()
    all = dao.find_all()
    ret = "<table><tr><th>Id</th><th>Name</th><th>Age</th><th>Wage</th><th>Active</th></tr>"
    for person in all:
        pattern = "<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td></tr>"
        ret += pattern.format(person.id, person.name, person.age, person.wage, person.active)
    ret += "</table>"
    return ret


pattern = """Content-type:text/html

{0}"""

str = pattern.format(generate_html_table())

print(str)


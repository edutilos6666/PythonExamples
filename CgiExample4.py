#! /usr/bin/python3

import cgi, cgitb


class Worker:
    def __init__(self, id, name, age, wage, active):
        self.id = id
        self.name = name
        self.age = age
        self.wage = wage
        self.active = active


    def __str__(self):
        pattern = "Worker({0},{1},{2},{3},{4})"
        return pattern.format(self.id, self.name, self.age, self.wage, self.active)


container = dict()
container[1] = Worker(1, "foo", 10, 100.0, True)

def handle_request():
    form = cgi.FieldStorage()
    id = int(form.getvalue("id"))
    name = form.getvalue("name")
    age = int(form.getvalue("age"))
    wage = float(form.getvalue("wage"))
    temp = form.getvalue("active")
    active = True if(temp.lower() == "true") else False
    w = Worker(id, name, age, wage, active)
    container[id] = w


def generate_table():
    ret = "<table><tr><th>Id</th><th>Name</th><th>Age</th><th>Wage</th><th>Active</th></tr>"
    for k, v in container.items():
        pattern = "<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td></tr>"
        str = pattern.format(v.id, v.name, v.age, v.wage, v.active)
        ret += str
    ret += "</table>"
    return ret


handle_request()
pattern = """Content-type:text/html

{0}
"""
str = pattern.format(generate_table())
print(str)










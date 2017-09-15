from bs4 import BeautifulSoup
import csv



def example2():
    """exactly in example1() """
    soup = BeautifulSoup(open("../people.xml"), "lxml")
    people = soup.find_all("person")

    for person in people:
        id = person.attrs["id"]
        name = person.find("name").contents[0]
        age = person.find("age").contents[0]
        wage = person.find("wage").contents[0]
        active = person.find("active").contents[0]
        print("{0},{1},{2},{3},{4}".format(id, name, age, wage, active))



def example1():
    filename = "../people.xml"
    soup = BeautifulSoup(open(filename), "lxml")
    # print(soup.prettify())

    people = soup.find_all("person")
    # print(people)

    print()
    for person in people:
        id = person.attrs["id"]
        name = person.find("name").contents[0]
        age = person.find("age").contents[0]
        wage = person.find("wage").contents[0]
        active = person.find("active").contents[0]
        print("{0}, {1}, {2}, {3}, {4}".format(id, name, age, wage, active))


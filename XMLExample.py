import xml.sax
from xml.dom import minidom



def example3():
    'minidom.parse'
    domtree = minidom.parse("people.xml")
    root = domtree.documentElement

    persons = root.getElementsByTagName("Person")
    for person in persons:
        print("<<Person>>")
        if(person.hasAttribute("id")):
            print("id = ", person.getAttribute("id"))
        name = person.getElementsByTagName("Name")[0].childNodes[0].data
        age = person.getElementsByTagName("Age")[0].childNodes[0].data
        wage = person.getElementsByTagName("Wage")[0].childNodes[0].data
        active = person.getElementsByTagName("Active")[0].childNodes[0].data
        print("Name = ", name)
        print("Age = ", age)
        print("Wage = ", wage)
        print("Active = ", active)

        print()

    print()

def example2():
    'same as example1()'
    class PersonContentHandler(xml.sax.ContentHandler):
        def __init__(self):
            self.currentTag = None
            self.name = None
            self.age = None
            self.wage = None
            self.active = None

        def startElement(self, name, attrs):
            self.currentTag = name
            if(name == "Person"):
                print("\n*** Person***")
                id = attrs["id"]
                print("id = ", id)

        def endElement(self, name):
             if(self.currentTag == "Name"):
                 print("Name = ", self.name)
             elif(self.currentTag == "Age"):
                 print("Age = ", self.age)
             elif(self.currentTag == "Wage"):
                 print("Wage = ", self.wage)
             elif(self.currentTag == "Active"):
                 print("Active = ", self.active)

             self.currentTag = ""

        def characters(self, content):
             if(self.currentTag == "Name"):
                 self.name = content
             elif(self.currentTag == "Age"):
                 self.age = content
             elif(self.currentTag == "Wage"):
                 self.wage = content
             elif(self.currentTag == "Active"):
                 self.active = content


    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    parser.setContentHandler(PersonContentHandler())
    parser.parse("people.xml")

















def example1():
    'xml sax'
    class CustomContenHandler(xml.sax.ContentHandler):
        def __init__(self):
            self.CurrentTag = ""
            self.name = ""
            self.age = ""
            self.wage = ""
            self.active = ""

        def startElement(self, name, attrs):
            self.CurrentTag = name
            if name == "Person":
                print("\n*** Person ***")
                id = attrs["id"]
                print("id = ", id)

        def characters(self, content):
            if(self.CurrentTag == "Name"):
                self.name = content
            if(self.CurrentTag == "Age"):
                self.age = content
            if(self.CurrentTag == "Wage"):
                self.wage = content
            if(self.CurrentTag == "Active"):
                self.active = content


        def endElement(self, name):
            if(self.CurrentTag == "Name"):
                print("Name = ", self.name)
            if(self.CurrentTag == "Age"):
                print("Age = ", self.age)
            if(self.CurrentTag == "Wage"):
                print("Wage = ", self.wage)
            if(self.CurrentTag == "Active"):
                print("Active = ", self.active)
            self.CurrentTag = ""


    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    parser.setContentHandler(CustomContenHandler())
    parser.parse("people.xml")
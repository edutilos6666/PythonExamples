from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column , Integer, String, Table, Boolean , Float, BIGINT
from sqlalchemy.orm import Session , sessionmaker



def example3():
    """ with session 2"""
    path = "sqlite:///memory"
    engine = create_engine(path , echo = True)
    Base = declarative_base()

    class Person(Base):
        __tablename__ = "persons"
        id = Column(Integer, primary_key=True)
        name = Column(String, nullable=False)
        age = Column(Integer, nullable=False)
        wage = Column(Float, nullable=False)
        active = Column(Boolean, nullable=False)


        def __repr__(self):
            return "Person({0}, {1},{2},{3},{4})".format(self.id, self.name, self.age, self.wage, self.active)


    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()


    # clear all instances from table
    for instance in session.query(Person).order_by(Person.id):
        session.delete(instance)

    session.commit()

    # add some instances to the table
    session.add_all([
        Person(name = "foo", age = 10 , wage = 100.0, active= True),
        Person(name = "bar", age = 20 , wage = 200.0, active = False),
        Person(name = "bim", age = 30, wage = 300.0, active = True)
    ])

    session.commit()

    # find all
    for p in session.query(Person).order_by(Person.id):
        print(repr(p))


    session.close()
    Person.__table__.drop(engine)
    # Base.metadata.drop_all()


def example2():
    """with session"""
    engine = create_engine("sqlite:///memory", echo=True)
    Base = declarative_base()


    class User(Base):
        __tablename__ = "users"
        id = Column(Integer, primary_key=True)
        name = Column(String)
        fullname = Column(String)
        password = Column(String)

        def __repr__(self):
            return "<User(name = '%s', fullname = = '%s', password = '%s')>" % (self.name, self.fullname, self.password)

    Base.metadata.create_all(engine)
    ed_user = User(name="ed", fullname="Ed Jones", password="foo")

    Session = sessionmaker(bind=engine)
    # Session.configure(bind=engine)
    session = Session()

    for instance in session.query(User).order_by(User.id):
        session.delete(instance)

    session.commit()

    session.add(ed_user)

    our_user = session.query(User).filter_by(name = "ed").first()
    print("our_user = ", our_user)

    print("session.dirty = ", session.dirty)

    session.add_all([
        User(name = "wendy", fullname = "Wendy Williams", password = "foobar"),
        User(name = "mary", fullname = "Mary Contrary", password = "xxg527"),
        User(name = "fred", fullname = "Fred Flinstone", password = "blah")
    ])

    ed_user.password = "bim"
    print("session.dirty = ", session.dirty)
    print("session.new = ", session.new)
    session.commit()
    print("<<after commit>>")
    print("session.dirty = ", session.dirty)
    print("session.new = ", session.new)

    # query
    print("<<All users>>")
    for instance in session.query(User).order_by(User.id):
        print(instance.id, instance.name , instance.fullname)


    session.close()





def example1():
    engine = create_engine("sqlite:///memory", echo=True)
    Base = declarative_base()

    class User(Base):
        __tablename__ = "users"
        id = Column(Integer, primary_key =True)
        name = Column(String)
        fullname = Column(String)
        password = Column(String)

        def __repr__(self):
            return "<User(name = '%s', fullname = = '%s', password = '%s')>" % (self.name, self.fullname,self.password )

    Base.metadata.create_all(engine)

    ed_user = User(name = "ed", fullname = "Ed Jones", password = "foo")
    print(repr(ed_user))
from decimal import Decimal
from datetime import datetime
from pony.converting import str2datetime
from pony.orm import *


def example2():
    db = Database()
    class Person(db.Entity):
        id = PrimaryKey(int , auto=False)
        name = Required(str)
        age = Required(int)
        wage = Required(float)
        active = Required(bool)

        def __repr__(self):
            return "Person({0},{1},{2},{3},{4})".format(self.id, self.name, self.age, self.wage, self.active)


    sql_debug(False)
    driver_name = "sqlite"
    path = "dbs/example1.sqlite"

    db.bind(driver_name, path, create_db= True)
    db.generate_mapping(create_tables=True)

    # delete all
    with db_session:
        all = Person.select()
        for p in all:
            p.delete()


    with db_session:
        Person(id = 1, name = "foo", age = 10 , wage = 100.0, active = True)
        Person(id = 2, name = "bar", age = 20, wage = 200.0, active = False)
        Person(id = 3,name = "bim", age = 30, wage = 300.0, active = True)

    # commit()

    with db_session:
        all = Person.select()
        print("<all people>>")
        for p in all:
            print(p)


    # update
    with db_session:
        one = Person.select(lambda p: p.id == 1).first()
        one.name = "new_foo"
        one.age = 66
        one.wage = 666.6
        one.active = False

    with db_session:
        one = Person.select(lambda p: p.id == 1).first()
        print("after update = ", one)


    print()
    with db_session:
        all = Person.select_by_sql("SELECT * FROM Person")
        print("<<all>>")
        for p in all:
            print(p)


    print()
    with db_session:
        second = select(p for p in Person if p.id == 2 and p.name == "bar"
                        and (p.age > 10 and p.age < 30) and p.wage == 200.0 and  not(p.active)).first()
        print("second = ", second)





def example1():
    db = Database()
    class Customer(db.Entity):
        email = Required(str, unique=True)
        password = Required(str)
        name = Required(str)
        country  = Required(str)
        address = Required(str)
        cart_items = Set("CartItem")
        orders = Set("Order")

    class Product(db.Entity):
        id = PrimaryKey(int , auto=True)
        name = Required(str)
        categories= Set("Category")
        description = Optional(str)
        picture = Optional(buffer)
        price = Required(Decimal)
        quantity = Required(int)
        cart_items = Set("CartItem")
        order_items = Set("OrderItem")

    class CartItem(db.Entity):
        quantity = Required(int)
        customer = Required(Customer)
        product = Required(Product)

    class OrderItem(db.Entity):
        quantity = Required(int)
        price = Required(Decimal)
        order = Required("Order")
        product = Required(Product)
        PrimaryKey(order, product)

    class Order(db.Entity):
        id = PrimaryKey(int, auto=True)
        state = Required(str)
        date_created = Required(datetime)
        date_shipped = Optional(datetime)
        date_delivered = Optional(datetime)
        total_price = Required(Decimal)
        customer = Required(Customer)
        items = Set(OrderItem)

    class Category(db.Entity):
        name = Required(str, unique =True)
        products = Set(Product)

    from datetime import date
    class Person(db.Entity):
        id = PrimaryKey(int)
        name = Required(str)
        age = Required(int)
        dob = Required(date)

    sql_debug(True)
    db.bind("sliqte", "estore.sqlite", create_db=True)
    db.generate_mapping(create_tables=True)

    db.generate_mapping(create_tables=True)

    with db_session:
        Person(id=1, name="Jogn", age=30, dob=date(1986, 1, 1))
        Person(id=2, name="Mike", age=32, dob=date(1984, 5, 20))
        Person(id=3, name="Mary", age=20, dob=date(1996, 2, 15))





    # fill tables with data

    # now queries
    # All USA customers
    Customer.select(lambda c:c.country == "USA")
    # The number of customers for each country
    select((c.country, count(c)) for c in Customer)
    # max product price
    max(p.price for p in Product)
    # Max SSD price
    max(p.price for p in Product
                for cat in p.categories if cat.name == "Solid State Drives")
    # Three most expensive products
    Product.select().order_by(desc(Product.price))[:3]
    # Out of stock products
    Product.select(lambda p: p.quantity == 0)
    # Most popular product
    Product.select().order_by(lambda p:desc(sum(p.order_items.quantity))).first()

    # Products that have never been ordered
    Product.select(lambda p: not p.order_items)

    # Customers who made several orders
    Customer.select(lambda c: count(c.orders) > 1)

    # Three most valuable customers
    Customer.select().order_by(lambda c: desc(sum(c.orders.total_price)))[:3]

    # Customers whose orders were shipped
    Customer.select(lambda c: SHIPPED in c.orders.state)

    # Customers with no orders
    Customer.select(lambda c : not c.orders)

    # The same query with the LEFT JOIN instead of NOT EXISTS
    left_join(c for c in Customer for o in c.orders if o is None)

    # Customers which ordered several different tablets
    select(c for c in Customer
           for p in c.orders.items.product
           if "Tables" in p.categories.name and count(p) > 1)

    # using date and time in queries
    select(o for o in Order if o.date_craeted >= datetime.now() - timedelta(days=3))[:]

    select(o for o in Order if o.date_created + timedelta(days=3) >= datetime.now())[:]

    # raw_sql()
    select(m for m in DBVoteMessage if m.date >= raw_sql("NOW() - '1 minute'::INTERVAL"))

    select(o for o in Order if o.date_created.month == 12)

    # retrieving objects with a criteria
    Person.select(lambda p:p.age > 20 and p.name == "John")

    # retrieving object attributes
    select(p.name for p in Person)

    # aggregate query
    select((p.name, count(p)) for p in Person)

    # using joins
    select(p for p in Person for c in p.cars if c.make in ("Toyota", "Honda"))

    # without distinct
    select(p for p in Person for c in p.cars
           if c.make in ("Toyota", "Honda")).without_distinct()

    select((p, c) for p in Person for c in p.cars if c.make in ("Toyota", "Honda"))

    """
    functions which can be used insidde a query
    avg()
    abs()
    exists()
    len()
    max()
    min()
    count()
    concat()
    random()
    raw_sql()
    select()
    sum()
    getattr()
    """
    select(avg(c.orders.total_price) for c in Customer)

    select(o for o in Order if o.customer in
           select(c for c in Customer if c.name.startswith("A")))[:]

    # using getattr()
    attr_name = "name"
    param_value = "John"
    select(c for c in Customer if getattr(c, attr_name) ==  param_value)





    # using raw_sql()
    select(p for p in Person if raw_sql('abs("p"."age") > 25'))

    q = Person.select(lambda x:raw_sql('abs("x"."age")') > 25)
    print(q.get_sql())

    x = 25
    select(p for p in Person if raw_sql('abs("p"."age") > $x'))

    x = 1
    s = 'p.id > $x'
    select(p for p in Person if raw_sql(s))

    x = 1
    cond = raw_sql('p.id > $x')
    select(p for p in Person if cond)

    x = date(1990, 1, 1)
    select(p for p in Person if raw_sql('p.dob < $x'))

    x = 10
    y = 15
    select(p for p in Person if raw_sql('p.age > $(x+y)'))

    select(p for p in Person if raw_sql('p.dob < $date.today()'))

    names = select(raw_sql('UPPER(p.name)') for p in Person)[:]
    print(names)

    dates = select(raw_sql('(p.dob)') for p in Person)[:]
    print(dates)

    dates = select(raw_sql('(p.dob)', result_type=date) for p in Person)[:]
    print(dates)

    x = 25
    select(p for p in Person).filter(lambda p:p.age > raw_sql('$x'))
    x = 25
    Person.select().filter(raw_sql('p.age > $x'))

    x = "123"
    y = "John"
    Person.select(lambda p: raw_sql("UPPER(p.name) || $x")
                  == raw_sql("UPPER($y||'123')"))

    x = 10
    y = 31
    q = select(p for p in Person if p.age > x and p.age < raw_sql('$y'))
    x = date(1980, 1, 1)
    y = "j"
    q = q.filter(lambda p :p.dob > x and p.name.startswith(raw_sql('UPPER($y)')))
    persons = q[:]

    x = 9
    Person.select().order_by(lambda p: raw_sql('SUBSTR(p.dob, $x)'))

    x = 9
    Person.select().order_by(raw_sql('SUBSTR(p.dob , $x)'))


    Product.select_by_sql("SELECT * FROM Products")

    x = 1000
    y = 500
    Product.select_by_sql("SELECT * FROM Product WHERE price > $x OR price = $(y *2)")

    Product.select_by_sql("SELECT * FROM Product WHERE price > $x OR price = $(y*2)",
                          globals = {"x": 100}, locals= {"y":200})









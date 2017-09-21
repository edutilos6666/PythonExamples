import MySQLdb
'''
installing mysqlclient:
 sudo pip3 install mysqlclient
'''


def example2():
    'OOP style'
    class Worker:
        def __init__(self, id, name, age, wage, active):
            self.id = id
            self.name = name
            self.age = age
            self.wage = wage
            self.active = active

        def __str__(self):
            return "Worker({0},{1},{2},{3},{4})".format(
                self.id, self.name, self.age , self.wage , self.active
            )

    class WorkerDAOImpl:
        def __init__(self):
            self.hostname = "localhost"
            self.username , self.password = "root", "root"
            self.dbname , self.tablename = "test2", "Worker2"
            self.db , self.cursor = None , None

        def connect(self):
            self.db = MySQLdb.connect(self.hostname, self.username, self.password, self.dbname)
            self.db.autocommit(on = True)
            self.cursor = self.db.cursor()

        def disconnect(self):
            if self.db != None :
                self.db.close()

        def drop_table(self):
            self.connect()
            sql = "drop table if exists {0}".format(self.tablename)
            self.cursor.execute(sql)
            self.disconnect()

        def create_table(self):
            self.connect()
            sql = """create table if not exists {0} (
id bigint primary key , 
name varchar(50) not null, 
age int not null, 
wage double not null, 
active boolean not  null)""".format(self.tablename)
            self.cursor.execute(sql)
            self.disconnect()

        def save(self, w):
            self.connect()
            sql = """insert into {0} VALUES({1}, "{2}", {3}, {4}, {5})""".format(
                self.tablename, w.id, w.name, w.age, w.wage, w.active
            )
            self.cursor.execute(sql)
            self.disconnect()


        def update(self, id, newW):
            self.connect()
            sql = """update {0} set name = "{1}",age ={2}, wage = {3}, active = {4}  where id = {5}""".format(
                self.tablename, newW.name, newW.age , newW.wage, newW.active , id
            )

            self.cursor.execute(sql)
            self.disconnect()


        def remove(self, id):
            self.connect()
            sql = """delete from {0} where id = {1}""".format(self.tablename, id)
            self.cursor.execute(sql)
            self.disconnect()


        def find_by_id(self, id):
            ret = None
            self.connect()
            sql = """select * from {0} where id = {1}""".format(self.tablename, id)
            self.cursor.execute(sql)
            row = self.cursor.fetchone()
            self.disconnect()
            id = int(row[0])
            name = row[1]
            age = int(row[2])
            wage = float(row[3])
            temp = row[4]
            active = True if(temp == 1) else False
            ret = Worker(id , name, age, wage, active)
            return ret

        def find_all(self):
            ret = []
            self.connect()
            sql = "select * from {0}".format(self.tablename)
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            self.disconnect()

            for row in rows:
                id = int(row[0])
                name = row[1]
                age = int(row[2])
                wage = float(row[3])
                temp = row[4]
                active = True if (temp == 1) else False
                ret.append(Worker(id, name, age, wage, active))


            return ret



    dao = WorkerDAOImpl()
    # dao.connect()
    dao.drop_table()
    dao.create_table()
    dao.save(Worker(1, "foo", 10, 100.0, True))
    dao.save(Worker(2, "bar", 20, 200.0 , False))
    dao.save(Worker(3, "bim", 30, 300.0, True))
    dao.save(Worker(4, "pako", 40, 400.0, False))
    all = dao.find_all()
    print("<<all workers>>")
    for worker in all:
        print(str(worker))


    dao.update(1, Worker(1, "new_foo", 66, 666.6, False))
    one = dao.find_by_id(1)
    print("one after update = ", one)

    dao.remove(1)
    all = dao.find_all()
    print("<<all workers after remove(1)>>")
    for worker in all:
        print(worker)

    # dao.disconnect()
    print()



def example1():
    'with list and tuple instead of class'
    hostname , username, password , dbname = "localhost", "root", "root", "test2"
    tablename = "Worker"
    db =  MySQLdb.connect(hostname, username, password, dbname)
    print("connection success!")
    db.autocommit(on=True)

    # get cursor from db
    cursor = db.cursor()

    # drop table if exists
    sql = "drop table if exists {0}".format(tablename)
    cursor.execute(sql)

    # create table if not exists
    sql = """create table if not exists {0} (
id bigint primary key , 
name varchar(50) not null, 
age int not null, 
wage double not null, 
active boolean not null ) """.format(tablename)
    cursor.execute(sql)

    # insert some values
    workers = dict()
    workers[1] = (1, "foo", 10 ,100.0, True)  # we can mix list and tuple here :)
    workers[2] = [2, "bar", 20 , 200.0, False]
    workers[3] = [3, "bim", 30, 300.0, True]
    workers[4] = [4, "pako", 40, 400.0, False]

    pattern = """insert into {0} VALUES({1}, "{2}",{3},{4},{5})"""
    for k , worker in workers.items():
        sql = pattern.format(tablename, worker[0], worker[1], worker[2], worker[3], worker[4])
        cursor.execute(sql)


    # select all values
    sql = """select * from {0}""".format(tablename)
    cursor.execute(sql)
    all = cursor.fetchall()
    for row in all:
        pattern = "{0}, {1},{2},{3},{4}".format(row[0], row[1], row[2],row[3],row[4])
        print(pattern)


    db.close()




    print()
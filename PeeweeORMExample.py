import peewee
import datetime


path = "dbs/peewee_example2.sqlite"
database = peewee.SqliteDatabase(path)
def example2():


    class Person(peewee.Model):
        id = peewee.PrimaryKeyField()
        name = peewee.CharField()
        age = peewee.IntegerField()
        wage = peewee.DoubleField()
        active = peewee.BooleanField()

        class Meta:
            database = database


        def __repr__(self):
            return "Person({0},{1},{2},{3},{4})".format(
                self.id, self.name, self.age, self.wage, self.active
            )

    try:
        Person.create_table()
    except peewee.OperationalError as err:
        print("err = ", err)


    people_list = [
        {
            "id": 1 ,
         "name": "foo",
         "age": 10,
         "wage": 100.0,
         "active": True
        },
        {
          "id": 2 ,
            "name": "bar",
            "age": 20,
            "wage": 200.0,
            "active": False
        },
        {
            "id": 3,
            "name": "bim",
            "age":30 ,
            "wage": 300.0 ,
            "active": True
        },
        {
            "id":4,
            "name": "pako",
            "age": 40,
            "wage":400.0,
            "active": False
        }

    ]

    # for person in people_list:
    #     Person.create(**person)

    # insert one
    Person.create(id = 5, name = "messi", age = 29 , wage = 1000.0, active = True)

    # bulk insert
    Person.insert_many(people_list).execute()

    print("<< all people>>")
    for person in Person.select():
        print(person)


    print()
    # update
    first = Person.get(Person.id == 1)
    first.name = "new_foo"
    first.age = 66
    first.wage = 666.6
    first.active = False
    first.save()

    first = Person.get(Person.id == 1)
    print("first after update = ", first)

    # delete
    second = Person.get(Person.id == 2)
    second.delete_instance()

    print("<<all people after delete>>")
    for person in Person.select():
        print(person)

    # clear up the table
    for person in Person.select():
        person.delete_instance()


def example1():
    path = "dbs/peewee_example1.sqlite"
    database = peewee.SqliteDatabase(path)

    class Artist(peewee.Model):
        name = peewee.CharField()

        class Meta:
            database = database



    class Album(peewee.Model):
        artist = peewee.ForeignKeyField(Artist)
        title = peewee.CharField()
        release_date= peewee.DateTimeField()
        publisher = peewee.CharField()
        media_type = peewee.CharField()

        class Meta:
            database = database



    try:
        Artist.create_table()
    except peewee.OperationalError:
        print("Artist table already exists!")


    try:
        Album.create_table()
    except peewee.OperationalError:
        print("Album table already exists!")



    new_artist = Artist.create(name="Newsboys")
    album_one = Album(artist=new_artist,
                      title="Read All About it",
                      release_date = datetime.date(1988, 12, 1),
                      publisher = "Refuge",
                      media_type = "CD")

    album_one.save()

    albums = [{"artist":new_artist,
               "title": "Hell is for Wimps",
               "release_date": datetime.date(1990, 7, 31),
               "publisher":"Sparrow",
               "media_type": "CD"},
              {"artist": new_artist,
               "tile": "Love Liberty Disco",
               "release_date": datetime.date(1999, 11, 16),
               "publisher": "Sparrow",
               "media_type": "CD"},
              {"artist": new_artist,
               "title": "Thrive",
               "release_date": datetime.date(2002, 3, 26),
               "publisher": "Sparrow",
               "media_type": "CD"}
              ]

    for album in albums:
        a = Album(**album)
        a.save()

    bands = ["MXPX", "Kutless", "Thousand Foot Krutch"]
    for band in bands:
        artist = Artist.create(name=band)
        artist.save()


    # or insert all at once
    Album.insert_many(albums).execute()


    # basic queries
    band = Artist.select().where(Artist.name == "Kutless").get()
    print(band.name)

    # shortcut method
    band = Artist.get(Artist.name == "Kutless")
    print(band.name)

    band.name = "Beach Boys"
    band.save()

    album = Album.select().join(Artist).where(
        (Album.title == "Thrive") & (Artist.name == "Newsboys")
    ).get()
    album.title= "Steup Up to the Microphone"
    album.save()



    query = Album.select().join(Artist)
    qry_filter = (Album.title == "Step Up to the Microphone") & (Artist.name == "Newyboys")
    album = query.where(qry_filter).get()



    # delete record in peewee
    band = Artist.get(Artist.name == "MXPX")
    band.delete_instance()


class Book:
    def __init__(self, title , price):
        self.title = title
        self.price = price
        self.delim = ' , '

    def display(self):
        print('<<book info>>')
        print('title = ', self.title)
        print('price = ', self.price)


    def __repr__(self):
        return self.title + self.delim + str(self.price)

class Novel(Book):
    def __init__(self, title, price, author):
        super(Novel, self).__init__(title, price)
        self.author = author

    def display(self):
        print('<<novel info>>')
        print('title = ', self.title)
        print('price = ', self.price)
        print('author = ', self.author)


    def __repr__(self):
        return super(Novel, self).__repr__() + self.delim + self.author


class Writable:
    def is_writable(self):
        pass
    def write(self):
        pass


class Readable:
    def is_readable(self):
        pass

    def read(self):
        pass


class Executable:
    def is_executable(self):
        pass

    def execute(self):
        pass



class CustomFile(Readable, Writable, Executable):
    def __init__(self, fileName):
        self.fileName = fileName

    def is_readable(self):
        return '.read' in self.fileName

    def read(self):
        if self.is_readable():
            print(self.fileName, ' was read.')
        else:
            print(self.fileName, ' is not readable.')

    def is_writable(self):
        return '.write' in self.fileName

    def write(self):
        if self.is_writable():
            print(self.fileName , ' was written.')
        else:
            print(self.fileName, ' is not writable.')

    def is_executable(self):
        return '.exe' in self.fileName

    def execute(self):
        if self.is_executable():
            print(self.fileName, ' was executed.')
        else:
            print(self.fileName, ' is not executable.')

    def __repr__(self):
        return self.fileName
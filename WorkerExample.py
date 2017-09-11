class Worker:
    def __init__(self, id, name, age, wage, active):
        self.id = id
        self.name = name
        self.age = age
        self.wage = wage
        self.active = active
        self.delim = ' , '

    def __repr__(self):
        return 'Worker(' + str(self.id) + self.delim + \
            self.name + self.delim + \
            str(self.age) + self.delim + \
            str(self.wage) + self.delim + \
            str(self.active)  + ')'


class WorkerDAO:
    def save(self, w):
        pass

    def update(self, id , newW):
        pass

    def remove(self, id):
        pass

    def find_by_id(self, id):
        pass


    def find_all(self):
        pass


class WorkerDAOImpl(WorkerDAO):
    def __init__(self):
        self.container = dict()

    def save(self, w):
        self.container[w.id] = w

    def update(self, id, newW):
        del self.container[id]
        self.container[newW.id] = newW

    def remove(self, id):
        del self.container[id]

    def find_by_id(self, id):
        return self.container[id]


    def find_all(self):
        ret = []
        for id, w in self.container.items():
            ret.append(w)

        return ret


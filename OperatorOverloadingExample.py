class Box:
    def __init__(self, width=0 , height= 0, depth = 0):
        self.width, self.height , self.depth = width , height, depth
        self.delim = ' , '

    def __str__(self):
        return 'Box('+ str(self.width)+ self.delim + \
            str(self.height) + self.delim + \
            str(self.depth) + ')'


    def volume(self):
        return self.width * self.height * self.depth

    def __add__(self, other):
        ret = Box()
        ret.width = self.width + other.width
        ret.height = self.height + other.height
        ret.depth = self.depth + other.depth
        return ret

    def __sub__(self, other):
        ret = Box()
        ret.width = self.width - other.width
        ret.height = self.height - other.height
        ret.depth = self.depth - other.depth
        return ret


    def __mul__(self, other):
        ret = Box()
        ret.width = self.width * other.width
        ret.height = self.height * other.height
        ret.depth = self.depth * other.depth
        return ret


    def __truediv__(self, other):
        ret = Box()
        ret.width = self.width / other.width
        ret.height = self.height/ other.height
        ret.depth = self.depth / other.depth
        return ret


    def __mod__(self, other):
        ret = Box()
        ret.width = self.width % other.width
        ret.height = self.height % other.height
        ret.depth = self.depth % other.depth
        return ret


    def __eq__(self, other):
        v1 , v2 = self.volume(), other.volume()
        return v1 == v2

    def __ne__(self, other):
        v1, v2 = self. volume(), other.volume()
        return v1 != v2

    def __lt__(self, other):
        v1, v2 = self.volume(), other.volume()
        return v1 < v2

    def __le__(self, other):
        v1 , v2 = self.volume(), other.volume()
        return v1 <= v2


    def __gt__(self, other):
        v1, v2 = self.volume(), other.volume()
        return v1 > v2

    def __ge__(self, other):
        v1, v2 = self.volume(), other.volume()
        return v1 >= v2

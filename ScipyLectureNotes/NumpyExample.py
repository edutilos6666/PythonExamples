import numpy as np
import time  # for np.random.seed()
from matplotlib import pyplot as plt
from scipy import misc

from PyQt5 import QtCore



def example27():
    """ data statistics"""
    data = np.loadtxt("populations.txt")
    year , hares, lynxes , carrots = data.T
    # year = np.int64(year)
    plt.axes([0.2, 0.1, 0.5, 0.8])
    plt.plot(year, hares, year, lynxes, year, carrots)
    plt.legend(("Hare", "Lynx", "Carrot"), loc=(1.05, 0.5))

    print("mean populations over time = ", end = "")
    populations = data[:, 1:]
    print(populations.mean(axis=0))

    print("sample standard deviations = ", end = "")
    print(populations.std(axis=0))

    print("Which species has the highest population each year = ", end ="")
    print(np.argmax(populations, axis = 1))

    plt.show()



def example26():
    """create face_locket """
    face = misc.face(gray=True)  #scipy provides this racoo image by default
    sy , sx = face.shape
    y , x = np.ogrid[0:sy, 0:sx]  # x and y indices of pixels
    print(y.shape, x.shape)
    centerx, centery = (660, 300) # racoon's face is located in this coordinate
    mask = ((y-centery)**2 + (x-centerx)**2) > 230**2
    face[mask] = 0 # set these bits to 0 -> black
    plt.imshow(face, cmap=plt.cm.gray)
    plt.show()


def example25():
    """
generate following: 

[[1, 6,11],
[2, 7,12],
[3, 8,13],
[4, 9,14],
[5, 10,15]] 
    """
    a = np.arange(5)
    b = np.array([1,6,11])
    a = a[:, np.newaxis]
    c = a + b
    print(c)
    print()
    d1 = c[1, :]
    d2 = c[3, :]
    d = np.vstack([d1, d2])
    print(d)
    print()



def example24():
    """images """
    path = "../assets/drozy.png"
    img = plt.imread(path)
    print("img.shape = ", img.shape)
    print("imd.dtype = ", img.dtype)
    print()
    img_red = img[:,:,0]
    plt.imshow(img_red, cmap=plt.cm.gray)
    # plt.show()
    plt.savefig("../assets/plot.png")
    plt.imsave("../assets.red_drozy.png", img_red, cmap= plt.cm.gray)




def example23():
    """load file """
    data = np.loadtxt("populations.txt")
    print(data)
    year, hare , lynx, carrot = data.T
    print("year = ", year)
    print("hare = ", hare)
    print("lynx = ", lynx)
    print("carrot = ", carrot)
    print()
    # save data
    np.savetxt("pop2.txt", data)


def example22():
    """polynomial 5 , Chebyshev"""
    x = np.linspace(-1, 1, 2000)
    y = np.cos(x)+ 0.3*np.random.rand(2000)
    p = np.polynomial.Chebyshev.fit(x, y, 90) # 90 degree
    t = np.linspace(-1, 1, 200)
    plt.plot(x,y, 'r.')
    plt.plot(t, p(t), 'k-', lw=3)
    plt.show()


def example21():
    """polynomial 4"""
    p = np.polynomial.Polynomial([-1, 2, 3])  # in reverse order
    print("p(0) = ", p(0))
    print("p.roots() = ", p.roots())
    print("p.degree() = ", p.degree())
    print()



def example20():
    """polynomial 3"""
    x = np.linspace(0, 1, 20)
    y = np.cos(x) + 0.2*np.random.rand(20)
    p = np.poly1d(np.polyfit(x, y, 3))
    t = np.linspace(0, 1, 200)
    plt.plot(x, y, 'o', t, p(t), '-')
    plt.show()



def example19():
    """polynomial 2"""
    p = np.poly1d([3,2,-1]) # 3x^2 + 2x - 1
    print("p(0) = ", p(0))
    print("p.roots = ", p.roots)
    print("p.order = ", p.order)
    print()

def example18():
    """polynomial"""
    x = np.linspace(0,1, 20)
    y = np.cos(x) + 0.3*np.random.rand(20)
    p = np.poly1d(np.polyfit(x, y,3))
    print(p)
    t = np.linspace(0, 1, 200)
    plt.plot(x, y, 'o', t, p(t), '-')
    plt.show()

def example17():
    """ array sorting"""
    a = np.array([[4, 3,5], [1,2,1]])
    # sort column wise
    b = np.sort(a , axis = 1)
    # sort row wise
    c = np.sort(a, axis = 0)
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)
    # inplace sort
    a.sort(axis = 1)
    print("a (after sort) = ", a)
    #arg sort
    a = np.array([4,3,1,2])
    j = np.argsort(a)
    print("j = ", j)
    print("a[j] = ", a[j])
    j_max , j_min = np.argmax(a), np.argmin(a)
    print("j_max , j_min = ", j_max , " , ", j_min)

    print()


def example16():
    """array reshape, ravel , transpose , T , resize"""
    # flattening
    # c = a.flatten() # unlike ravel(), flatten() returns copy , not view
    a = np.array([[1,2,3], [4,5,6]])
    print("a = ", a)
    ret = a.ravel()
    print("a.ravel() = ", ret)
    ret = a.T
    print("a.T = ", ret)
    ret = ret.ravel()
    print("a.T.ravel() = ", ret)
    print()
    #reshaping
    print("a.shape = ", a.shape)
    ret = a.ravel().reshape((2,3))
    print("a.ravel().reshape((2,3)) = ", ret)
    ret = a.reshape((2,-1))
    print("a.reshape((2,-1)) = ", ret)
    ret[0,0] = 99 # a will be modified as well
    print(a)
    a = np.zeros((3,2))
    ret = a.T.reshape(3*2)
    ret[0] = 99 # a will not be modified
    print(a)
    print()
    #adding dimension
    z = np.array([1,2,3])
    print("z = ", z)
    print("z.shape = ", z.shape) # (3,)
    ret = z[:, np.newaxis]
    print("z[:, np.newaxis] = ", ret)
    print("and shape = ", ret.shape) # (3, 1)
    ret = z[np.newaxis , :]
    print("z[np.newaxis, :] = ", ret)
    print("and shape = ", ret.shape) # (1,3)
    print()
    # dimension shuffling
    a = np.arange(4*3*2).reshape(4, 3, 2)
    print("a.shape = ", a.shape) # (4, 3, 2)
    print("a[0,2,1] = ", a[0,2,1]) # 5
    ret = a.transpose(1, 2,0)
    print("a.transpose(1,2,0).shape  = ", ret.shape) # (3,2,4)
    print("ret[2,1,0] = ", ret[2,1,0]) # 5
    ret[2,1,0] = -1 # changes a
    print("a[0,2,1] = ", a[0,2,1]) # -1
    print()
    # resizing
    a = np.arange(4)
    a.resize((8, ))
    print(a)

    print()




def example15():
    """using np.mgrid() instead of np.ogrid()"""
    x , y = np.mgrid[0:5, 0:5]
    print(x.shape, y.shape)
    print(x, y)
    distance = np.sqrt(x**2 + y*+2)
    print(distance)
    plt.pcolor(distance)
    plt.colorbar()
    plt.show()

def example14():
    """example13() improved , better way"""
    x , y = np.ogrid[0:5, 0:5]
    print(x.shape , y.shape)
    distance = np.sqrt(x**2 + y **2)
    print(distance)
    plt.pcolor(distance)
    plt.colorbar()
    plt.show()

def example13():
    """broadcasting generating grid"""
    x , y = np.arange(5), np.arange(5)[:, np.newaxis]
    distance = np.sqrt(x**2 + y**2)
    print(distance)
    plt.pcolor(distance)
    plt.colorbar()
    plt.show()


def example12():
    """broadcasting"""
    # distance between different usa cities
    mileposts = np.array([0, 198, 303, 736, 871, 1175,1475,
                          1544, 1913, 2448])

    m2  = mileposts[:, np.newaxis]
    distance_array = np.abs(mileposts - m2)
    print(distance_array)
    print()


def example11():
    """reductions"""
    x = np.array([1,2,3,4])
    ret = np.sum(x)
    ret = x.sum()
    print("x = ", x)
    print("x.sum() = ", ret)
    x = np.array([[1,1], [2,2]])
    print("x = ", x)
    ret = x.sum(axis = 0) #columnwise
    print("columnwise x.sum() = ", ret)
    ret = x.sum(axis = 1) #rowwise
    print("rowwise x.sum() = ", ret)
    ret = (x[:, 0].sum(), x[:, 1].sum())
    print("columnwise x.sum() = ", ret)
    ret = (x[0, :].sum(), x[1, :].sum())
    print("rowwise x.sum() = ", ret)
    x = np.array([1,3,2])
    print("x = ", x)
    print("x.min() = ", x.min())
    print("x.max() = ", x.max())
    print("x.argmin() = ", x.argmin())
    print("x.argmax() = ", x.argmax())
    ret = np.all(x > 1)
    print("all x > 1 = ", ret)
    ret = np.any(x>1)
    print("any x > 1 = ", ret)
    a = np.zeros((100, 100))
    ret = np.any(a != 0)
    print("any a != 0  = ", ret)
    ret = np.all( a == 0)
    print("all a == 0 = ", ret)
    a = np.array([1,2,3,2])
    b = np.array([2,2,3,2])
    c = np.array([6,4,4,5])
    ret = ((a<=b) & (b <= c)).all()
    print("all a<=b & b <= c = ", ret)
    #statistics
    x = np.array([1,2,3,1])
    y = np.array([[1,2,3], [5,6,1]])
    ret = np.mean(x)
    print("x.mean() = ", ret)
    ret = np.median(x)
    print("median x  = ", ret)
    ret = np.std(x)
    print("std x = ", ret)
    x.mean()
    x.std()
    ret = np.median(y, axis = -1) # last axis
    print("median y for axis = -1 = ", ret)
    x = np.array([[1,2,3], [4,5,6]])
    ret = np.cumsum(x)
    print("cumsum x = ", ret)
    print("sum x = ", np.sum(x))
    print()


def example10():
    """ elementwise operations on arrays"""
    a = np.arange(1, 5)
    b = np.ones(4)+ 1
    print("a+1 = " , (a+1))
    print("b = ", b)
    print("a + b = ", (a+b))
    print("a - b = ", (a-b))
    print("a * b = ", (a*b))
    print("a / b = ", (a/b))
    print("a * 2 = ", (a*2))
    print("a ** 2 = ", (a**2))
    print("2 ** a = ", 2**a)
    print()
    # matrix multiplication
    c = np.ones((3,3))
    print("c.dot(c) = ", c.dot(c))
    print("c*c = ", c*c) # that is elementwise multiplication
    evens = np.arange(0, 10, 2)
    odds = np.arange(1, 10, 2)
    print(evens, odds)
    sum_numbers = evens + odds
    print(sum_numbers)
    a = np.arange(5)
    a = 2**a
    print(a)
    b = 2**(3*a)- a
    print(b)
    print()
    #comparison
    a = np.arange(1, 5)
    b = np.array([4,2,2,4])
    print("a = ", a)
    print("b = ", b)
    print("a == b = ", (a==b))
    print("a > b = ", (a>b))
    print("a < b = ", (a<b))
    print("a>=b = ", (a>=b))
    print("a<= b = ", (a<=b))
    #arraywise comparisons
    c = np.arange(1, 5)
    ret = np.array_equal(a, b)
    print("a equal b = ", ret)
    ret = np.array_equal(a, c)
    print("a equal c = ", ret)
    # logical operations
    a = np.array([1,1,0,0], dtype= bool)
    b = np.array([True, False, True, False])
    ret = np.logical_or(a, b)
    print("a or b = ", ret)
    ret = np.logical_and (a, b)
    print("a and b = ", ret)
    ret = np.logical_xor(a, b)
    print("a xor b = ", ret)
    ret = np.logical_not(a)
    print("not a = ", ret)
    ret = np.logical_not(b)
    print("not b = ", ret)
    #transcendental functions
    a = np.arange(5)
    ret = np.sin(a)
    print("sin(a) = ", ret)
    ret = np.log(a)
    print("log(a) = ", ret)
    ret = np.exp(a)
    print("exp(a) = ", ret)
    print()


def example9():
    """ fancy indexing"""
    a = np.arange(10)
    b = np.array(a%3 == 0)
    print(a)
    print(b)
    masks = (a%3  == 0)
    a[masks] = -1
    print(a)
    a[[0, 3, 6, 9]] = -100
    print(a)
    print()
    a = np.arange(0, 6) + np.arange(0, 51, 10)[:, np.newaxis]
    print(a)
    masks = (a < 6)
    masks2 = (a>= 50)
    print(np.array(masks))
    print()
    print(np.array(masks2))
    print()
    a[masks] = 0
    a[masks2] = 0
    print(a)
    print()

def example8():
    """indexing and slicing of numpy"""
    evens = np.arange(0, 9, 2)
    odds = np.arange(1, 10, 2)
    print(evens, odds)
    evens_reversed = evens[::-1]
    odds_reversed = odds[::-1]
    print(evens_reversed, odds_reversed)
    numbers = np.concatenate((evens_reversed, odds_reversed))
    print(numbers)
    print(np.arange(0, 6)+ np.arange(0, 51, 10)[:, np.newaxis])
    a = np.ones((4,4), dtype=np.int64)
    a[2,3] = 2
    a[3,1] = 6
    print()
    print(a)
    print()
    row1 = np.zeros(5)
    rest_rows = np.diag(np.arange(5)+2.0)
    print(row1, rest_rows)
    print()
    a = np.vstack((row1, rest_rows))
    print(a)
    print()
    # np.tile()
    a = np.array([[4,3],[2,1]])
    a = np.tile(a, (1,3))
    a = np.tile(a, (2,1))
    print(a)

    """
    [[4 3 4 3 4 3]
 [2 1 2 1 2 1]
 [4 3 4 3 4 3]
 [2 1 2 1 2 1]]
    """
    print()

def example7():
    """imshow gray image"""
    image = np.random.random((100, 100))
    plt.imshow(image, cmap = plt.cm.gray)
    plt.colorbar()
    plt.show()

def example6():
    """virtualisation with 2D matrix"""
    row1 = np.linspace(1, 10, 20)
    row2 = np.linspace(0, 5, 20)
    matrix = np.array([row1, row2])
    print(matrix[0])
    plt.plot(matrix[0], matrix[1], 'o')
    plt.show()


def example5():
    """virtualisation , sin and cos"""
    x = np.linspace(-2*np.pi, 2*np.pi, 100, endpoint=True)
    y_sin, y_cos = np.sin(x), np.cos(x)
    plt.plot(x, y_sin)
    plt.plot(x, y_cos)
    plt.legend(["Sin Curve", "Cos Curve"])
    plt.show()



def example4():
    """imshow"""
    image = np.random.rand(30, 30)
    plt.imshow(image , cmap = plt.cm.hot)
    plt.colorbar()
    plt.show()

def example3():
    """virtualisation of np.array s with matplot"""
    x = np.linspace(0, 10, 20)
    y = np.linspace(0, 5, 20)
    plt.plot(x,y)
    plt.plot(x, y, 'o')
    plt.show()


def example2():
    """np different data types 
    default: int64 or float64"""
    a = np.array([1,2,3])
    print("a.dtype = ", a.dtype)  # int64
    a = np.array([1.0,2.0, 3.0])
    print("a.dtype = ", a.dtype)  # float64
    a = np.array([True, False, False])
    print("a.dtype = ", a.dtype)  # bool
    a = np.array(["foo", "bar", "pako"])
    print("a.dtype = ", a.dtype)  # <U4

    print()

def example1():
    """experimenting with np: arange , array , linspace , ones, zeros, eye, diag
    random 
    """
    # array
    a = np.array([[1, 2,3], [4,5,6]])
    print("a.shape = ", a.shape)
    print("a.ndim = ", a.ndim)
    print("len(a) = ", len(a))  # a.ndim == len(a)
    print("type(a) = ", type(a))
    print("np.shape(a) = ", np.shape(a))
    print("np.ndim(a) = ", np.ndim(a))
    print()
    # arange
    a = np.arange(10)
    print(a)
    a = np.arange(1, 10)
    print(a)
    a = np.arange(1, 10, 2)
    print(a)
    a = np.arange(1, 10, 2, dtype = np.int64)
    print(a)
    a = np.arange(1, 10, 2, dtype=np.float64)
    print(a)
    print()
    #linspace
    a = np.linspace(0 , 1, 5, dtype = np.float32)
    print(a)
    a = np.linspace(1, 10, 100)
    print(a)
    print()
    # ones , zeros , eye, diag
    a = np.ones((3, 3))
    print(a)
    a  = np.zeros((3,3))
    print(a)
    a = np.eye(3)
    print(a)
    a = np.diag(np.arange(4)+1)
    print(a)
    print()

    # random
    print("rand(4) = ", np.random.rand(4))
    a = np.random.randint(1, 10 , 5)
    print(a)
    a = np.random.randn(4) # gaussian
    print(a)
    np.random.seed(np.int64(time.time()))
    a = np.random.rand(10)
    print(a)
    print()
    a = np.array([[1,2,3], [4,5,6]])
    b = np.empty([3,4], dtype = np.int64)
    print(b)
    print()
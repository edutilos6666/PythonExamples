import numpy as np
import copy
import matplotlib.pyplot as plt
from scipy.misc import imread , imresize, imsave
from scipy.io import loadmat, savemat


def example6():
    'loadmat'
    ex1 = loadmat("matlabfiles/example1.mat")
    print(ex1.values())
    print(ex1.items())
    arr1 = ex1.get("arr")
    arr1_arr = np.array(arr1)
    print(arr1_arr, arr1_arr.shape)

    arr2 = np.array([[1, 2, 3], [4,5,6], [7,8,9]])
    savemat('matlabfiles/example2.mat', {'arr2': arr2})

def example5():
    img = imread('assets/drozy.png')
    img_tinted = img* [1, 0.95, 0.9]
    img_tinted = np.uint8(img_tinted)

    plt.subplot(2, 2, 1)
    plt.imshow(img)

    plt.subplot(2,2, 2)
    plt.imshow(img_tinted)


    img3 = imresize(img, (300, 300))
    img4 = imresize(img, (150 , 150))
    plt.subplot(2, 2, 3)
    plt.imshow(img3)

    plt.subplot(2, 2, 4)
    plt.imshow(img4)


    imsave('assets/drozy_modified.png', img_tinted)

    plt.show()

def example4():
    x = np.arange(0, 4*np.pi, 0.1)
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    y_tan = np.tan(x)

    a = np.arange(0, 10 , 0.5)
    y_square = np.power(a, 2)


    plt.subplot(2, 2, 1)
    plt.plot(y_sin)
    plt.title('Sin curve')


    plt.subplot(2, 2, 2)
    plt.plot(y_cos)
    plt.title('Cos curve')

    plt.subplot(2,2,3)
    plt.plot(y_tan)
    plt.title('Tan curve')


    plt.subplot(2, 2, 4)
    plt.plot(y_square)
    plt.title('Square curve')

    plt.show()


def example3():
    x = np.arange(0, 4*np.pi , 0.1)
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    y_tan = np.tan(x)
    plt.plot(y_sin)
    plt.plot(y_cos)
    # plt.plot(y_tan)
    plt.xlabel('x axis label')
    plt.ylabel('y axis label')
    plt.title('Sin , Cos and Tan curves')
    plt.legend(['sin', 'cos'])
    plt.show()

def example2():
    'matplot'
    x = np.arange(0, 3*np.pi , 0.1)
    y = np.sin(x)
    plt.plot(x,y)
    plt.show()

def example1():
    'only numpy'
    a = np.array([1, 2,3])
    print("type(a) = ", type(a))
    print("a.shape = ", a.shape)
    print(a[0], a[1], a[2])
    print("<<a>>: ", end = "")
    for n in a :
        print(n , end = " ; ")
    print()
    print(a)
    a[0] = 100
    print(a)
    # 2-dimensional array
    b = np.array([[1,2,3], [4,5,6]])
    print("type(b) = ", type(b))
    print("b.shape = ", b.shape)
    print(b[0,0]," , ", b[0,1], ", ", b[0,2])
    for arr in b:
        for n in arr:
            print(n, end = " ; ")
        print()
    print()
    print(b)
    b[0,0], b[1,2] = 100, 666
    print(b)
    a = np.zeros((3,3))
    print(a)
    a = np.ones((2, 3))
    print(a)
    a = np.full((2,3), 111)
    print(a)
    a = np.eye(3)
    print(a)
    a = np.random.random((3,4))
    print(a)
    a = np.array([[1, 2,3,4], [5,6,7,8], [9,10,11,12]])
    print()
    print(a)
    b = a[:2, 1:3]
    print(b)
    print(a[0,1])
    b[0,0] = 777
    print(a[0,1])
    b = copy.copy(a[:2, 1:3])
    b[0,0] = 666
    print(a[0,1])
    a = np.array([[1, 2,3,4], [5,6,7,8], [9,10,11,12]])
    row0 = a[0, :]
    row1 = a[1, :]
    row1_arr = a[1:2, :]
    print(row0, row0.shape)
    print(row1, row1.shape)
    print(row1_arr, row1_arr.shape)
    # integer array indexing
    a = np.array([[1,2], [3,4], [5,6]])
    print(a[[0, 1,2], [0, 1, 0]])
    print(np.array([a[0,0], a[1, 1], a[2,0]]))
    print(a[[0,0], [1,1]])
    print(np.array([a[0,1], a[0,1]]))
    a = np.array([[1, 2,3], [4,5, 6], [7,8,9], [10,11,12]])
    indices_0 = np.arange(4)
    indices_1 = np.array([0, 2, 0, 1])
    print(a[indices_0, indices_1])
    a[indices_0, indices_1] += 10
    print(a)
    a = np.array([[1,2], [3,4], [5,6]])
    indices_gt_2 = (a > 2)
    print(indices_gt_2)
    print(a[indices_gt_2])
    print(a[a>2])
    # data types
    a = np.array([[1,2], [3,4]])
    print("a.dtype = ", a.dtype)
    a = np.array([[1.0, 2.0], [3.3, 4.4]])
    print("a.dtype = ", a.dtype)
    a = np.array([[1,2], [3,4]], dtype = np.int64)
    print("a.dtype = ",a.dtype)
    # array math
    x = np.array([[1,2], [3,4]], dtype = np.float64)
    y = np.array([[5,6], [7,8]], dtype = np.float64)
    print("x+y = ", (x+y))
    print(np.add(x,y))
    print()
    print("x -y = ", (x-y))
    print(np.subtract(x,y))
    print()
    print("x*y = ", (x*y))
    print(np.multiply(x,y))
    print()
    print("x/y = ", (x/y))
    print(np.divide(x,y))
    print()
    print(np.sqrt(x))
    print()
    print(x.dot(y))
    print(np.dot(x,y))
    print()
    v = np.array([10, 11])
    print(x.dot(v))
    print(np.dot(x,v))
    print()
    a= np.array([[1,2],[3,4]])
    print(np.sum(a))
    print(np.sum(a, axis = 0))
    print(np.sum(a, axis= 1))
    print()
    print(a)
    print(a.T) # transpose a
    # for one dimensional array , T does nothing
    a = np.array([1,2,3])
    print(a.T)
    print()
    # broadcasting
    x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
    v = np.array([10, 20, 30])
    y = np.empty_like(x)
    print(y)
    for i in np.arange(4):
        y[i, :] = x[i, :] + v

    print(y)
    print()
    vv = np.tile(v , (4,1))
    print(vv)
    y = x + vv
    print(y)
    print()
    # now broadcasting
    y = x + v
    print(y)




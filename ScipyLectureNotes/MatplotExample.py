import numpy as np
import matplotlib.pyplot as plt
import copy
from mpl_toolkits.mplot3d import Axes3D



def example20():
    """3D plot example2"""
    fig = plt.figure()
    ax = Axes3D(fig)
    X = np.arange(-10, 10, 0.25)
    Y = np.arange(-10, 10, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2+ Y**2)
    Z = np.sin(R)
    ax.plot_surface(X, Y, Z , rstride= 1 , cstride = 1, cmap = plt.cm.hot)
    ax.contourf(X, Y, Z, zdir="z", offset = -1, cmap = plt.cm.hot)
    ax.set_zlim(-2,2)
    plt.show()

def example19():
    """3D plot"""
    fig = plt.figure()
    ax = Axes3D(fig)
    X = np.arange(-4, 4, 0.25)
    Y = np.arange(-4, 4, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.sin(R)

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.hot)
    ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.cm.hot)
    ax.set_zlim(-2, 2)

    plt.show()


def example18():
    """polar bar"""
    ax = plt.axes([0.025, 0.025, 0.95, 0.95], polar=True)

    N = 20
    theta = np.arange(0.0, 2 * np.pi, 2 * np.pi / N)
    radii = 10 * np.random.rand(N)
    width = np.pi / 4 * np.random.rand(N)
    bars = plt.bar(theta, radii, width=width, bottom=0.0)

    for r, bar in zip(radii, bars):
        bar.set_facecolor(plt.cm.jet(r / 10.))
        bar.set_alpha(0.5)

    ax.set_xticklabels([])
    ax.set_yticklabels([])
    plt.show()


def example17():
    """polar bar"""
    plt.axes([0, 0, 1, 1], polar=True)
    N = 20
    theta = np.arange(0., 2 * np.pi, 2 * np.pi / N)
    radii = 10 * np.random.rand(N)
    width = np.pi / 4 * np.random.rand(N)
    bars = plt.bar(theta, radii, width=width, bottom=0.0)

    for r, bar in zip(radii, bars):
        bar.set_facecolor(plt.cm.jet(r / 10.))
        bar.set_alpha(0.5)

    plt.show()


def example16():
    """quiver 2 """
    n = 8
    X, Y = np.mgrid[0:n, 0:n]
    T = np.arctan2(Y - n / 2., X - n / 2.)
    R = 10 + np.sqrt((Y - n / 2.0) ** 2 + (X - n / 2.0) ** 2)
    U, V = R * np.cos(T), R * np.sin(T)

    plt.axes([0.025, 0.025, 0.95, 0.95])
    plt.quiver(X, Y, U, V, R, alpha=.5)
    plt.quiver(X, Y, U, V, edgecolor='k', facecolor='None', linewidth=.5)

    plt.xlim(-1, n)
    plt.xticks(())
    plt.ylim(-1, n)
    plt.yticks(())

    plt.show()


def example15():
    """ quiver """
    n = 8
    X , Y = np.mgrid[0:n, 0:n]
    plt.quiver(X, Y, edgecolor = "red", facecolor = "k")
    plt.show()

def example14():
    """pie chart"""
    n = 10
    Z = np.random.uniform(0, 1, n)
    labels = []
    for i in range(n):
        labels.append("Label "+ str(i+1))

    plt.pie(Z, explode = Z*0.05, labels = labels)
    plt.show()

def example13():
    """imshow """

    def f(x, y):
        return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)

    n = 10
    x = np.linspace(-3, 3, 4*n)
    y = np.linspace(-3, 3, 4*n)
    X , Y = np.meshgrid(x, y)
    plt.imshow(f(X,Y))
    plt.show()

def example12():
    """contour example"""

    def f(x, y):
        return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)


    n = 256
    x = np.linspace(-3, 3, n)
    y = np.linspace(-3, 3, n)
    X, Y = np.meshgrid(x,y)

    plt.axes([0.025, 0.025, 0.95, 0.95])
    plt.contourf(X, Y, f(X, Y), 10, alpha= 0.75, cmap = plt.cm.hot)
    C = plt.contour(X, Y, f(X, Y), 10, colors= "black", linewidth =.5)
    plt.clabel(C, inline = 1, fontsize= 10)

    plt.xticks(())
    plt.yticks(())
    plt.show()


def example11():
    """bar chart example 2"""
    n = 10
    X = np.arange(n)
    Y1 = np.random.random(n)+0.5
    Y2 = np.random.random(n)+ 0.5
    Y2 = -copy.copy(Y2)

    plt.bar(X, Y1, facecolor = "blue", edgecolor = "green")
    plt.bar(X, Y2, facecolor = "green", edgecolor = "blue")

    for (x,y) in zip(X, Y1):
        plt.text(x+0.001, y+0.01, "%.2f"% y, ha="center", va="bottom", color="red" )

    for (x, y) in zip(X, Y2):
        plt.text(x+0.001, y-0.15, "%.2f"% y , ha = "center", va = "bottom", color = "red")



    plt.show()



def example10():
    """bar chart example"""
    n = 10
    x = np.arange(n)
    y = np.random.random(n)+ 0.5
    plt.bar(x, y, facecolor = "blue", edgecolor= "green")

    for (n1, n2) in zip(x, y):
        plt.text(n1+0.01, n2+0.01 , "%.2f" % n2, ha="center", va="bottom", color = "red")

    plt.show()



def example9():
    """scatter example 2"""
    n = 2**10
    x = np.random.normal(0, 1, n)
    y = np.random.normal(0, 1, n)
    plt.scatter(x, y, color = "blue")

    color_names = ["red", "green", "cyan", "yellow", "orange"]

    for i in range(5):
        x1 = np.random.choice(x, int(n / 4))
        y1 = np.random.choice(y, int(n / 4))
        plt.scatter(x1, y1, color= color_names[i])



    plt.show()




def example8():
    """scatter example"""
    x = np.random.normal(0, 1, 1024)
    y = np.random.normal(0, 1, 1024)
    plt.scatter(x, y)
    plt.show()


def example7():
    """subplot example"""
    x = np.linspace(-np.pi , np.pi , 100)
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    y_tan = np.tan(x)
    y4 = copy.copy(x)

    plt.subplot(2,2, 1)
    plt.plot(x, y_sin)
    plt.title("Sin Curve")

    plt.subplot(2, 2, 2)
    plt.plot(x, y_cos)
    plt.title("Cos Curve")

    plt.subplot(2,2, 3)
    plt.plot(x, y_tan)
    plt.title("Tan Curve")

    plt.subplot(2,2, 4)
    plt.plot(x, y4)
    plt.title("y = x")

    plt.show()



def example6():
    """adding a legend 
    method 2"""
    x = np.linspace(-np.pi , np.pi , 100)
    y_sin = np.sin(x)
    y_cos = np.cos(x)

    plt.plot(x, y_sin ,  color= "blue", linewidth = 2.0, linestyle = "-", label ="Sin Curve")
    plt.plot(x, y_cos, color="red", linewidth = 2.0, linestyle="-", label="Cos Curve")

    plt.legend(loc = "upper left")
    plt.show()


def example5():
    """adding a legend 
    method 1 
    """
    x = np.linspace(-np.pi , np.pi , 100)
    y_sin = np.sin(x)
    y_cos = np.cos(x)


    plt.plot(x, y_sin , x , y_cos)
    plt.legend(("Sin Curve", "Cos Curve"), loc = "upper left")
    plt.show()


def example4():
    """moving spines """
    x = np.linspace(-np.pi , np.pi , 100)
    y_sin = np.sin(x)
    y_cos = np.cos(x)


    ax = plt.gca()
    ax.spines["top"].set_color("none")
    ax.spines["right"].set_color("none")
    ax.spines["left"].set_position(("data", 0))
    ax.spines["bottom"].set_position(("data", 0))
    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")

    plt.plot(x, y_sin , x, y_cos)
    plt.show()


def example3():
    """setting tick labels"""
    x = np.linspace(-np.pi , np.pi , 100)
    y_sin = np.sin(x)
    y_cos = np.cos(x)

    plt.xlim(-4, 4, 9)
    plt.ylim(-1,1, 5)
    #setting ticks
    plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
               [r"$-\pi$", r"$-\pi/2$", r"$0$", r"$\pi/2$", r"$\pi$"])
    plt.yticks([-1, 0, 1], [r"$-1$", r"$0$", r"$1$"])

    plt.plot(x, y_sin, x, y_cos)
    plt.show()



def example2():
    """manipulating default values"""
    #setting canvas widthxheight and dpi
    plt.figure(figsize = (8, 6), dpi=80)
    plt.subplot(1, 1,1)

    x = np.linspace(-np.pi , np.pi, 100)
    y_sin = np.sin(x)
    y_cos = np.cos(x)

    #changing xlim, ylim , xticks , yticks
    # plt.xlim(-4.0, 4.0)
    # plt.ylim(-1.0, 1.0)
    plt.xlim(x.min(), x.max())
    plt.ylim(min(y_sin.min(), y_cos.min()), max(y_sin.max(), y_cos.max()))

    plt.xticks(np.linspace(-4, 4, 9, endpoint=True))
    plt.yticks(np.linspace(-1, 1, 5, endpoint=True))

    #plotting
    plt.plot(x, y_sin, color= "blue", linewidth = 2.0, linestyle = "-")
    plt.plot(x, y_cos, color = "red", linewidth = 2.0, linestyle = "-")

    plt.show()


def example1():
    """simple example"""
    x =  np.linspace(-2*np.pi, 2*np.pi , 200)
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    plt.plot(x, y_sin , x, y_cos)
    plt.show()
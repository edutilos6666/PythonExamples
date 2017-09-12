import numpy as np
from matplotlib import pyplot as plt



def example3():
    'scatter plot'
    n = 1024
    x = np.random.normal(0, 1, n)
    y = np.random.normal(0, 1, n )

    plt.scatter(x, y, color= "green")

    colors = ["red", "blue", "yellow", "magenta", "purple",
              "cyan", "orange", "olivedrab", "goldenrod", "lightyellow"]
    colors  = np.random.permutation(colors)
    for i in np.arange(10):
        x2 = np.random.choice(x, n / 4)
        y2 = np.random.choice(y, n / 4)
        plt.scatter(x2, y2, color=colors[i])

    plt.show()

def example2():
    'normal curves'
    x = np.linspace(-np.pi , np.pi , 256, endpoint=True)
    y = np.sin(2*x)

    x2 = np.linspace(-np.pi , -np.pi/2, 64, endpoint=True)
    y2 = np.sin(2*x2)

    x3 = np.linspace(-np.pi/2, 0, 64, endpoint=True)
    y3 = np.sin(2 * x3)

    x4 = np.linspace(0 , np.pi / 2, 64, endpoint=True)
    y4 = np.sin(2 * x4)

    x5 = np.linspace(np.pi/2, np.pi, 64, endpoint=True)
    y5 = np.sin(2 * x5)

    plt.plot(x, y +1 , color= "blue", alpha = 1.00)
    plt.plot(x, y- 1 , color = "blue", alpha= 1.00)
    plt.fill_between(x, y+1  , 1, color = "blue")
    plt.fill_between(x2, y2-1, -1, color = "blue" )
    plt.fill_between(x4, y4 - 1, -1, color="blue")
    plt.fill_between(x3, y3-1, -1, color= "orange")
    plt.fill_between(x5, y5 - 1, -1, color="orange")

    plt.show()


def example1():
    plt.figure(figsize= (8,6), dpi= 80)
    plt.subplot(1, 1, 1)

    x = np.linspace(-np.pi , np.pi , 256 , endpoint=True)
    y_sin, y_cos = np.sin(x), np.cos(x)

    plt.plot(x, y_sin, color= "red", linewidth = 1.0, linestyle= "-")
    plt.plot(x, y_cos, color="green", linewidth = 1.0, linestyle = "-")

    plt.xlim(-4.0, 4.0)
    plt.ylim(-1.0, 1.0)

    plt.xticks(np.linspace(-4, 4, 9 , endpoint=True))
    plt.yticks(np.linspace(-1, 1, 5, endpoint = True))

    # plt.xticks([-np.pi , -np.pi/2, 0, np.pi/2, np.pi])
    # plt.yticks([-1, 0, 1])


    gca = plt.gca()  # get current axis
    gca.spines["bottom"].set_position(("data", 0))
    gca.spines["left"].set_position(("data", 0))
    gca.spines["top"].set_color("none")
    gca.spines["right"].set_color("none")
    gca.xaxis.set_ticks_position("bottom")
    gca.yaxis.set_ticks_position("left")

    plt.legend(["Sin Curve", "Cos Curve"], loc= "upper right")

    t = 2 *np.pi / 3
    plt.annotate(r'$cos(\frac{2\pi}{3})=-\frac{1}{2}$',
                 xy=(t, np.cos(t)), xycoords='data',
                 xytext=(-90, -50), textcoords='offset points', fontsize=16,
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))



    plt.annotate(r'$sin(\frac{2\pi}{3}) = \frac{\sqrt{3}}{2}$',
                xy = (t , np.sin(t)), xycoords = 'data',
                xytext = (30 , 60), textcoords = 'offset points', fontsize = 16 ,
                arrowprops = dict(arrowstyle = "->", connectionstyle="arc3,rad=.2"))


    plt.plot([t, t], [0, np.sin(t)], color  = "red", linewidth = 2.5 , linestyle = "--")
    plt.scatter([t, ], [np.sin(t), ], 50, color= "red")

    for label in gca.get_xticklabels() + gca.get_yticklabels():
        label.set_fontsize(16)
        label.set_bbox(dict(facecolor = "white", edgecolor = "None", alpha = 0.65))


    plt.show()


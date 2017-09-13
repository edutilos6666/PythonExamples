import numpy as np
from scipy import io as spio, misc
import matplotlib.pyplot as plt
from scipy import linalg
from scipy import fftpack
from scipy import optimize
from scipy import stats
from scipy import ndimage
from scipy import signal

def example8():
    """ image filtering """
    face = misc.face(gray = True)
    face = face[:512, -512:]
    noisy_face =np.copy(face).astype(np.float)
    noisy_face += face.std()*0.5*np.random.standard_normal(face.shape)
    blurred_face = ndimage.gaussian_filter(noisy_face, sigma=3)
    median_face = ndimage.median_filter(noisy_face , size=5)
    wiener_face = signal.wiener(noisy_face, (5,5))

    plt.subplot(1, 4, 1)
    plt.imshow(noisy_face, cmap = plt.cm.gray)
    plt.title("Noisy face")

    plt.subplot(1, 4, 2)
    plt.imshow(blurred_face , cmap = plt.cm.gray)
    plt.title("Gaussian filter")

    plt.subplot(1, 4, 3)
    plt.imshow(median_face, cmap = plt.cm.gray)
    plt.title("Median filter")

    plt.subplot(1, 4, 4)
    plt.imshow(wiener_face, cmap= plt.cm.gray)
    plt.title("Wiener filter")

    plt.show()



def example7():
    """ scipy image processing"""
    face = misc.face(gray=True)
    shifted_face = ndimage.shift(face, (50, 50))
    shifted_face2 = ndimage.shift(face, (50, 50), mode="nearest")
    rotated_face = ndimage.rotate(face, 30)
    cropped_face = face[50:-50, 50:-50]
    zoomed_face = ndimage.zoom(face, 2)

    plt.tick_params(
        # axis='x',  # changes apply to the x-axis
        which='both',  # both major and minor ticks are affected
        bottom='off',  # ticks along the bottom edge are off
        top='off',  # ticks along the top edge are off
        labelbottom='off')
    plt.subplot(3,3, 1)
    plt.imshow(face, cmap = plt.cm.gray)
    plt.subplot(3, 3, 2)
    plt.imshow(shifted_face, cmap = plt.cm.gray)
    plt.subplot(3, 3, 3)
    plt.imshow(shifted_face2, cmap = plt.cm.gray)
    plt.subplot(3, 3, 4)
    plt.imshow(rotated_face, cmap= plt.cm.gray)
    plt.subplot(3, 3, 5)
    plt.imshow(cropped_face, cmap= plt.cm.gray)
    plt.subplot(3, 3, 6)
    plt.imshow(zoomed_face, cmap= plt.cm.gray)
    plt.show()

def example6():
    """ stats histogram"""
    a = np.random.normal(size = 1000)
    bins = np.arange(-4, 5)
    print("bins = ", bins)
    histogram = np.histogram(a, bins = bins, normed=True)[0]
    bins = 0.5*(bins[1:]+ bins[:-1])
    print("bins = ", bins)
    b = stats.norm.pdf(bins)
    # plt.plot(bins, histogram)
    # plt.plot(bins, b)
    # plt.show()

    # loc? and std
    loc, std = stats.norm.fit(a)
    print("loc = ", loc)
    print("std = ", std)

    # median and percentile
    median = np.median(a)
    percentile50 = stats.scoreatpercentile(a, 50)
    percentile90 = stats.scoreatpercentile(1, 90)
    print("median = ", median)
    print("percentile 50 = ", percentile50)
    print("percentile 90 = ", percentile90)
    # T test
    a = np.random.normal(0, 1, size= 100)
    b = np.random.normal(1, 1, size = 10)
    ttest = stats.ttest_ind(a, b)
    print("ttest = ", ttest)




def example5():
    """ optimization problems"""
    def f(x):
        return x**2 + 10*np.sin(x)

    x = np.arange(-10, 10, 0.1)
    # plt.plot(x, f(x))
    # plt.show()

    # find local minima
    ret = optimize.fmin_bfgs(f, 0)
    print(ret)  # -1.30644012

    # another way to find local minima
    print()
    ret = optimize.basinhopping(f, 0)
    print(ret)

    # another way to find local minima between 2 bounds
    print()
    xmin_local = optimize.fminbound(f, 0, 10)
    print(xmin_local)

    # calculate root
    root = optimize.fsolve(f, 1)
    print("root = ", root)
    root2 = optimize.fsolve(f, -2.5)
    print("root2 = ", root2)

    # fit fnction
    xdata = np.linspace(-10, 10, num = 20)
    ydata = f(xdata) + np.random.randn(xdata.size)
    def f2(x, a, b):
        return a*x**2 +  b*np.sin(x)

    guess = [2,2]
    params , params_covariance = optimize.curve_fit(f2, xdata, ydata , guess)
    print("params = ", params)
    print("params_covariance = ", params_covariance)


def example4():
    """fast fourier transformation"""
    time_step = 0.02
    period = 5.
    time_vec = np.arange(0, 20 , time_step)
    sig = np.sin(2*np.pi/ period* time_vec) + 0.5*np.random.randn(time_vec.size)
    sample_freq = fftpack.fftfreq(sig.size, d = time_step)
    sig_fft = fftpack.fft(sig)
    pidxs = np.where(sample_freq > 0)
    freqs = sample_freq[pidxs]
    power = np.abs(sig_fft)[pidxs]
    freq = freqs[power.argmax()]
    print(np.allclose(freq, 1./period))
    sig_fft[np.abs(sample_freq) > freq] = 0
    main_sig = fftpack.ifft(sig_fft)
    plt.figure()
    plt.plot(time_vec, sig)
    plt.plot(time_vec, main_sig, linewidth = 3)
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.show()



def example3():
    """scipy linalg"""
    # calculating determinant of matrix
    arr = np.array([[1,2], [3,4]])
    print("det arr = ", linalg.det(arr)) # -2.0
    arr = np.array([[3, 2], [6, 4]])
    ret = linalg.det(arr)
    print("det arr = ", ret) # 0
    # only square matrices have determinant!
    # following error
    # linalg.det(np.ones((3, 4)))
    arr = np.ones((4, 4))
    ret = linalg.det(arr)
    print("det arr  = ", ret) # 0.0
    # calculating inversion of matrix
    arr = np.array([[1, 2], [3, 4]])
    iarr = linalg.inv(arr)
    print("iarr = ", iarr)
    ret = np.allclose(np.dot(arr, iarr), np.eye(2))
    print("ret = ", ret)
    # singular matrix(det == 0) does not have
    # inversion
    arr = np.array([[3, 2], [6,4]])
    # following error
    # linalg.inv(arr)

    # SVD -> singular-value decomposition
    arr = np.arange(9).reshape((3,3)) + np.diag([1,0,1])
    uarr, spec, vharr = linalg.svd(arr)
    print("spec = ", spec)
    sarr = np.diag(spec)
    svd_mat = uarr.dot(sarr).dot(vharr)
    print("np.allclose(svd_mat, arr) = ", np.allclose(svd_mat , arr))



def example2():
    """image file"""
    filename = "../assets/drozy.png"
    image = misc.imread(filename)
    # plt.imshow(image, cmap = plt.cm.gray)
    # plt.show()
    image2 = plt.imread(filename)
    plt.imshow(image2)
    plt.show()


def example1():
    """saving and loading matlab file"""
    a = np.ones((3,3))
    b = np.zeros((3, 3))
    c = np.diag(np.arange(1, 5))
    filename = "../matlabfiles/example3.mat"
    spio.savemat(filename, {"a": a , "b": b, "c": c})
    data = spio.loadmat(filename, struct_as_record=True)
    print(data["a"])
    print()
    print(data["b"])
    print()
    print(data["c"])
    print()
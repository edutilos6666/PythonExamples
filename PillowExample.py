from  PIL import Image
from PIL import ImageFilter, ImageEnhance


"""PIL is pillow library for image processing"""


def example7():
    """enhancement"""
    im = Image.open("assets/drozy.png")
    out = ImageEnhance.Contrast(im)
    out = out.enhance(1.3)
    out.show("30% more contrast")



def example6():
    """point transforms """
    im = Image.open("assets/drozy.png")
    filename = "assets/5.png"
    out = im.point(lambda i: i*1.2)
    out.save(filename)
    out.show()

def example5():
    """applying image filters"""
    im = Image.open("assets/drozy.png")
    filename = "assets/4.png"
    out = im.filter(ImageFilter.DETAIL)
    out = im.filter(ImageFilter.BLUR)
    out = im.filter(ImageFilter.GaussianBlur)
    out = im.filter(ImageFilter.CONTOUR)
    out.save(filename)


def example4():
    im = Image.open("assets/drozy.png")
    filename = "assets/3.png"
    out = im.transpose(Image.FLIP_LEFT_RIGHT)
    out = im.transpose(Image.FLIP_TOP_BOTTOM)
    out = im.transpose(Image.ROTATE_90)
    out = im.transpose(Image.ROTATE_180)
    out = im.transpose(Image.ROTATE_270)
    out.save(filename)


def example3():
    im = Image.open("assets/drozy.png")
    im2 = im.rotate(45)
    im2.save("assets/2.png", "PNG")

def example2():
    im = Image.open("assets/drozy.png")
    im2 = im.convert("L")
    im2.save("assets/1.png", "PNG")

def example1():
    im = Image.open("assets/drozy.png")
    print(str(im))
import re



def example3():
    're.sub()'
    str = "123-34355-1232332 # my phone number"
    pattern = r"\s#\s[a-zA-Z\s]+"
    sub1 = re.sub(pattern , "", str)
    pattern = r"\D+"
    sub2 = re.sub(pattern, "", str)
    print("sub1 = ", sub1)
    print("sub2 = ", sub2)
    print()


def example2():
    're.search()'
    str = "123-34355-1232332 # my phone number"
    pattern = R"(\d+)-(\d+)-(\d+)"
    searched = re.search(pattern , str)
    print("searched.group() = ", searched.group())
    print("searched.group(0) = ", searched.group(0))
    print("searched.group(1) = ", searched.group(1))
    print("searched.group(2) = ", searched.group(2))
    print("searched.group(3) = ", searched.group(3))
    print()

def example1():
    're.match()'
    str = "123-34355-1232332 # my phone number"
    pattern = r"(\d+)-(\d+)-(\d+)"
    matched = re.match(pattern ,str)
    print("matched.group() = ", matched.group())
    print("matched.group(0) = ", matched.group(0))
    print("matched.group(1) = ", matched.group(1))
    print("matched.group(2) = ", matched.group(2))
    print("matched.group(3) = ", matched.group(3))
    print()

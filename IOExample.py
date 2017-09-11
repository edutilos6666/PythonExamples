
def example2():
    'read and write , from and into file'
    file_name = "example2.dat"
    # writing into file
    names = ["foo", "bar", "bim", "pako"]
    with open(file_name, "w")  as f_out:
        for name in names:
            f_out.write(name +"\n")

    # reading from file
    with open(file_name, "r") as f_in:
        for line in f_in:
            print(line.strip())

    print()
    # writing into file 2
    file_name2 = "example2_2.dat"
    with open(file_name2, "w") as f_out:
        names = [name+"\n" for name in names]
        f_out.writelines(names)

    # reading from file 2
    with open(file_name2, "r") as f_in:
        lines = f_in.readlines()
        lines = [l.strip() for l in lines]
        for line in lines:
            print(line)

    print()


def example1():
    'user input'
    id , name, age, wage, active = None, None , None, None, None
    print("insert your id: ")
    id = int(input())
    print("insert your name: ")
    name = input()
    print("insert your age: ")
    age = int(input())
    print("insert your wage: ")
    wage = float(input())
    print("insert whether you are active: ")
    temp = input()
    active = True if(temp.lower() == "true") else False
    print("id = ", id)
    print("name = ", name)
    print("age = ", age)
    print("wage = ", wage)
    print("active = ", active)
    print()
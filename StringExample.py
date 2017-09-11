import copy


def example4():
    'string builtin methods'
    str = "foobar"
    print("str = ", str)
    print("str.capitalize() = ", str.capitalize())
    print("str.upper() = ", str.upper())
    print("str.capitalize().swapcase() = ", str.capitalize().swapcase())
    print("str.upper().lower() = ", str.upper().lower())
    print("str.title() = ", str.title())
    print()
    print("str.islower() = ", str.islower())
    print("str.isupper() = ", str.isupper())
    print("str.istitle() = ", str.istitle())
    print("str.isalpha() = ", str.isalpha())
    print("str.isspace() = ", str.isspace())
    print("str.isidentifier() = ", str.isidentifier())
    print("str.isprintable() = ", str.isprintable())
    print("str.isnumeric() = ", str.isnumeric())
    print("str.isdecimal() = ", str.isdecimal())
    print("str.isdigit() = ", str.isdigit())
    print("str.isalnum() = ", str.isalnum())
    print()
    foo_in_str = "foo" in str
    print("foo in str = ", foo_in_str)
    print("str.startswith(foo) = ", str.startswith("foo"))
    print("str.endswith(bar) = ", str.endswith("bar"))
    print("str.find(oba) = ", str.find("oba"))
    print("str.find(oba,3) = ", str.find("oba", 3))
    print()
    print("max(str) = ", max(str))
    print("min(str) = ", min(str))
    print("len(str) = ", len(str))
    replaced = str.replace("foo", "FOO")
    print("replaced = ", replaced)
    str = "foo bar bim"
    splitted = str.split()
    print("splitted = ", splitted)
    joined = " ; ".join(splitted)
    print("joined = ", joined)
    print()




def example3():
    'multiline string'
    str = """id = {0}
name = {1}
age = {2}
wage = {3}
active = {4}
    """
    id, name, age, wage, active = 1, "foo", 10, 100.0, True
    print(str.format(id, name, age , wage, active))
    print()



def example2():
    'formatting'
    id , name, age, wage, active = 1 , "foo", 10, 100.0, True
    print("id = %i , name = %s , age = %i, wage = %f , active = %r" % (id, name, age, wage, active))
    pattern = "id = {0}, name = {1}, age = {2}, wage = {3}, active = {4}"
    print(pattern.format(id , name, age, wage, active))
    print("age = %i , and %d , and %u, and %x, and %o"  % (age, age, age, age, age))
    print("wage = %f, and %e , and %g" %(wage, wage, wage) )
    print()





def example1():
    'basic string operations , slicing and concatenating'
    str1 = "foo"
    str2 = "bar"
    str_combined = str1 + str2
    str = str_combined
    str3 = copy.copy(str_combined)
    str4 = copy.deepcopy(str_combined)
    print('str1 = ', str1)
    print('str2 = ', str2)
    print('str_combined = ', str_combined)
    print('str = ', str)
    print('str is str_combined = ', (str is str_combined))
    print('str3 = ', str3)
    print('str3 is str_combined = ', (str3 is str_combined))
    print('str4 = ', str4)
    print('str4 is str_combined = ', (str4 is str_combined))
    print('str3[0:3] = ', str3[0:3])
    print('str3[3:] = ', str3[3:])
    print()


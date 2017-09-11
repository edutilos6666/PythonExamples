def example1():
    id , name, age, wage, active = None, None, None, None, None
    print('insert id: ')
    id = int(input())
    print('insert name: ')
    name = input()
    print('insert age: ')
    age = int(input())
    print('insert wage: ')
    wage = float(input())
    print('insert whether you  are active: ')
    active = True if (input().lower() == 'true') else False

    print('id = ', str(id))
    print('name = ', str(name))
    print('age = ', str(age))
    print('wage = ', str(wage))
    print('active = ', str(active))


    if age > 0 and age < 10:
        print(name , ' is still a kid.')
    elif age >=10 and age < 20:
        print(name , ' is a teenager.')
    elif age >=20 and age < 40:
        print(name , ' is an adult.')
    else:
        print(name, ' is an elderly.')


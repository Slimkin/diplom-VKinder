from menu import about_fromAges, about_gender, about_toAges, about_status

def gender():
    choice = input('-> ')
    if choice == '0':
        gen = '2'    
    elif choice == '1':
        gen = '1'
    elif choice == 'q':
        print('выход')
        exit(0)
    else:
        print('введено неправильное значение, попробуйте еще раз')
        gender()
    return gen


def from_ages():
    try:
        age = int(input('-> '))
    except ValueError:
        print('введено неправильное значение\n0 - попробовать еще раз\nq - для выхода')
        choice = input('-> ')
        if choice == '0':
            print('\nвведите возраст от которого осуществляется поиск')
            from_ages()
        elif choice == 'q':
            print('выход')
            exit(0)
        else:
            print('введено неправильное значение, попробуйте еще раз\nвведите возраст от которого осуществляется поиск')
            from_ages()
        return age
    fa = str(age)
    return fa


def to_ages():
    try:
        age = int(input('-> '))
    except TypeError:
        print('введено неправильное значение\n0 - попробовать еще раз\nq - для выхода')
        choice = input('-> ')
        if choice == '0':
            to_ages()
        elif choice == 'q':
            print('выход')
            exit(0)
        else:
            print('введено неправильное значение, попробуйте еще раз\nвведите возраст до которого осуществляется поиск')
            to_ages()
        return age
    ta = str(age)
    return ta


def status():
    choice = input('-> ')
    if choice == '0':
        stat = '0'    
    elif choice == '1':
        stat = '1'
    elif choice == 'q':
        print('выход')
        exit(0)
    else:
        print('введено неправильное значение, попробуйте еще раз')
        status()
    return stat


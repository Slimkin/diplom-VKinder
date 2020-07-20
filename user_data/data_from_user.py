
def gender():
    choice = input('-> ')
    if choice == '0':
        gen = '2'
        return gen
    elif choice == '1':
        gen = '1'
        return gen
    elif choice == 'q':
        print('выход')
        raise SystemExit
    else:
        print('введено неправильное значение, попробуйте еще раз')
        return gender()


def from_ages():
    try:
        age = int(input('-> '))
        return age
    except ValueError:
        print('введено неправильное значение\n0 - попробовать еще раз\nq - для выхода')
        choice = input('-> ')
        if choice == '0':
            print('\nвведите возраст от которого осуществляется поиск')
            return from_ages()
        elif choice == 'q':
            print('выход')
            raise SystemExit
        else:
            print('введено неправильное значение, попробуйте еще раз\nвведите возраст от которого осуществляется поиск')
            return from_ages()
    fa = str(age)
    return fa


def to_ages():
    try:
        age = int(input('-> '))
        return age
    except TypeError:
        print('введено неправильное значение\n0 - попробовать еще раз\nq - для выхода')
        choice = input('-> ')
        if choice == '0':
            return to_ages()
        elif choice == 'q':
            print('выход')
            raise SystemExit
        else:
            print('введено неправильное значение, попробуйте еще раз\nвведите возраст до которого осуществляется поиск')
            return to_ages()
    ta = str(age)
    return ta


def status():
    choice = input('-> ')
    if choice == '0':
        stat = '0'
        return stat
    elif choice == '1':
        stat = '1'
        return stat
    elif choice == 'q':
        print('выход')
        raise SystemExit
    else:
        print('введено неправильное значение, попробуйте еще раз')
        return status()


def choise():
        choice = input('-> ')
        if choice == '0':
            return '0'
        elif choice == '1':
            return '1'
        elif choice == 'q':
            print('выход')
            raise SystemExit
        else:
            print('введено неправильное значение, попробуйте еще раз')
            return choise()


def name_for_db():
    name = input('-> ')
    return name
def convert_base_R(num, to_base=10, from_base=10):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base_R(n // to_base, to_base) + alphabet[n % to_base]
try:
    print('Выберите операцию:\n1) сложение\n2) умножение\n3) вычитание\n4) деление (только целочисленное)\nВаш выбор: ', end = '')
    task = int(input())
    a, b = input('Введите два числа в произвольных ' +
                 'системах счисления через пробел: ').split()
    a_base, b_base = map(int, input('Введите системы счисления ' +
                                    'чисел через пробел: ').split())
    a_10 = int(convert_base_R(a, from_base = a_base))
    b_10 = int(convert_base_R(b, from_base = b_base))
    if b_10 == 0 and task == 4:
        raise ZeroDivisionError
    c_base = int(input('Введите систему счисления результата: '))
    if task == 1:
        print('Результат:', convert_base_R(a_10 + b_10, to_base = c_base))
    elif task == 2:
        print('Результат:', convert_base_R(a_10 * b_10, to_base = c_base))
    elif task == 3:
        print('Результат:', convert_base_R(a_10 - b_10, to_base = c_base))
    elif task == 4:
        print('Результат:', convert_base_R(a_10 // b_10, to_base = c_base))
except ValueError:
    print('Ошибка введенных данных.')
except ZeroDivisionError:
    print('Ошибка деления на ноль.')
except IndexError:
    print('Ошибка индекса.')
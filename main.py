import math
print('Введите операцию: ')
oper = int(0)
while oper != 11:
    print('Сложение двух чисел - 1')
    print('Вычесть из первого числа второе - 2')
    print('Перемножить два числа - 3')
    print('Деление первого числа на второе - 4')
    print('Возвести в степень N первое число - 5')
    print('Найти квадратный корень числа - 6')
    print('Найти факториал числа - 7')
    print('Найти косинус - 8')
    print('Найти синус - 9')
    print('Найти тангенс - 10')
    print('Чтоб выйти из программы введите - 11')
    oper = int(input())
    if oper == 1:
        a = int(input('Введите первое число ' ))
        b = int(input('Введите второе число ' ))
        res = a + b
        print(res)
    elif oper == 2:
        a = int(input('Введите первое число '))
        b = int(input('Введите второе число '))
        res = a - b
        print(res)
    elif oper == 3:
        a = int(input('Введите первое число '))
        b = (int(input('Введите второе число ')))
        res = a * b
        print(res)
    elif oper == 4:
        a = int(input('Введите первое число '))
        b = int(input('Введите второе число '))
        if b == 0:
            print('Делить на 0 нельзя')
        else:
            res = a // b
            print(res)
    elif oper == 5:
        a = int(input('Введите первое число '))
        b = int(input('Введите второе число '))
        res = a ** b
        print(res)
    elif oper == 6:
        a = int(input('Введите число '))
        if a < 0:
            print('У отрицательных чисел нет корней')
        else:
            print(math.sqrt(a))
    elif oper == 7:
        a = int(input('Введите число '))
        print(math.factorial(a))
    elif oper == 8:
        a = int(input('Введите число '))
        print(math.cos(a))
    elif oper == 9:
        a = int(input('Введите число '))
        print(math.sin(a))
    elif oper == 10:
        a = int(input('Введите число '))
        print(math.tan(a))
    elif oper > 11:
        print('Введите одну из перечисленных операций')
def positive():
    print("Положительное")

def negative():
    print("Отрицательное")

def test():
    x = int(input("Введите целое число: "))
    if x > 0:
        positive()
    elif x < 0:
        negative()

test()
 
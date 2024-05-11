
x = 1 + 2 + 3 + 4 + 5
x = float(x)
i=5
a = 10
while True:
    a = input("Введите число ")
    if a=="0":
        break
    i += 1
    x += float(a)
    y = (x / i)
    print(f"Среднее значение этих {i} чисел равно {y:.5f}") 

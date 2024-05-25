def Write_file():
    with open('Numbers', 'a') as File:
        numbers = list(map(str, input('Введите все числа через пробел: ').split()))
        for i in numbers:
            File.writelines(i + '\n')
def Read_file():
    try:
        with open('Numbers', 'r') as File:
            for line in File:
                try:
                    num = float(line)
                    maximum = num
                    minimum = num
                    summa = 0
                    if num > maximum:
                        maximum = num
                    if num < minimum:
                        minimum = num
                    summa += num
                except:
                    pass
    except:
        return print('Ошибка чтения файла')
    return str(maximum), str(minimum), str(summa)

def Operatinon(a):
    with open('Numbers', 'a') as File:
        File.write(a[0] + '\n')
        File.writelines(a[1] + '\n')
        File.writelines(a[2] + '\n')
for i in range(10):
    Write_file()
    Operatinon(Read_file())
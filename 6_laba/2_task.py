def Write_file():
    with open('Numbers', 'a') as File:
        numbers = list(map(str, input('Введите все числа через пробел: ').split()))
        for i in numbers:
            File.writelines(i + '\n')
def Read_file():
    max_num = float('-inf')
    min_num = float('inf')
    sum_num = 0
    with open('Numbers', 'r') as File:
        for line in File:
            try:
                x = float(line)
                if x > max_num:
                    max_num = x
                if x < min_num:
                    min_num = x
                sum_num += float(line)
            except:
                pass
    return max_num, min_num, sum_num

def Operatinon(a):
    with open('Numbers', 'a') as File:
        File.write(str(a[0]) + '\n')
        File.writelines(str(a[1]) + '\n')
        File.writelines(str(a[2]) + '\n')

Write_file()
Operatinon(Read_file())

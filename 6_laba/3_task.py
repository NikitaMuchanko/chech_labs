def Total():
    with open('Kino', 'r') as f:
        x = f.readlines()
        temp = []
        total = []
        for Lines in range(len(x)):
            for Element in x[Lines]:
                if Element in '01':
                    temp.append(Element)
            total.append(temp)
            temp = []
    return total

def Counter():
    total_places = Total()

    Places_all = 0
    Places = 0

    for i in range(len(total_places)):
        Places_all += total_places[i].count('0') + total_places[i].count('Base')
        Places += total_places[i].count('0')
        print(f'На ряду номер {i}: {total_places[i].count('0')} свободных мест')
    num1, num2 = map(int, input('\nВведите номер ряда и места через пробел (отсчёт начинать с 0): ').split())
    if total_places[num1][num2] == '0':
        print('Данное место свободно')
    elif total_places[num1][num2] == 'Base':
        print('Данное место занято')

Counter()


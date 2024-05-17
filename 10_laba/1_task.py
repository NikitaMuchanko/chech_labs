numbers = ["999999", "888888", "000000", "123456", "9093393043"] 
const_max_len = max([len(i) for i in numbers])
numbers_pos = [0]*len(numbers)
position = 0
privious = ''
with open("pi-10million.txt") as f:
    while True:
        data = privious + f.read()
        if data == privious: 
            break
        for i in range(len(numbers)):
            if numbers_pos[i] == 0:
                j = data.find(numbers[i])
                if j != 0: numbers_pos[i] = j + position
 
        position = position + len(data) - const_max_len
        privious = data[-const_max_len:]
 
for (a, b) in zip(numbers, numbers_pos):
    print(f'{a} имеет индекс {b-1}')
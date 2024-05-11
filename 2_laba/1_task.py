
number = input("Введите четырехзначное число: ")

number = str(number)
if len(number)<4:
    number= number + '0'*(4-len(number))

if number == number[::-1]:
    print(1)
else:
    print(0)

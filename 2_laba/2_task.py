# Ввод года
year = int(input("Введите год: "))

# Проверка, является ли год високосным
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("YES")
else:
    print("NO")

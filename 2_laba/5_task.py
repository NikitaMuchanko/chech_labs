numbers = []
count = 0

while True:
    num = int(input("Введите число (0 для завершения): "))
    if num == 0:
        break
    numbers.append(num)
    count += 1

operation = int(input("Выберите операцию:\n1. Сумма\n2. Произведение\n3. Среднее значение\n4. Максимальное число\n5. Минимальное число\n6. Количество четных и нечетных чисел\n"))

if operation == 1:
    print("Сумма:", sum(numbers))
elif operation == 2:
    product = 1
    for num in numbers:
        product *= num
    print("Произведение:", product)
elif operation == 3:
    print("Среднее значение:", sum(numbers) / count)
elif operation == 4:
    print("Максимальное число:", max(numbers))
elif operation == 5:
    print("Минимальное число:", min(numbers))
elif operation == 6:
    even_count = sum(1 for num in numbers if num % 2 == 0)
    odd_count = count - even_count
    print("Количество четных чисел:", even_count)
    print("Количество нечетных чисел:", odd_count)
else:
    print("Неверный выбор операции.")

def guess_number(N):
    start = 1
    end = N
    while start <= end:
        mid = (start + end) // 2
        print(f"Загаданное число находится в первой половине диапазона? (да/нет)")
        answer = input().lower()
        if answer == "да":
            end = mid - 1
        else:
            start = mid + 1
    print(f"Загаданное число: {start}")

# Запрос N от пользователя
N = int(input("Введите N: "))
guess_number(N)

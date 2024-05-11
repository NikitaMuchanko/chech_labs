def sum_digits():
    total_sum = 0
    while True:
        user_input = input("Введите строку (цифры): ")
        if user_input.isdigit():
            total_sum += int(user_input)
            print(f"Сумма: {total_sum}")
            break
        else:
            print("Введенная строка не состоит только из цифр. Попробуйте еще раз.")

sum_digits()

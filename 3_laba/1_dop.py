correct_answers = 0
wrong_answers = 0
last_three_correct = 0
last_three_wrong = 0

while correct_answers < 5:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    
 
    correct_answer = num1 * num2
    
    
    user_answer = int(input(f"Результат умножения {num1} на {num2}? "))
    
    if user_answer == correct_answer:
        print("Правильно!")
        correct_answers += 1
        last_three_correct += 1
        last_three_wrong = 0
    else:
        print("Неправильно. Правильный ответ:", correct_answer)
        wrong_answers += 1
        last_three_correct = 0
        last_three_wrong += 1
    
    
    if last_three_correct >= 3:
        print("Отлично Ты продолжаешь улучшать свои знания.")
    
    
    if last_three_wrong >= 3:
        print("Не забудь про таблицу умножения!")

print("Yспешно сдал тест по таблице умножения!")

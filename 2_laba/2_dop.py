def min_cooking_time(k, m, n):
    # Вычисляем общее время обжаривания всех котлет
    total_cooking_time = n * m
    
    # Учитываем, что на сковородку можно положить только k котлет одновременно
    cooking_intervals = n // k
    remaining_cooklets = n % k
    
    if remaining_cooklets > 0:
        cooking_intervals += 1
    
    # Время обжаривания всех котлет, учитывая ограничение по количеству котлет на сковородку
    total_cooking_time = cooking_intervals * m
    
    return total_cooking_time

# Пример использования функции
k = 5
m = 10
n = 20
print(min_cooking_time(k, m, n))

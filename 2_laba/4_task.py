

def find_smallest_divisor(n):
    i = 2
    while i <= n:
        if n % i == 0:
            return i
        i += 1
n = int(input("Введите число: "))
print(find_smallest_divisor(n))




def find_smallest_divisor(n):
    for i in range(2, n + 1):
        if n % i == 0:
            return i

# Пример использования
n = int(input("Введите число: "))
print(find_smallest_divisor(n))

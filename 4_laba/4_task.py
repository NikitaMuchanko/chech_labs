def find_loser(n, m):
   
    total_cubes = 0
    for i in range(1, n + 1):
        total_cubes += i * 2
        if total_cubes > m:
            total_cubes -= 25
            break

    
    for i in range(1, n + 1):
        if total_cubes >= m:
            return i
        total_cubes -= 25

    return n + 1  


n = int(input("Введите количество детей: "))
m = int(input("Введите количество кубиков в куче: "))


loser = find_loser(n, m)
print(f"Проигравшим является ребенок номер {loser}.")

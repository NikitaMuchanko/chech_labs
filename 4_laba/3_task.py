import math

def fibonacci_formula(n):
    a = ((1 + math.sqrt(5)) / 2)**n
    b = ((1 - math.sqrt(5)) / 2)**n
    return (a-b)/ math.sqrt(5)

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def find_n():
    n = 1
    while True:
        formula_result = fibonacci_formula(n)
        recursive_result = fibonacci_recursive(n)
        difference = abs(formula_result - recursive_result)
        if difference > 0.001:
            return n
        n += 1


n = find_n()
print(f"n, при котором разница превышает 0.001: {n}")

def f(a, b):
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            j += 1
        i += 1
    return j == len(b)

a = [1, 2, 3, 4, 5]
b = [1, 3, 5]
print(f(a, b))  

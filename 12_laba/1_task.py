
def f(start, stop):
    if start > stop:
        return 0
    if start == stop: 
        return 1
    if start <stop:
        return f(start+1, stop) + f(start+2, stop) + f(start*3, stop)
n = int(input("Введите число n  "))
print(f(1,n))

def move(n, source, target, auxiliary):
    if n == 1:
        print(f"Переложите диск 1 с  {source} на {target}")
        return
    move(n-1, source, auxiliary, target)
    print(f"Переложите диск {n} с  {source} на {target}")
    move(n-1, auxiliary, target, source)
    
move(2, 'A', 'C', 'B') 




def move_iterative(n, source, target, auxiliary):
    stack = [(n, source, target, auxiliary)]
    while stack:
        n, source, target, auxiliary = stack.pop()
        if n == 1:
            print(f"Переложите диск {n} с  {source} на {target}")
        else:
            stack.append((n-1, source, auxiliary, target))
            stack.append((1, source, target, auxiliary))
            stack.append((n-1, auxiliary, target, source))

move_iterative(2, 'A', 'C', 'B')  

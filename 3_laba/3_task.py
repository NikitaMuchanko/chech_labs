#1 y=-x
def f1(x,y ):
    return (y <= -x) or ((x>=4 ) and (y>=3))

print(f1(1,-1))

#2 (x**2)+(y**2)>= 9
def f2(x,y):
    return ((x**2 + y**2) == 9) and ((x<=3 and x>=-3) and (y<=3 and y>=-3))
print(f2((-3,3)))

#3 (x-5)**2 + (y-5)**2 = 25

def f3(x,y):
    return ((x-5)**2 + (y-5)**2 >=25) and (y < (-x+5)) and (y>=0) and (y<=5) and (x>=0) and (x<=5)

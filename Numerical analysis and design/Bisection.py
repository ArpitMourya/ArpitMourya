def f(x):
    a = pow(x,3)
    c = 2*x
    d = -5
    return a-c+d
a = 0.0
b= 0.0
result = 0
for i in range(-100 ,100,1):
    if f(i)>0:
        b = i
    elif f(i)<(0):
        a = i
    if f(a)*f(b)<0:
        break
x=0
x1 = 1000
temp = 0
while round(x,3)!=round(x1,3):
    x1 = temp
    uper = (b-a) * f(a)
    lowr = (f(b)-f(a))
    x = a-(uper/lowr)
    temp = x
    if f(x)*f(a)<0:
        b=x
    elif f(a)*f(x)>0:
        a=x
    elif f(x)==0:
        result = x
        break
print(x)



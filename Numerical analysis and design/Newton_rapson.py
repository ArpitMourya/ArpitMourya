import sympy
x = sympy.symbols('x')
fb =lambda x: x**3-5*x+3
f = x**3-5*x+3
df = sympy.diff(f,x)
a = 0.0
b= 0.0
result = 0
for i in range(-10 ,50,1):
    if fb(i)>0:
        b = i
    elif fb(i)<(0):
        a = i
    if fb(a)*fb(b)<0:
        break
x0 = (a + b)/2
temp  = x0
x1 = 1000
while round(x0,2)!= round(x1,2):
    x0 = temp
    x1 = x0-(fb(x0) / df.subs(x,x0)) 
    temp = x1
print(x1)


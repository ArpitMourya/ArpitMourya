import numpy as np

z=1
t = np.array([1996,1997,1998,1999,2000])
y = np.array([70,74,80,86,90])
x = np.array(list(i-t[2] for i in t))
sum_y=np.sum(y)
sum_x=np.sum(x)
sum_x2 = np.sum(np.fromiter((i**2 for i in x),int))
sum_xy = np.sum(list(i*y[id] for id,i in enumerate(x,0)))
a = sum_y/len(t)
b=sum_xy/sum_x2
print(a,b)
z=int(input("At what point to predict "))
Y = a+(b*z)
print(Y)

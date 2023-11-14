import numpy as np
import matplotlib.pyplot as plt

  
# Adding the title

  
# Adding the labels
z=1
t = np.array([1990,1991,1992,1993,1994,1995,1996])
y = np.array([6,7,5,4,6,7,5])
x = np.array(list(i-t[3] for i in t))
plt.plot(t, y)
plt.title("Simple Plot")
x2 = np.array(list(i**2 for i in x))
sum_y=np.sum(y)
sum_x=np.sum(x)
sum_x2 = np.sum(x2)
sum_x3= np.sum(np.fromiter((i**3 for i in x),int))
sum_x4 = np.sum(np.fromiter((i**4 for i in x),int))
sum_x2y = np.sum(np.fromiter((i*y[id] for id,i in enumerate(x2,0)),int))
sum_xy = np.sum(list(i*y[id] for id,i in enumerate(x,0)))
b=sum_xy/sum_x2
# var = int(input("value of x  "))
eq1=np.array(([[len(t),sum_x2] ,[sum_x2,sum_x4]]))
eq2 = np.array(([sum_y],[sum_x2y]))
a ,c = np.linalg.solve(eq1,eq2)
for var in range(0,10):
    # print(a,b,c)
    z = float(a) + (b * var) + float(c) * (var**2) 
    print(z)
plt.ylabel("y-axis")
plt.xlabel("t-axis")
plt.show()
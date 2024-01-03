import numpy as np
import matplotlib.pyplot as plt

t = np.array([1996,1997,1998,1999,2000])
y = np.array([70,74,80,86,90])
x = np.array(list(i-t[0] for i in t))
sum_y=np.sum(y)
sum_x=np.sum(x)
sum_x2 = np.sum(np.fromiter((i**2 for i in x),int))
sum_xy = np.sum(list(i*y[id] for id,i in enumerate(x,0)))
A=np.array([[len(t),sum_x],[sum_x,sum_x2]])
z=np.array([sum_y,sum_xy])
a,b = np.linalg.solve(A,z)
test=2003
Y=a+(b*(test-t[0]))
plt.scatter(t,y,color='red')
plt.plot(list(range(1996,2004)),[a+(b*(i-t[0])) for i in range(1996,2004)],color='green')
plt.show()
print(a,b)
print("Answer",Y)

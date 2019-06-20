import numpy as np
from math import sqrt
import matplotlib.pyplot as plt

#slope of best fit line = b = r(sy/sx) {corrcoefxy* standard deviation of y over standard deviation of x}
#y-intercept of best fit line = a = mean of y - b(mean of x)
fname = 'anscombe.txt'
dtype1 = np.dtype([('x1', 'f4'), ('y1', 'f4'), ('x2', 'f4'), ('y2', 'f4'), ('x3', 'f4'), ('y3', 'f4'), ('x4', 'f4'), ('y4', 'f4')])
a = np.loadtxt(fname, dtype=dtype1, usecols=(0,1,2,3,4,5,6,7))

print(a)

mean_x1 = np.mean(a['x1'])
var_x1 = np.var(a['x1'])
print(f"The mean of x1 is {mean_x1} and the variance of x1 is {var_x1}.")
mean_y1 = np.mean(a['y1'])
var_y1 = np.var(a['y1'])
print(f"The mean of y1 is {mean_y1} and the variance of y1 is {var_y1}.")
corrcoefx1y1= np.corrcoef(a['x1'], a['y1'])[0,1]
print(f"The correlation coefficient between x1 and y1 is {corrcoefx1y1}.")
slope_x1y1= corrcoefx1y1*sqrt(var_y1)/sqrt(var_x1)
y_intercept_x1y1= mean_y1 - (slope_x1y1*mean_x1)
print(f"y = {slope_x1y1}x + {y_intercept_x1y1}")
print("\n")

plt.scatter(a['x1'], a['y1'])
plt.xlabel('x1')
plt.ylabel('y1')
f = lambda x: slope_x1y1*x + y_intercept_x1y1
x= np.array([min(a['x1']), max(a['x1'])])
plt.plot(x, f(x), c ="orange", label = "best fit line")
plt.legend()
plt.show()


mean_x2 = np.mean(a['x2'])
var_x2 = np.var(a['x2'])
print(f"The mean of x2 is {mean_x2} and the variance of x2 is {var_x2}.")
mean_y2 = np.mean(a['y2'])
var_y2 = np.var(a['y2'])
print(f"The mean of y2 is {mean_y2} and the variance of y2 is {var_y2}.")
corrcoefx2y2 = np.corrcoef(a['x2'], a['y2'])[0,1]
print(f"The correlation coefficient between x2 and y2 is {corrcoefx2y2}.")
slope_x2y2 = corrcoefx1y1*sqrt(var_y2)/sqrt(var_x2)
y_intercept_x2y2 = mean_y2 - (slope_x2y2*mean_x2)
print(f"a = {slope_x2y2}b + {y_intercept_x2y2}")
print("\n")

plt.scatter(a['x2'], a['y2'])
plt.xlabel('x2')
plt.ylabel('y2')
g = lambda q: slope_x2y2*q + y_intercept_x2y2
q = np.array([min(a['x2']), max(a['x2'])])
plt.plot(q, g(q), c ="red", label= "best fit line")
plt.legend()
plt.show()


mean_x3 = np.mean(a['x3'])
var_x3 = np.var(a['x3'])
print(f"The mean of x3 is {mean_x3} and the variance of x3 is {var_x3}.")
mean_y3 = np.mean(a['y3'])
var_y3 = np.var(a['y3'])
print(f"The mean of y3 is {mean_y3} and the variance of y3 is {var_y3}.")
corrcoefx3y3 = np.corrcoef(a['x3'], a['y3'])[0,1]
print(f"The correlation coefficient between x3 and y3 is {corrcoefx3y3}.")
slope_x3y3= corrcoefx3y3*sqrt(var_y3)/sqrt(var_x3)
y_intercept_x3y3= mean_y3 - (slope_x3y3*mean_x3)
print(f"d = {slope_x3y3}f + {y_intercept_x3y3}")
print("\n")

plt.scatter(a['x3'], a['y3'])
plt.xlabel('x3')
plt.ylabel('y3')
h = lambda n: slope_x3y3*n + y_intercept_x3y3
n = np.array([min(a['x3']), max(a['x3'])])
plt.plot(n, h(n), c = "pink", label= "best fit line")
plt.legend()
plt.show()

mean_x4 = np.mean(a['x4'])
var_x4 = np.var(a['x4'])
print(f"The mean of x4 is {mean_x4} and the variance of x4 is {var_x4}.")
mean_y4 = np.mean(a['y4'])
var_y4 = np.var(a['y4'])
print(f"The mean of y4 is {mean_y4} and the variance of y4 is {var_y4}.")
corrcoefx4y4= np.corrcoef(a['x4'], a['y4'])[0,1]
print(f"The correlation coefficient between x4 and y4 is {corrcoefx4y4}.")
slope_x4y4= corrcoefx4y4*sqrt(var_y4)/sqrt(var_x4)
y_intercept_x4y4= mean_y4 - (slope_x4y4*mean_x4)
print(f"e = {slope_x4y4}g + {y_intercept_x4y4}")
print("\n")

plt.scatter(a['x4'], a['y4'])
plt.xlabel('x4')
plt.ylabel('y4')
p = lambda r: slope_x4y4*r + y_intercept_x4y4
r = np.array([min(a['x4']), max(a['x4'])])
plt.plot(r, p(r), c = "black", label="best fit line")
plt.legend()
plt.show()

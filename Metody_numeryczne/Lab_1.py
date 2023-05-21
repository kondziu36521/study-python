import numpy as np
import scipy
import matplotlib.pyplot as plt
import math

a=2
x=1
abserr=1.0E-5

my_x=[]
my_y=[]

#program glowny
xnew=0
iter=1

while iter <= 10:
     xnew=x/2+0.5*a/x
     my_x.append(iter)
     my_y.append(xnew)

     if abs(xnew-x)<abserr:
        x=xnew
     else:
        x=xnew

    iter+=1

print("sqrt(%g)=%.5g error=%g iter=%d\n",a,xnew, xnew-math.sqrt(a), iter)
plt.scatter(my_x, my_y, color='darkgreen', marker='^')


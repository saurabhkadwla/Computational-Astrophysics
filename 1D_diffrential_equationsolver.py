import sys
import numpy as np
import matplotlib.pyplot as plt

#defining exact solution
def sol_ana(y, x): # exact solution
  return np.exp(-0.5*x**2)


def fxy(y, x):#Right hand side 
  return (-x*y)
  
  
x0 = 0.0
xm = 10.0
N = 100 # No. of points which divides x0 to xm on no. line
xv = np.linspace(x0,xm,N) 
h = xv[1]-xv[0] 

y_num = np.zeros(N) # assigning for RK 2nd order
y_num[0] = 1.0

y_eul = np.zeros(N)
y_eul[0] = 1.0 

y_R_K_4 = np.zeros(N)
y_R_K_4[0] = 1.0


#Runge kutta 2nd order
for i in range(1,N):
  k_1 = h*fxy(y_num[i-1],xv[i-1])
  k_2 = h*fxy(y_num[i-1]+k_1,xv[i-1]+h)
  y_num[i] = y_num[i-1] + 0.5*(k_1 + k_2)

# Euler method
  y_eul[i] = y_eul[i-1] + h*fxy(y_eul[i-1],xv[i-1])

#Runge kutta 4th order

  k_1 = h*fxy(y_R_K_4[i-1],xv[i-1])
  k_2 = h*fxy(y_R_K_4[i-1]+0.5*k_1,xv[i-1]+0.5*h)
  k_3 = h*fxy(y_R_K_4[i-1]+0.5*k_2,xv[i-1]+0.5*h)
  k_4 = h*fxy(y_R_K_4[i-1]+k_3,xv[i-1]+h)
  y_R_K_4[i] = y_R_K_4[i-1] + 0.1666*(k_1+2*k_2+2*k_3+k_4)

y_ana = sol_ana(0.0, xv)
error_euler = ((np.sum((y_ana - y_eul)**2))/N)**(1/2)
error_rk2 = ((np.sum((y_ana - y_num)**2))/N)**(1/2)
error_rk4 = ((np.sum((y_ana - y_R_K_4)**2))/N)**(1/2)
print(error_rk4,error_rk2,error_euler)

 
 
#Error Propgation with N

z = np.arange(N)


error_euler, error_rk2, error_rk4  = np.zeros(N),np.zeros(N),np.zeros(N)
for i in range(N):
    error_rk4[i] = ((np.sum((y_ana - y_R_K_4[i])**2))/i)**(1/2)
    error_euler[i] = ((np.sum((y_ana - y_eul[i])**2))/i)**(1/2)
    error_rk2[i] = ((np.sum((y_ana - y_num[i])**2))/i)**(1/2)


# plotting x vs y

plt.plot(xv, y_num, 'r--',label="R.k. 2nd")
plt.plot(xv, y_ana, 'k',label="Analytical")
plt.plot(xv,y_eul,'g',label="Euler")
plt.plot(xv,y_R_K_4,'b',label="R.K. 4th")
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()
sys.exit()


# plotting Error propgation 
plt.plot(z,error_rk4,'o')
plt.plot(z,error_euler,'+')
plt.plot(z,error_rk2,'k')
sys.exit()

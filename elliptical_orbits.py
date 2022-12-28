import numpy as np 
import matplotlib.pyplot as plt

theta_0 = 0
theta_m = 2*np.pi
N = 1000

theta = np.linspace(theta_0,theta_m,N) 
e = 0.8 # eccentricity
a = 5.0

h = theta[1] - theta[0]

u_num = np.zeros(N) #Intializing for Euler method
u_num[0] = 1.0

v_num = np.zeros(N)

u_R_k2 = np.zeros(N) #Intializing for RK 2nd order
u_R_k2[0] = 1.0

v_R_k2 = np.zeros(N)


def R(u): # right hand side of 2nd order diffrential equation
    return 1/(a*(1-e**2)) - u

def f(v): # putting "du/dtheta" = v = f(v)
    return v
  
#Euler Method
for i in range(1,N):
    v_num[i] = v_num[i-1] +h*R(u_num[i-1])
    u_num[i] = u_num[i-1] + h*f(v_num[i-1])



#Runge-kutta 2nd order
    k_1 = h*R(u_R_k2[i-1])
    c_1 = h*f(v_R_k2[i-1])
    c_2 = h*f(v_R_k2[i-1] + k_1/2)
    k_2 = h*R(u_R_k2[i-1] + c_1/2)   
    v_R_k2[i] = v_R_k2[i-1] + k_2
    u_R_k2[i] = u_R_k2[i-1] + c_2

r = 1/u_num # r = 1/u

r_R_K2 = 1/u_R_k2

r_exact = a*(1-e**2)/(1+e*np.cos(theta-theta_0)) #Exact solution

plt.polar('equal')

#plotting r vs theta graph 

plt.plot(theta,r_exact,"k--")

plt.polar(theta,r,"g--")
plt.polar(theta,r_R_K2,"b")
plt.show()


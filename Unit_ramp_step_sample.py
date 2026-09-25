import numpy as np
import matplotlib.pyplot as plt

# Index Range
n = np.arange(-10,11)

# Elementary discrete signal
def unit_sample(n):
    return np.where(n == 0, 1, 0)

def unit_step(n):
    return np.where(n >= 0, 1, 0)

def unit_ramp(n):
    return np.where(n >= 0, n, 0)

delta = unit_sample(n)
u = unit_step(n)
r = unit_ramp(n)

# print("n  =",n)
# print("d(n)=",delta)
# print("u(n)=",u)
# print("r(n)=",r)

plt.figure(figsize=(8,6))

plt.subplot(3,1,1)
plt.stem(n,delta)
plt.title("Unit Sample Signal d(n)")
plt.xlabel('n')
plt.ylabel('d(n)')
plt.grid()

plt.subplot(3,1,2)
plt.stem(n,u)
plt.title("Unit Step Signal d(n)")
plt.xlabel('n')
plt.ylabel('u(n)')
plt.grid()

plt.subplot(3,1,3)
plt.stem(n,r)
plt.title("Unit Sample Signal d(n)")
plt.xlabel('n')
plt.ylabel('r(n)')
plt.grid()

plt.tight_layout()
plt.show()
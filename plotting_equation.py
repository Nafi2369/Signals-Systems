import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-7,8)

def impulse(n,n0):
    return np.where(n == n0, 1, 0)

# X(n) = 2*delta(n+2) - delta(n-4)
x = 2*impulse(n,-2) - impulse(n,4)

# print if u want

plt.figure(figsize=(9,5))
plt.stem(n,x)
plt.title('X(n) = 2δ(n+2) − δ(n−4),   −7 ≤ n ≤ 7') 
plt.xlabel('n')
plt.ylabel('X(n)')
plt.xticks(n)
plt.grid()
plt.show()
import numpy as np
import matplotlib.pyplot as plt

def sig_add(x1,n1,x2,n2):
    n = np.arange(min(n1.min(),n2.min()), max(n1.max(), n2.max())+1)
    y1 = np.zeros(len(n))
    y2 = np.zeros(len(n))
    y1[(n >= n1.min()) & (n <= n1.max())] = x1
    y2[(n >= n2.min()) & (n <= n2.max())] = x2
    return y1+y2, n

def sig_fold(x, n):
    return x[::-1], -n[::-1]

def sig_shift(x,n,k):
    # y(n) = x(n-k)
    return x, n+k

# input sequences
x1 = np.array([1,2,3,4,3,2,1])
n1 = np.arange(-3,4)

x2 = np.array([2,2,1,1,0.5])
n2 = np.arange(0,5)

x_add, n_add = sig_add(x1,n1,x2,n2)
x_fold, n_fold = sig_fold(x2,n2)
x_shift, n_shift = sig_shift(x2, n2, 3)

plt.figure(figsize=(9,10))

plt.subplot(5,1,1)
plt.stem(n1,x1)
plt.title("x1(n)")
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid()

plt.subplot(5,1,2)
plt.stem(n2,x2)
plt.title("x2(n)")
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid()

plt.subplot(5,1,3)
plt.stem(n_add,x_add)
plt.title("Addition: y(n) = x1(n)+x2(n)")
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid()

plt.subplot(5,1,4)
plt.stem(n_fold,x_fold)
plt.title("Folding: y(n) = x(-n)")
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid()

plt.subplot(5,1,5)
plt.stem(n_shift,x_shift)
plt.title("Shifting: y(n) = x(n-3)")
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid()

plt.tight_layout()
plt.show()
import numpy as np
import matplotlib.pyplot as plt

def sig_conv(x, nx, h, nh):
    N = len(x) + len(h) -1
    y = np.zeros(N)
    for n in range(N):
        for k in range(len(x)):
            if 0 <= n-k < len(h):
                y[n] += x[k] * h[n-k]
    ny = np.arange(nx[0]+nh[0], nx[0]+nh[0]+N)
    return y,ny

x = np.array([1,2,3,1])
nx = np.arange(-1,3)

h = np.array([1,1,1])
nh = np.arange(0,3)

y,ny = sig_conv(x,nx,h,nh)

y1 = np.convolve(x,h)

plt.figure(figsize=(8,10))

plt.subplot(4,1,1)
plt.stem(nx,x)
plt.title('Input sequence x(n)')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.xlim(-2,6)
plt.grid()

plt.subplot(4,1,2)
plt.stem(nh,h)
plt.title('Impulse response h(n)')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.xlim(-2,6)
plt.grid()

plt.subplot(4,1,3)
plt.stem(ny,y)
plt.title('Convoluted Output y(n)')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.xlim(-2,6)
plt.grid()

plt.subplot(4,1,4)
plt.stem(ny, y1)
plt.title('Checking with built-in function')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.xlim(-2,6)
plt.grid()

plt.tight_layout()
plt.show()
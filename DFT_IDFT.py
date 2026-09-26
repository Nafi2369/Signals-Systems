import numpy as np
import matplotlib.pyplot as plt

# Dft: X(k) = sum_{n=0}^{N-1} x(n) e^{-j2*pi*k*n/N}
def dft(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape(N,1)
    W = np.exp(-2j*np.pi*k*n/N)
    return W @ x

# Idft: x(n) = (1/N) sum_{k=0}^{N-1} X(k) e^{j2*pi*k*n/N}
def idft(X):
    N = len(X)
    k = np.arange(N)
    n = k.reshape((N,1))
    W = np.exp(2j*np.pi*k*n/N)
    return (W @ X) / N

x = np.array([1,2,3,4,4,3,2,1])
N = len(x)
k = np.arange(N)

X = dft(x)
x_rec = idft(X)

plt.figure(figsize=(9,10))

plt.subplot(4,1,1)
plt.stem(k, x)
plt.title('Original Sequnce x(n)')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid()

plt.subplot(4,1,2)
plt.stem(k, np.abs(X))
plt.title('DFT Magnitude |X(k)|')
plt.xlabel('k')
plt.ylabel('Magnitude')
plt.grid()

plt.subplot(4,1,3)
plt.stem(k, np.angle(X))
plt.title('DFT Phase <X(k)')
plt.xlabel('k')
plt.ylabel('Phase(rad)')
plt.grid()

plt.subplot(4,1,4)
plt.stem(k, x_rec.real)
plt.title('Reconstructed using IDFT')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid()

plt.tight_layout()
plt.show()
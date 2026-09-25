import numpy as np
import matplotlib.pyplot as plt

Fs = 1000                   # sampling frequency
t = np.arange(0, 1, 1/Fs)   # 1 second

freqs = [1, 3, 5, 10]       # Hz
A = 1

plt.figure(figsize=(8,10))

for i,f in enumerate(freqs):
    x = A*np.sin(2*np.pi*f*t)
    plt.subplot(len(freqs),1,i+1)
    plt.plot(t,x)
    plt.title(f'Sinusoidal Wave: x(t) = Asin(2*pi*{f}*t), f = {f}, T = {1/f:.3f} s')
    plt.xlabel('Time(s)')
    plt.ylabel('Amplitude')
    plt.grid()

plt.tight_layout()
plt.show()
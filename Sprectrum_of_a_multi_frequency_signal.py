import numpy as np 
import matplotlib.pyplot as plt 

Fs = 100            # sampling frequency (Hz)                   
N = 200             # number of samples (2 s)        
k = np.arange(N) / Fs  

x = (0.25 + 2*np.sin(2*np.pi*5*k) + np.sin(2*np.pi*12.5*k) 
+ 1.5*np.sin(2*np.pi*20*k) + 0.5*np.sin(2*np.pi*35*k)) 

X = np.fft.fft(x) 
f = np.fft.fftfreq(N, 1/Fs) 

# One-sided amplitude spectrum 
half = N // 2 
amp = np.abs(X[:half]) / N 
amp[1:] = 2 * amp[1:] 
f_half = f[:half] 

plt.figure(figsize=(10, 8))

plt.subplot(2, 1, 1) 
plt.plot(k, x) 
plt.title('x(k) = 0.25 + 2sin(2π5k) + sin(2π12.5k) + 1.5sin(2π20k) + 0.5sin(2π35k)') 
plt.xlabel('Time (s)'); plt.ylabel('Amplitude'); plt.grid() 

plt.subplot(2, 1, 2) 
plt.stem(f_half, amp) 
plt.title('Amplitude Spectrum of x(k)') 
plt.xlabel('Frequency (Hz)'); plt.ylabel('Amplitude'); plt.xlim(-1, 50); plt.grid() 

plt.tight_layout() 
plt.show() 
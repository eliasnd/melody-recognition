"""
Trying to create a fourier transform example using Numpy.
Benned Hedegaard - 10/26/2019
"""

import numpy as np
import matplotlib.pyplot as plt

hz = 44100
seconds = 1 # In seconds
timesteps = seconds * hz

two_pi = 2*np.pi
x = np.linspace(0.0, seconds, timesteps)
y = np.sin(10000*two_pi*x) + np.sin(5000*two_pi*x)
#y = np.sin(16000*two_pi*x) - np.sin(8000*two_pi*x) + np.sin(4000*two_pi*x) - np.sin(2000*two_pi*x) + np.sin(1000*two_pi*x) - np.sin(500*two_pi*x) + np.sin(250*two_pi*x) - np.sin(125*two_pi*x)
#y = np.sin(16000*two_pi*x) + np.sin(8000*two_pi*x) + np.sin(4000*two_pi*x) + np.sin(2000*two_pi*x) + np.sin(1000*two_pi*x) + np.sin(500*two_pi*x) + np.sin(250*two_pi*x) + np.sin(125*two_pi*x)

yf = np.fft.fft(y) # Fourier transform y
xf = range(len(yf))

plt.plot(np.fft.fftfreq(len(y)), yf)
plt.show()
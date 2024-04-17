import matplotlib.pyplot as plt
import numpy as np
from utils import *

N = 64
T = 1/128
k = np.arange(N)

# <Task1.1>
f = generateSignal(T, k, 20)
drawPlot(k, f, 'Original Signal', 20)

# <Task1.2>
f = generateSignal(T, k, 20, Fourier=True)
drawPlot(k, np.abs(f), 'Fourier Signal', 20, (2,1,1), (10,10))
f = generateSignal(T, k, 108, Fourier=True)
drawPlot(k, np.abs(f), 'Fourier Signal', 108, (2,1,2))
savePlot()

f = generateSignal(T, k, 10)
drawPlot(k, f, 'Original Signal', 20, (2,2,1), (10,10))
f = generateSignal(T, k, 50)
drawPlot(k, f, 'Original Signal', 50, (2,2,2))
f = generateSignal(T, k, 80)
drawPlot(k, f, 'Original Signal', 80, (2,2,3))
f = generateSignal(T, k, 120)
drawPlot(k, f, 'Original Signal', 120, (2,2,4))
savePlot()

f = generateSignal(T, k, 10, Fourier=True)
drawPlot(k, np.abs(f), 'Fourier Signal', 10, (2,2,1), (10,10))
f = generateSignal(T, k, 50, Fourier=True)
drawPlot(k, np.abs(f), 'Fourier Signal', 50, (2,2,2))
f = generateSignal(T, k, 80, Fourier=True)
drawPlot(k, np.abs(f), 'Fourier Signal', 80, (2,2,3))
f = generateSignal(T, k, 120, Fourier=True)
drawPlot(k, np.abs(f), 'Fourier Signal', 120, (2,2,4))
savePlot()

# <Task1.3>
hertz, magF = sampling(k, T, N, 20)
drawPlot(hertz[:N//2], magF[:N//2], 'Sampling Theorem', 20, (2,1,1), (10,10))

# <Task1.4>
hertz, magF = sampling(k, T, N, 19)
drawPlot(hertz[:N//2], magF[:N//2], 'Sampling Theorem', 19, (2,1,2))
savePlot()

# <Task2.1>
frequencies_1 = [15, 40]
f, m, p = phazeModule(frequencies_1)
drawPlot(f, m, 'Magnitude', frequencies_1, (2,1,1), (10,10))
drawPlot(f, p, 'Phase', frequencies_1, (2,1,2))
savePlot()
frequencies_2 = [25, 50]
f, m, p = phazeModule(frequencies_2)
drawPlot(f, m, 'Magnitude', frequencies_2, (2,2,1), (20,10))
drawPlot(f, p, 'Phase', frequencies_2, (2,2,3))
frequencies_3 = [35, 60]
f, m, p = phazeModule(frequencies_3)
drawPlot(f, m, 'Magnitude', frequencies_3, (2,2,2))
drawPlot(f, p, 'Phase', frequencies_3, (2,2,4))
savePlot()

# <Task3.1>
t, x = frequencySpectre()
drawPlot(t, x, 'Rectangle Signal', subplot=(2,1,1), figureSize=(10,10), stem=True)

# <Task3.2>
t, x = frequencySpectre(Fourier=True)
drawPlot(t, x, 'Fourier Rectangle Signal', subplot=(2,1,2), stem=True)
savePlot()
t, x = frequencySpectre(Fourier=True, w=5)
drawPlot(t, x, 'Fourier Rectangle Signal', 'w=5', (2,1,1), (10,10), True)
t, x = frequencySpectre(Fourier=True, w=0.5)
drawPlot(t, x, 'Fourier Rectangle Signal', 'w=0.5', (2,1,2), None, True)
savePlot()

# <Task3.3>
t, x = frequencySpectre(Spectre=True)
drawPlot(t, x, 'Frequency Spectrum on the Interval [-π, π]', stem=True)

# <Task3.4>
t, x = frequencySpectre(Spectre=True)
plt.plot(t, np.real(x), label='Real Part')
plt.plot(t, np.imag(x), label='Imaginary Part')
plt.title('Real and Imaginary Parts of Frequency Spectrum')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
savePlot()

# <Task4.1>
t, x = tfdWhiteNoise()
drawPlot(t, x, 'White Noise')

# <Task4.2>
t, x = tfdWhiteNoise(filter=True)
drawPlot(t, x, 'White Noise with Filter')

# <Task4.3>
f, m, m1 = tfdWhiteNoise(filter=True, tf=True)
drawPlot(f, m, 'Magnitude Spectrum of White Noise (Input)', subplot=(2,1,1), figureSize=(10,10), stem=True)
drawPlot(f, m1, 'Magnitude Spectrum of White Noise (Output)', subplot=(2,1,2), stem=True)
savePlot()

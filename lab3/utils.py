import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import lfilter


figureCount = 1
xLabel = 'Time Index'
yLabel = 'Amplitude'

def drawPlot(x, y, title, frequency=0, subplot=None, figureSize=None, stem=False):
    if figureSize:
        plt.figure(figsize=figureSize)
    if subplot:
        plt.subplot(subplot[0], subplot[1], subplot[2])
    else:
        plt.clf()    
    if frequency and not stem:  
        plt.plot(x, y, label=f'{frequency} Hz')
    elif not frequency and not stem:
        plt.plot(x, y)    
    elif frequency and stem:
        if type(frequency) == str:
            plt.stem(x, y, label=frequency)  
        else:    
            plt.stem(x, y, label=f'{frequency} Hz')
    elif not frequency and stem:
        plt.stem(x, y)       
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.grid(True)
    plt.legend()
    if subplot:
        plt.tight_layout()
    else:
        savePlot()

def savePlot():
    global figureCount
    plt.savefig(f'output/{figureCount}.png')
    plt.close()
    figureCount += 1

def generateSignal(t, k, frequency, Fourier=False, draw=True):
    f = np.sin(2 * np.pi * frequency * k * t)
    if Fourier:
        f = np.fft.fft(f)
    return f 

def sampling(k, T, N, frequency):
    f = generateSignal(T, k, frequency, Fourier=True, draw=False)
    magF = np.abs(f)
    hertz = k * (1 / (N * T))
    return hertz, magF

def phazeModule(frequencies):
    t = np.linspace(0, 1, 100)
    x = np.sin(2 * np.pi * frequencies[0] * t) + np.sin(2 * np.pi * frequencies[1] * t)
    y = np.fft.fft(x)
    m = np.abs(y)
    p = np.unwrap(np.angle(y))
    f = np.arange(len(y)) * 99 / len(y)
    return f, m, p

def frequencySpectre(Fourier=False, Spectre=False, w=50):
    A = 0.75
    Ts = 0.01
    T = 100
    t = np.arange(0, T, Ts)
    x = A * np.where(np.abs(t) <= w / 2, 1, 0)
    if Fourier:
        df = 1 / T
        Fmax = 1 / Ts
        t = np.arange(0, Fmax, df)
        x = np.fft.fft(x)
    if Spectre:
        df = 1 / T
        Fmax = 1 / Ts
        f = np.arange(0, Fmax, df)
        x = np.fft.fftshift(np.fft.fft(x))
        t = np.arange(-Fmax / 2, Fmax / 2, df)
    return t, x

def tfdWhiteNoise(filter=False, tf=False):
    Ts = 0.01
    T = 50
    t = np.arange(0, T, Ts)
    x1 = np.random.rand(len(t))

    if filter:
        a = np.zeros(3)
        b = np.zeros(1)
        om0 = 2 * np.pi
        dz = 0.05
        A = 1
        oms = om0 * Ts
        a[0] = 1 + 2 * dz * oms + oms**2
        a[1] = -2 * (1 + dz * oms)
        a[2] = 1
        b[0] = A * 2 * dz * oms**2
        y1 = lfilter(b, a, x1)
        if tf:
            df = 1 / T
            Fmax = 1 / Ts
            f = np.arange(-Fmax / 2, Fmax / 2, df)
            Fu1 = np.fft.fftshift(np.fft.fft(x1))
            Fu2 = np.fft.fftshift(np.fft.fft(y1))
            m = np.abs(Fu1)
            m1 = np.abs(Fu2)
            return f, m, m1
        else:    
            return t, y1
    return t, x1

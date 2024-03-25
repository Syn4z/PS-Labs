import matplotlib.pyplot as plt
import numpy as np
import time


figureCount = 1
xLabel = 'Time Index'
yLabel = 'Amplitude'

def drawPlot(x, y, title, subplot=None, figureSize=None):
    if figureSize:
        plt.figure(figsize=figureSize)
    if subplot:
        plt.subplot(subplot[0], subplot[1], subplot[2])
    else:
        plt.clf()    
    plt.stem(x, y)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    if subplot:
        plt.tight_layout()
    else:
        savePlot()

def savePlot():
    global figureCount
    plt.savefig(f'output/{figureCount}.png')
    plt.close()
    figureCount += 1

def generateSequence(a, b, d, c):
    n = np.arange(1, d+1)
    l = np.arange(1, c+1)

    drawPlot(n, a, 'Sequence a', (2, 1, 1))
    drawPlot(l, b, 'Sequence b', (2, 1, 2))
    savePlot()

def convolution(a, b):
    c = np.convolve(a, b)
    m = len(a) + len(b) - 1
    k = np.arange(1, m+1)

    drawPlot(k, c, 'Convolution of a and b')
    return c, m

def fourierTransform(a, b, m):
    AE = np.fft.fft(a, m)
    BE = np.fft.fft(b, m)
    p = AE * BE
    k = np.arange(1, m+1)

    drawPlot(k, np.real(p), 'Result of Fourier Transform')
    return p, k

def inverseFourierTransform(p, k):
    y = np.fft.ifft(p)

    drawPlot(k, y, 'Result of Inverse Fourier Transform')
    return y

def comparedConvolution(c, m, y):
    error = c - y
    k = np.arange(1, m+1)

    drawPlot(k, c, 'Initial Convolution (c)', (3, 1, 1), (10, 10))
    drawPlot(k, y, 'Convolution Obtained by Inverse Fourier Transform (y)', (3, 1, 2))
    drawPlot(k, error, 'Error between Initial Convolution and Obtained Convolution', (3, 1, 3))
    savePlot()

def longerTimeConvolution(n):
    t = np.arange(0, n, 1)
    t1 = np.arange(1, n, 1)
    sq = 2 * np.sign(np.sin(20 * np.pi * t1 + 1))
    cosine = 3 * np.cos(15 * np.pi * t + np.pi/6)
    start_time = time.time()
    c = np.convolve(sq, cosine)

    return time.time() - start_time

def longerTimeFourier(n):
    t = np.arange(0, n, 1)
    t1 = np.arange(1, n, 1)
    sq = 2 * np.sign(np.sin(20 * np.pi * t1 + 1))
    cosine = 3 * np.cos(15 * np.pi * t + np.pi/6)
    m = n * 2
    start_time = time.time()
    AE = np.fft.fft(sq, m)
    BE = np.fft.fft(cosine, m)
    product = AE * BE
    y1 = np.fft.ifft(product)

    return time.time() - start_time

def blockConvolution(a, b, c):
    b1 = b[0:6]
    b2 = b[6:]
    m = np.arange(1, len(c)+1)

    c1 = np.convolve(a, b1)
    c2 = np.convolve(a, b2)

    return b1, b2, c1, c2, m
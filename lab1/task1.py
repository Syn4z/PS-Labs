import numpy as np
import matplotlib.pyplot as plt


def randomNoise(Ts=0.01, plot=True):
    if Ts == 0.01:
        xLabel = 'x$_1$'
        color = 'r'
    elif Ts == 0.001:
        xLabel = 'x$_2$'
        color = 'g'  
    if Ts == 0.01 and not plot:   
        t = np.arange(1, 5, Ts) 
    t = np.arange(0, 5, Ts)
    x = np.random.rand(len(t))

    if plot:
        plt.plot(t, x, label=xLabel, color=color)
        plt.title(f'Example of white noise using plot, Ts={Ts}s')
    else:
        plt.hist(x, bins=20, label=xLabel, color=color)    
        plt.title(f'Example of white noise using hist, Ts={Ts}s')
    plt.grid(True)
    plt.xlabel('time(s)')
    plt.ylabel('function y(t)')
    plt.legend()

def digitalFilter(Ts=0.01):
    om0 = 2 * np.pi
    dz = 0.005
    A = 1
    oms = om0 * Ts

    a = np.zeros(3)
    a[0] = 1 + 2 * dz * oms + oms ** 2
    a[1] = -2 * (1 + dz * oms)
    a[2] = 1

    b = np.zeros(1)
    b[0] = A * 2 * oms ** 2

    t = np.arange(0, 50, Ts)
    x = np.random.rand(len(t))
    y1 = np.convolve(x, b, mode='same') / a[0] - np.convolve(x, a[1:], mode='same') / a[0]

    if Ts == 0.01:
        xLabel = 'x$_1$'
        color = 'r'
    elif Ts == 0.001:
        xLabel = 'x$_2$'
        color = 'g'

    plt.plot(t, y1, label=xLabel, color=color)
    plt.grid(True)
    plt.xlabel('time(s)')
    plt.ylabel('function y(t)')
    plt.title(f'Filtering noise with a second-order filter Ts={Ts}s')
    plt.legend()

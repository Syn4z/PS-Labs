import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter


def randomNoise(Ts=0, signalLimit=0, plot=True):
    t = np.arange(0, signalLimit+Ts, Ts)
    x = np.random.randn(len(t))
    if Ts == 0.01:
        xLabel = 'x$_1$'
        color = 'r'
    elif Ts == 0.001:
        xLabel = 'x$_2$'
        color = 'g'  

    if plot:
        plt.plot(t, x, label=xLabel, color=color)
        plt.title(f'Example of white noise using plot, Ts={Ts}s')
    else:
        plt.hist(x, bins=50, label=xLabel, color=color, edgecolor='black')    
        plt.title(f'Example of white noise using hist, Ts={Ts}s')
    plt.grid(True)
    plt.xlabel('Time(s)')
    plt.ylabel('Function y(t)')
    plt.legend()

def digitalFilter(Ts=0, t=0, x=0):
    om0 = 2 * np.pi
    dz = 0.005
    A = 1
    oms = om0 * Ts
    a = [1 + 2 * dz * oms + oms ** 2, -2 * (1 + dz * oms), 1]
    b = [A * 2 * oms ** 2]
    y1 = lfilter(b, a, x) 

    if Ts == 0.01:
        xLabel = 'x$_1$'
        color = 'r'
    elif Ts == 0.001:
        xLabel = 'x$_2$'
        color = 'g'
    plt.plot(t, y1, label=xLabel, color=color)
    plt.grid(True)
    plt.xlabel('Time(s)')
    plt.ylabel('Function y(t)')
    plt.title(f'Filtering noise with a second-order filter Ts={Ts}s')
    plt.legend()

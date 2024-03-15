import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter, sawtooth

def computeValues(R, S=False):
    if not S:
        m = np.arange(0, R)
        s = 2 * m * (0.9 ** m)
    else:
        m = np.arange(0, R, 0.001)
        s = 2 * sawtooth(3 * np.pi * m + np.pi/6)    
    d = np.random.rand(len(m)) - 0.5
    x = s + d
    
    return m, s, x, d

def plotGenerator(save):
    plt.grid(True)
    plt.xlabel('Time (n)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.savefig(f'{save}')
    plt.show()

def noiseGenerator():  
    m, s, x, d = computeValues(50)    
    plt.plot(m, s, label='s$_1$')
    plt.plot(m, x, label='s$_1$ + d')
    plt.title('The original signal and sum of the original signal and noise')
    save = './plots/2.1-2.4.png'
    plotGenerator(save)
    plt.plot(m, s, label='Original s')
    plt.plot(m, d, label='Noise d')
    plt.title('The original signal and noise')
    save = './plots/2.3.png'
    plotGenerator(save)

def noiseFilter(moreM=False, s2=False):
    if not s2:
        m, s, x, d = computeValues(50)
        M = [3, 5, 10]
    else:
        m, s, x, d = computeValues(1, True)
        M = [20, 50, 100]   
    b = np.ones(M[0]) / M[0]
    y = lfilter(b, 1, x)
    if not moreM:
        b = np.ones(M[0]) / M[0]
        y = lfilter(b, 1, x)
        plt.plot(m, x, 'g--', label='Noisy x')    
        plt.plot(m, y, 'c-', label='Filtered y')
        plt.plot(m, s, 'r-', label='Original s$_1$') 
        plt.title('Original, Noisy, and Filtered Signals')
        if not s2:
            save = './plots/2.5.png'
        else:
            save = './plots/2.7.png'    
    else:    
        fig, axs = plt.subplots(1, len(M), figsize=(15, 5))

        for i, M_val in enumerate(M):
            b = np.ones(M_val) / M_val
            y = lfilter(b, 1, x)
            
            axs[i].plot(m, x, 'g--', label='Noisy x') 
            axs[i].plot(m, y, 'c-', label=f'Filtered y')
            axs[i].plot(m, s, 'r-', label='Original s$_2$')
            axs[i].set_title(f'Original, Noisy, and Filtered Signals with M = {M_val}')
            axs[i].set_xlabel('Time (n)')
            axs[i].set_ylabel('Amplitude')
            axs[i].grid(True)
            axs[i].legend()

        plt.suptitle('The filtered signal with different M values')
        plt.tight_layout()
        if not s2:
            save = './plots/2.6.png'
        else: 
            save = './plots/2.8.png'    
    plotGenerator(save)        

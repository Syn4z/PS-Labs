import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter, sawtooth


def noiseFilter(noise=False, MAF=False, moreM=False, differentS=False):
    R = 50
    m = np.arange(0, R)
    s = 2 * m * (0.9 ** m)
    d = np.random.rand(len(m)) - 0.5
    x = s + d

    # Plotting the filtered signal with different M values 2.6
    if noise and MAF:
        if moreM:
            M = [3, 5, 10]
            for i in M:
                b = np.ones(i) / i
                y = lfilter(b, 1, x)
                plt.plot(m, y, label=f'M = {i}')
            plt.title('The filtered signal with different M values')
            save = './plots/2.6.png'
        # Plotting The original signal, the noisy signal and the filtered signal 2.5
        else:    
            M = 3
            b = np.ones(M) / M
            y = lfilter(b, 1, x)
            plt.plot(m, s, 'r-', label='Original s$_1$') 
            plt.plot(m, x, 'b--', label='Noisy x')    
            plt.plot(m, y, 'g-.', label='Filtered y')   
            plt.title('Original, Noisy, and Filtered Signals')
            save = './plots/2.5.png' 
    # Plotting the original signal with and without noise 2.1-2.4        
    elif noise and not MAF:
        plt.plot(m, s, label='s$_1$')
        plt.plot(m, x, label='s$_1$ + d')
        plt.title('The original signal without and with noise')
        save = './plots/2.1-2.4.png'
    # Plotting the original, noisy, and filtered signals 2.7    
    elif differentS:
        R = 1
        m = np.arange(0, R, 0.001)
        s = 2 * sawtooth(3 * np.pi * m + np.pi/6)
        d = np.random.rand(len(m)) - 0.5
        x = s + d
        if moreM:
            M = [20, 50, 100]
            for i in M:
                b = np.ones(i) / i
                y = lfilter(b, 1, x)
                plt.plot(m, y, label=f'M = {i}')
            plt.title('The filtered signal with different M values')
            save = './plots/2.8.png'
        else:    
            M = 20
            b = np.ones(M) / M
            y = lfilter(b, 1, x)
            plt.plot(m, s, 'r-', label='Original s$_2$') 
            plt.plot(m, x, 'b--', label='Noisy x')    
            plt.plot(m, y, 'g-.', label='Filtered y') 
            plt.title('Original, Noisy, and Filtered Signals')
            save = './plots/2.7.png' 
    plt.grid(True)
    plt.xlabel('Time (n)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.savefig(f'{save}')
    plt.show()

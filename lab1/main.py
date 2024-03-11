import matplotlib.pyplot as plt
from task1 import randomNoise, digitalFilter
from task2 import noiseFilter


Ts1 = 0.01
Ts2 = 0.001

# Plotting the random noise 1.1-1.4
plt.figure(figsize=(10, 8))
plt.subplot(2, 2, 1)
randomNoise(Ts1, True)
plt.subplot(2, 2, 2)
randomNoise(Ts1, False)
plt.subplot(2, 2, 3)
randomNoise(Ts2, True)
plt.subplot(2, 2, 4)
randomNoise(Ts2, False)
plt.tight_layout()
plt.savefig('./plots/1.1-1.4.png')
plt.show()

# Plotting the digital filter 1.5-1.6
plt.figure(figsize=(10, 8))
plt.subplot(1, 2, 1)
digitalFilter(Ts1)
plt.subplot(1, 2, 2)
digitalFilter(Ts2)
plt.tight_layout()
plt.savefig('./plots/1.5-1.6.png')
plt.show()

# Plotting the original signal without and with noise 2.1-2.4
noiseFilter(noise=True, MAF=False)

# Plotting the original signal, the noisy signal and the filtered signal 2.5
noiseFilter(noise=True, MAF=True)

# Plotting the filtered signal for more M 2.6
noiseFilter(noise=True, MAF=True, moreM=True)

# Plotting the original, noisy, and filtered signals for s2 2.7
noiseFilter(noise=False, MAF=False, moreM=False, differentS=True)

# Plotting the filtered signal s2 for more M 2.8
noiseFilter(noise=False, MAF=False, moreM=True, differentS=True)

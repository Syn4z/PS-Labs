import matplotlib.pyplot as plt
import numpy as np
from task1 import randomNoise, digitalFilter
from task2 import noiseFilter, noiseGenerator


signalLimit2 = 75
signalLimit1 = 5
Ts1 = 0.01
Ts2 = 0.001
t1 = np.arange(0, signalLimit2+Ts1, Ts1)
t2 = np.arange(1, signalLimit2+Ts2, Ts2)
x1 = np.random.randn(len(t1))
x2 = np.random.randn(len(t2))

# Plotting the random noise 1.1-1.4
plt.figure(figsize=(10, 8))
plt.subplot(2, 2, 1)
randomNoise(Ts1, signalLimit1, True)
plt.subplot(2, 2, 2)
randomNoise(Ts1, signalLimit1, False)
plt.subplot(2, 2, 3)
randomNoise(Ts2, signalLimit1, True)
plt.subplot(2, 2, 4)
randomNoise(Ts2, signalLimit1, False)
plt.tight_layout()
plt.savefig('./plots/1.1-1.4.png')
plt.show()

# Plotting the digital filter 1.5-1.6
plt.figure(figsize=(10, 8))
plt.subplot(2, 1, 1)
digitalFilter(Ts1, t1, x1)
plt.subplot(2, 1, 2)
digitalFilter(Ts2, t2, x2)
plt.tight_layout()
plt.savefig('./plots/1.5-1.6.png')
plt.show()

# Plotting the noise generator 2.1-2.4
noiseGenerator()
# Plotting the noise filter 2.5
noiseFilter()
# Plotting the noise filter with more M values 2.6
noiseFilter(moreM=True)
# Plotting the noise filter with s2 changed initial signal 2.7
noiseFilter(moreM=False, s2=True)
# Plotting the noise filter with more M values and s2 changed initial signal 2.8
noiseFilter(moreM=True, s2=True)
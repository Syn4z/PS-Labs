import matplotlib.pyplot as plt
from step1 import randomNoise, digitalFilter


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
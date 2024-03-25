import json
import matplotlib.pyplot as plt
import numpy as np
from utils import *

a = np.array([-2, 0, 1, -1, 3])
b = np.array([1, 2, 0, -1])
d = 5
c = 4

# <Task1>
generateSequence(a, b, d, c)

# <Task2>
c, m = convolution(a, b)

# <Task3>
p, k = fourierTransform(a, b, m)

# <Task4>
y = inverseFourierTransform(p, k)

# <Task5>
comparedConvolution(c, m, y)

# <Task6-7>
n = [2**16, 2**18]

results = {}
for i in n:
    results[i] = {
        "Convolution": longerTimeConvolution(i),
        "Fourier": longerTimeFourier(i)
    }

# <Task 8>
a = [1, 4, 2]
b = [1, 2, 3, 4, 5, 4, 3, 3, 2, 2, 1, 1]
c = np.convolve(a, b)
results["Convolution of A and B"] = np.array2string(c, separator=',')

# <Task 9> 
b1, b2, c1, c2, m = blockConvolution(a, b, c)
results["Block Convolution"] = {
    "B1 block": str(b1),
    "B2 block": str(b2),
    "Convolution of A and B1": np.array2string(c1, separator=','),
    "Convolution of A and B2": np.array2string(c2, separator=',')
}

with open('output/results.json', 'w') as f:
    json.dump(results, f, indent=4)

# <Task 10>
c_add = []
c_add.extend(c1[0:6])
c_add.extend(c1[6:8]+c2[0:2])
c_add.extend(c2[2:])

drawPlot(m, c, title='Convolution of A and B')
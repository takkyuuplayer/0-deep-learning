from common import lib as l

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)

l.plt.plot(x, y)
l.plt_show_alt(l.plt)


from common import lib as l

import numpy as np

def relu(x):
    return np.maximum(0, x)

x = np.arange(-5.0, 5.0, 0.1)
y = relu(x)

l.plt.plot(x, y)
l.plt_show_alt(l.plt)



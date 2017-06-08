from common import lib as l

import numpy as np

def step_function(x):
    return np.array(x > 0, dtype=np.int)

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)

l.plt.plot(x, y)
l.plt_show_alt(l.plt)

import sys, os
sys.path.append(os.curdir)

import common.lib as l
import numpy as np

def numerical_diff(f, x):
    h = 1e-4
    return (f(x+h)-(f(x-h))) / (2 * h)

def function_1(x):
    return 0.01 * x ** 2 + 0.1 * x

x = np.arange(0, 20, 0.1)
y = function_1(x)

l.plt.plot(x, y)
l.plt_show_alt(l.plt)

print(numerical_diff(function_1, 5))
print(numerical_diff(function_1, 10))

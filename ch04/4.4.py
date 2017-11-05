import sys, os
sys.path.append(os.curdir)

import numpy as np

from common.gradient import numerical_gradient

def function_2(x):
    return np.sum(x ** 2)

print(numerical_gradient(function_2, np.array([3.0, 4.0])))
print(numerical_gradient(function_2, np.array([0.0, 2.0])))
print(numerical_gradient(function_2, np.array([3.0, 0.0])))

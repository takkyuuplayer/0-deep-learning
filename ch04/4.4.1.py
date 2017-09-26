import sys, os
sys.path.append(os.curdir)

import numpy as np

from common.functions import numerical_gradient

def function_2(x):
    return np.sum(x ** 2)

def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x

    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= lr * grad

    return x

init_x = np.array([-3.0, 4.0])

print(gradient_descent(function_2, np.array([-3.0, 4.0]), lr=0.1, step_num=100))
print(gradient_descent(function_2, np.array([-3.0, 4.0]), lr=10.0, step_num=100))
print(gradient_descent(function_2, np.array([-3.0, 4.0]), lr=1e-10, step_num=100))

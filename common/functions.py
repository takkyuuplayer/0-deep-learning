import numpy as np

def step(x):
    y = x > 0
    return y.astype(np.int)


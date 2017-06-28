import sys, os
sys.path.append(os.curdir)

import numpy as np

from common.functions import softmax

a = np.array([0.3, 2.9, 4.0])
y = softmax(a)
print(y)
print(np.sum(y))

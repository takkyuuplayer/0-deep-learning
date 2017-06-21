import sys, os
sys.path.append(os.curdir)

from datasets.mnist import load_mnist

# 最初の呼び出しは数分待ちます…
(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

print(x_train.shape) # (60000, 784)
print(t_train.shape) # (60000,)
print(x_test.shape) # (10000, 784)
print(t_test.shape) # (10000,)

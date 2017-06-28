import sys, os
sys.path.append(os.curdir)

from datasets.mnist import load_mnist
from common.lib import pil_img_show_alt

import numpy as np

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

img = x_train[0]
label = t_train[0]
print(label) # 5

print(img.shape) # (784,)
img = img.reshape(28, 28) # 形状を元の画像サイズに変形
print(img.shape) # (28, 28)

pil_img_show_alt(img)

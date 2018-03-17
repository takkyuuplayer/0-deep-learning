import sys, os
sys.path.append(os.curdir)

from datasets.mnist import load_mnist
import common.lib as l
from common.util import smooth_curve
import numpy as np
from sgd import SGD
from momentum import Momentum
from adagrad import AdaGrad
from common.multi_layer_net import MultiLayerNet
from common.optimizer import Adam
from common.optimizer import RMSprop

# Load mnist data
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True)

train_size = x_train.shape[0]
batch_size = 128
max_iterations = 2000

# Initialize optimizers
optimizers = {}
optimizers['SGD'] = SGD()
optimizers['Momentum'] = Momentum()
optimizers['AdaGrad'] = AdaGrad()
optimizers['Adam'] = Adam()
optimizers['RMSprop'] = RMSprop()

networks = {}
train_loss = {}
for key in optimizers.keys():
    networks[key] = MultiLayerNet(
            input_size=784, hidden_size_list=[100, 100, 100, 100],
            output_size=10)
    train_loss[key] = []

# Learning
for i in range(max_iterations):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]

    for key in optimizers.keys():
        grads = networks[key].gradient(x_batch, t_batch)
        optimizers[key].update(networks[key].params, grads)

        loss = networks[key].loss(x_batch, t_batch)
        train_loss[key].append(loss)

    if i % 100 == 0:
        print( "===========" + "iteration:" + str(i) + "===========")
        for key in optimizers.keys():
            loss = networks[key].loss(x_batch, t_batch)
            print(key + ":" + str(loss))

# Show a graph
markers = {"SGD": "o", "Momentum": "x", "AdaGrad": "s", "Adam": "D", "RMSprop": "."}
x = np.arange(max_iterations)
for key in optimizers.keys():
    l.plt.plot(x, smooth_curve(train_loss[key]), marker=markers[key], markevery=100, label=key)
l.plt.xlabel("iterations")
l.plt.ylabel("loss")
l.plt.ylim(0, 1)
l.plt.legend()
l.plt_show_alt(l.plt)

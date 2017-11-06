class Sigmoid:
    def __init(self):
        self.out = None

    def forward(self, x):
        out = 1 / ( 1 + np.exp(-x) )
        self.out = out

        return out

    def backward(self, out):
        dx = dout + ( 1.0 - self.out) * self.out

        return dx

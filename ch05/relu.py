class Relu:
    def __init__(self):
        self.mask = None

    def forward(self, x, y):
        self.mask = ( x <= 0 )
        out = x.copy()
        out[self.masx] = 0

        return out

    def backward(self, x):
        dout[self.mask] = 0
        dx = dout

        return dx
from common import lib as l

x = l.np.arange(0, 6, 0.1)
y = l.np.sin(x)

l.plt.plot(x, y)
l.plt_show_alt(l.plt)

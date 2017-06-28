import sys, os
sys.path.append(os.curdir)

import common.lib as l
import numpy as np

from common.functions import step

x = np.arange(-5.0, 5.0, 0.1)
y = step(x)

l.plt.plot(x, y)
l.plt_show_alt(l.plt)

from subprocess import *
from datetime import datetime

import random, math, sys

import numpy as np
import matplotlib as mpl
mpl.use('Agg')
from matplotlib import pyplot as plt
from PIL import Image


def plt_show_alt(plt):
    plt.savefig("/srv/tmp/" + datetime.now().strftime("%Y%m%d-%H%M%S") + ".png")
    plt.clf()

def pil_img_show_alt(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.save("/srv/tmp/" + datetime.now().strftime("%Y%m%d-%H%M%S") + ".png")


# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
sys.path.append(r'/home/emtilt/Documents/GitHub')
from plotdanforth2016sys.io import *
from plotdanforth2016sys.plot import *
import numpy as np
f=importlines('1es1553',zrange=[.39,.4])

plotlinesinzrange('1es1553',linename='OVI 1032',linerestwave=1031.93,zrange=[0.18755,0.18986])
plotlinesinzrange('1es1553',linename='OVI 1038',linerestwave=1037.62,zrange=[0.18755,0.18986])
plotlinesinzrange('1es1553',linename='OVI 1032',linerestwave=1031.93,zrange=0.433+np.array([-0.01,+0.01]))
plotlinesinzrange('1es1553',linename='OVI 1032',linerestwave=1031.93,zrange=0.355+np.array([-0.01,+0.01]))


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
#print(f)
plotlinesinzrange('1es1553','OVI 1032',1031.93,zrange=[0.18755,0.18986])
plotlinesinzrange('1es1553','OVI 1038',1037.62,zrange=[0.18755,0.18986])
#plotlinesinzrange('1es1553','OVI 1032',1031.93,zrange=[0.2163,0.21635])
#plotlinesinzrange('1es1553','OVI 1032',1031.93,zrange=[0.31130,0.31131])
#plotlinesinzrange('1es1553','OVI 1032',1031.93,zrange=[0.37868,0.394996])




#plotlinesinzrange('1es1553','Lya 1215',1215.67,zrange=[0.0346,0.0347])
#plotlinesinzrange('1es1553','Lya 1215',1215.67,zrange=[0.0427,0.0428])
#plotlinesinzrange('1es1553','Lya 1215',1215.67,zrange=[0.0636,0.0637])
#plotlinesinzrange('1es1553','Lya 1215',1215.67,zrange=[0.2186,0.2188])

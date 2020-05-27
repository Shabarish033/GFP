# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 15:39:11 2020

@author: shabarish
"""

import os

img = []
height = []
width = []

from scipy import misc
imagesfolder = os.path.join(os.getcwd(), 'images')
for file in os.listdir(imagesfolder):
    A = os.path.join('images', file)
    image = misc.imread(A)
    h, w = image.shape
    height.append(h)
    width.append(w)

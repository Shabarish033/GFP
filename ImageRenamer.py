# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 12:21:12 2020

@author: shabarish
"""

import os

imagesfolder = os.path.join(os.getcwd(), 'images')
i = 0
for file in os.listdir(imagesfolder):
    i = i+1
    infilename = os.path.join(imagesfolder,file)
    newname = infilename.replace(file, str(str(i).zfill(5) +'.png'))
    output = os.rename(infilename, newname)

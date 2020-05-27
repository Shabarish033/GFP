# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 17:11:44 2020

@author: shabarish
"""

import json 
from xml.etree.ElementTree import Element, SubElement, tostring
import xml.etree.ElementTree as ET
import os
os.mkdir(os.path.join(os.getcwd(),'Emotions', 'annots'))

with open('export-2020-05-24T16_19_50.337Z.json') as json_file:
    data = json.load(json_file)

for i in range(len(data)):
    filename = data[i]['External ID']
    top = Element('annotation')
    FileName = SubElement(top, 'filename')
    FileName.text = str(filename)
    A = data[i]['Label']
    for k in range(len(A.keys())):        
        for j in range(len(data[i]['Label'][list(A.keys())[k]])):    
            xmin = data[i]['Label'][list(A.keys())[k]][j]['geometry'][0]['x']
            xmax = data[i]['Label'][list(A.keys())[k]][j]['geometry'][2]['x']
            ymin = data[i]['Label'][list(A.keys())[k]][j]['geometry'][0]['y']
            ymax = data[i]['Label'][list(A.keys())[k]][j]['geometry'][2]['y']
            bb = SubElement(top, 'bndbox')            
            Xmin = SubElement(bb, 'xmin')
            Xmin.text = str(xmin)
            Ymin = SubElement(bb, 'ymin')
            Ymin.text = str(ymin)
            Xmax = SubElement(bb, 'xmax')
            Xmax.text = str(xmax)
            Ymax = SubElement(bb, 'ymax')
            Ymax.text = str(ymax)
            ClassName = SubElement(bb, 'ClassName')
            ClassName.text = str(list(A.keys())[k])
        XMLFile = str(tostring(top))
        tree = ET.ElementTree(top)
        tree.write(os.path.join(os.getcwd(),'Emotions', 'annots', str(filename[0:-4]) + '.xml'))

#import os
#from xml.etree import ElementTree as ET
## load and parse the file
#filename = os.path.join(os.getcwd(),'Emotions', 'annots', '00001.xml')
#tree = ET.parse(filename)
## get the root of the document
#root = tree.getroot()
## extract each bounding box
#boxes = list()
#ClassName = str(root.find('.//ClassName').text)
#for box in root.findall('.//bndbox'):
#    ClassName = box.find('ClassName')
##    xmin = int(box.find('xmin').text)
##    ymin = int(box.find('ymin').text)
##    xmax = int(box.find('xmax').text)
##    ymax = int(box.find('ymax').text)
##    coors = [xmin, ymin, xmax, ymax, ClassName]
#    boxes.append(ClassName) #Returns a list of the coordinates for all images
#    # extract image dimensions
#width = 320
#height = 243

#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
from os import sep


def recurse(directory, spacing, print=False):
    directory = []

    filesInDir = [files for f in os.listdir(dir) if not files.startwith(',')]

    allF = sorted(files, key=lambda x: x.lower())
    for i, filename in enumerate(allF):

        pathFile = dir + sep + filename

        if (i == len(files) - 1):
        	flaglast = True
            print ('    ' +  '└── '+ filename )
            
        else:
            flaglast = False
            print ('    ' + '├── '+ filename)
       	displayDir(path,'    ',)

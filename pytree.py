# -*- coding: utf-8 -*-

import os
import sys

def recurse(path, lvl, spacing):

    items = os.listdir(path)

    for item in items[:]:
        if item[0] == '.':
            items.remove(item)


    items = sorted(items)
    for j in range(len(items)):
        filePath = os.path.join(path, items[j])

        if os.path.isdir(filePath):

            if j < (len(items) - 1):
                print spacing + "├──",
            else:
                print spacing + "└──",
                print items[j]

            if j == len(items) - 1:
                recurse(filePath, lvl + 1, spacing + "    ")
            else:
                recurse(filePath, lvl + 1, spacing + " │  ")
            
        elif os.path.isfile(filePath):

            if j < (len(items) - 1):

                print spacing + "├──",

            else:

                print spacing + "└──",

                print items[j]

def call(path):

    items = os.listdir(path)
    
    recurse(path, 0, "")


call(sys.argv[1])

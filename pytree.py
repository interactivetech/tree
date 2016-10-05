# -*- coding: utf-8 -*-

import os
import sys


def recurse(path , lvl , spacing):

  items = os.listdir(path)

  for item in items[:]:
    if item[0] == '.':
      items.remove(item)

	#print "LVL",lvl

  items=sorted(items)
  for j in range(len(items)):
    filePath = os.path.join(path , items[j])

    if os.path.isdir(filePath):

      if j < (len(items)-1):
        print spacing,"├──",
      else :
        print spacing, "└──",
        print items[j]

         #recursive add | and space space
         #if last file, only send a space space
        if j == len(items)-1:
          recurse(filePath , lvl+1 , spacing+"    ")
        else:
          recurse(filePath , lvl+1, spacing+" │  ")
      # if j<len(items)-1:
      # 	recurse(filePath,lvl+1,space+" │  ")
      # else:
      # 	recurse(filePath,lvl+1,space+"    ")




         elif os.path.isfile(filePath):

           if j < (len(items)-1):
             print spacing,"├──",
           else :
             print spacing,"└──",
             print items[j]



def call(path):

  items = os.listdir(path)
  #print items
  recurse(path,0,"")


call(sys.argv[1])

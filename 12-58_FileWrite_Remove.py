# -*- coding: utf-8 -*-
"""
Created on Sat May 25 16:19:03 2019

@author: Munire
"""

fileToothpaste=open("Toothpastelist.txt","a")
fileToothpaste.write("Paradontax")
fileToothpaste.write("\n")
fileToothpaste.write("Paradontax")
for x in fileToothpaste:
    print(x)
#fileToothpaste.read()
fileToothpaste.close()

#%% WRİTE STATUS
fileToothpaste=open("Toothpastelist.txt","w")
fileToothpaste.write("Paradontax")
#%% REMOVE

import os
os.remove("Toothpastelist2.txt")

#%% REMOVE 2

import os
if os.path.exists("Toothpastelist2.txt"):
    os.remove("Toothpastelist2.txt")
else:
    print("File is not exist!!!")
#%% REMOVE FOLDER
import os
os.rmdir("Folder")
os.rmdir("x")
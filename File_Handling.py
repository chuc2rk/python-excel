# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 11:21:59 2023

@author: chuc2
"""

import os
import shutil

# Set the current working directory
os.chdir(r"D:\Github\python-excel")

#get working dir
cwd = os.getcwd()

"""
os.path.join(cwd, "01-2014.xlsx"): os.path.join() 
is used to create a path by joining one or more path 
components together.it joins the current 
working directory (cwd) with the file name "01-2014.xlsx" 
to create the full path to the source file.

os.path.join(cwd, "2014", "01-2014.xlsx"): this part joins 
the current working directory with the folder name "2014" 
and the file name "01-2014.xlsx" to create the full path to
 the destination file, including its new location and name.
"""

os.rename(os.path.join(cwd, "01-2014.xlsx"), os.path.join(cwd, "2014", "01-2014.xlsx"))

# Rename the folder
os.rename("2015", "2014")

# Copy files to a subfolder
shutil.copy("03-2014.xlsx", os.path.join(cwd, "2014", "03-2014.xlsx"))

# Copy the entire folder
shutil.copytree("2014", "2014_copy")

# Move files or folders if needed
# shutil.move(source, destination)
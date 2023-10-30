# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 15:19:17 2023

@author: chuc2
"""

import os
import glob

# Change the current working directory
os.chdir(r"D:\Github\python-excel")

# Get the current working directory
cwd = os.getcwd()

# List all the .xlsx files in the current directory
filenames = glob.glob("*.xlsx")

# Iterate through the list of filenames
for file in filenames:
    # Extract the year from the filename
    year = file.split(".")[-2][-4:]

    # Try to convert the year to an integer
    try:
        year = int(year)
    except ValueError:
        print(f"Year '{year}' could not be converted to an integer")
        continue

    # Check if a directory with the year's name exists, and create it if not
    if not os.path.isdir(str(year)):
        os.mkdir(str(year))

    # Move the file to the directory corresponding to the year
    os.rename(file, os.path.join(cwd, str(year), file))

import os
import re

#The code above is written in Python programming language. 
# It uses the os module to rename all files in a directory 
# by replacing spaces with underscores.

# Define the root directory to start the search
root_directory = r'C:\Users\chuc2\OneDrive\WORKs\DII\2.DEO CA - CO MA\1.BAO VE TLDC'

# Loop through each subdirectory and file
for subdir, dirs, files in os.walk(root_directory):
    # Loop through each file in the directory
    for filename in files:
        # Replace any spaces in the filename with underscores
        new_filename = re.sub(r'\s', '_', filename)

        # Rename the file with the new filename
        old_filepath = os.path.join(subdir, filename)
        new_filepath = os.path.join(subdir, new_filename)
        os.rename(old_filepath, new_filepath)
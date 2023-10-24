import os
import re

# Define the path to the directory containing the folders
directory_path = r'C:\Users\chuc2\OneDrive\WORKs\DII\1.HAI VAN'

# Initialize the counter
counter = 1

# Loop through each item in the directory
for item in os.listdir(directory_path):
    # Check if the item is a directory
    if os.path.isdir(os.path.join(directory_path, item)):
        # Convert the folder name to uppercase
        new_foldername = item.upper()
        
        # Add the counter to the folder name
        new_foldername = f"{counter}.{new_foldername}"
        
        # Rename the folder with the new name
        os.rename(os.path.join(directory_path, item), os.path.join(directory_path, new_foldername))
        
        # Increment the counter
        counter += 1
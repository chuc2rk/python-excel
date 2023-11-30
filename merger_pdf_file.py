import os
from PyPDF2 import PdfReader, PdfMerger

# Define the path to the directory containing the PDF files
directory_path = r'C:\Users\chuc2\OneDrive\Desktop\New folder'

# Create a PdfMerger object to merge the PDF files
merger = PdfMerger()

# Loop through each item in the directory
for root, _, files in os.walk(directory_path):
    # Loop through each file in the current directory
    for filename in files:
        # Check if the file is a PDF
        if filename.endswith('.pdf'):
            # Get the path to the PDF file
            filepath = os.path.join(root, filename)
            
            # Read the PDF file
            pdf = PdfReader(filepath)
            
            # Add the PDF file to the merger
            merger.append(pdf)
            
# Write the merged PDF to a file
with open('merged.pdf', 'wb') as output_file:
    merger.write(output_file)

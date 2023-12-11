# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 11:10:46 2023

@author: Quyen
"""

import PyPDF2

# Open the PDF file you want to split
with open("Luong_TTP_Deo_Ca_2021.pdf", "rb") as pdf_file:
    pdf = PyPDF2.PdfFileReader(pdf_file)

    # Get the total number of pages in the PDF
    page_count = pdf.getNumPages()

    # Specify the naming format for the output files
    output_file_prefix = "Luong_TTP_Deo_Ca_2021"

    # Define the number of pages per output file
    pages_per_file = 3

    # Calculate the number of output files needed
    num_output_files = (page_count + pages_per_file - 1) // pages_per_file

    # Iterate through the PDF to split it
    for file_index in range(num_output_files):
        # Calculate the start and end pages for the current output file
        start_page = file_index * pages_per_file
        end_page = min(start_page + pages_per_file - 1, page_count - 1)

        # Create a PDF writer object for the new PDF
        pdf_writer = PyPDF2.PdfFileWriter()

        # Add pages to the new PDF
        for page_number in range(start_page, end_page + 1):
            pdf_writer.addPage(pdf.getPage(page_number))

        # Customize the output file name based on your desired format
        output_pdf = f"{output_file_prefix}_{file_index + 1}.pdf"

        # Save the new PDF as a separate file
        with open(output_pdf, "wb") as output_file:
            pdf_writer.write(output_file)

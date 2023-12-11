import PyPDF2

# Open the PDF file you want to split
with open("Luong_TTP_Deo_Ca_2021.pdf", "rb") as pdf_file:
    pdf = PyPDF2.PdfFileReader(pdf_file)

    # Get the total number of pages in the PDF
    page_count = pdf.getNumPages()

    # Specify the naming format for the output files
    output_file_prefix = "Luong_TTP_Deo_Ca_2021"

    month = 12
    # Iterate through the PDF to split it
    for start_page in range(0, page_count, ):
        end_page = min(start_page + 1, page_count - 1)

        # Create a PDF writer object for the new PDF
        pdf_writer = PyPDF2.PdfFileWriter()

        # Add pages to the new PDF
        for page_number in range(start_page, end_page + 1):
            pdf_writer.addPage(pdf.getPage(page_number))

        
        # Customize the output file name based on your desired format
        output_pdf = f"{output_file_prefix}_{month}.pdf"
        month = month - 1
        # Save the new PDF as a separate file
        with open(output_pdf, "wb") as output_file:
            pdf_writer.write(output_file)

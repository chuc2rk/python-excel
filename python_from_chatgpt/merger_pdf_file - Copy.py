import os
from docx2pdf import convert
from fpdf import FPDF

# Đường dẫn tới thư mục chứa các tệp Word và Excel
input_folder = r"C:\Users\chuc2\OneDrive\Desktop\bb"

# Đường dẫn tới thư mục đầu ra cho các tệp PDF
output_folder = r"C:\Users\chuc2\OneDrive\Desktop"

# Chuyển đổi tệp Word (docx) sang PDF
docx_files = [f for f in os.listdir(input_folder) if f.endswith(".docx")]
for docx_file in docx_files:
    input_path = os.path.join(input_folder, docx_file)
    output_path = os.path.join(output_folder, os.path.splitext(docx_file)[0] + ".pdf")
    convert(input_path, output_path)

# Chuyển đổi tệp Excel (xlsx) sang PDF
xlsx_files = [f for f in os.listdir(input_folder) if f.endswith(".xlsx")]
for xlsx_file in xlsx_files:
    input_path = os.path.join(input_folder, xlsx_file)
    output_path = os.path.join(output_folder, os.path.splitext(xlsx_file)[0] + ".pdf")
    
    # Sử dụng thư viện FPDF để chuyển đổi Excel sang PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Đọc tệp Excel và ghi vào tệp PDF
    with open(input_path, "rb") as excel_file:
        pdf.set_font("Arial", size=12)
        for line in excel_file:
            pdf.multi_cell(0, 10, line.decode("utf-8"))
    
    pdf.output(output_path)

print("Đã chuyển đổi các tệp thành công sang PDF.")

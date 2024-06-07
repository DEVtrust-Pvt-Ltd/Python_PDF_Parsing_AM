import PyPDF2

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        text_content = ""
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text_content += page.extract_text()

    return text_content

# Provide the path to your PDF file
pdf_path = 'sample.pdf'

# Call the function to read the PDF file
pdf_text = read_pdf(pdf_path)

# Print the extracted text content
print(pdf_text)
import PyPDF2
import re

# Open the PDF file in binary mode
with open(r"C:\Users\Ciprian\Downloads\GABUR.pdf", 'rb') as pdf_file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Get the total number of pages in the PDF document
    total_pages = len(pdf_reader.pages)

    # Set the start page to the desired page number (index starts from 0)
    start_page = 2

    # Loop through the pages starting from the desired page
    for page_num in range(start_page, total_pages):
        # Get the page object
        page_obj = pdf_reader.pages[page_num]
        # page_obj = pdf_reader.getPage(page_num)

        # Extract the text from the page
        page_text = page_obj.extract_text()

        print(re.sub(r'([a-zA-Z])(\d)', r'\1 \2', "\n".join(page_text.split('\n')[2:])))

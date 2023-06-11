import pdfquery
import PyPDF2

# Open the PDF file in binary mode
with open(r"C:\Users\Ciprian\Downloads\GABUR.pdf", 'rb') as pdf_file:

    # Create a PyPDF2 PdfFileReader object to read the PDF file
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Set the start page to the desired page number (index starts from 0)
    start_page = 5

    # Get the page object for the desired start page
    start_page_obj = pdf_reader.pages[start_page]

    # Create a PDFQuery object using the start page object
    pdf = pdfquery.PDFQuery(start_page_obj)

    # Load the PDF document into the PDFQuery object
    pdf.load()

    # Use PDFQuery to extract data from the PDF document
    # For example, to get the text of the first line of the first table on the page:
    first_line = pdf.extract('LTTextLineHorizontal:in_bbox("0, 0, 100, 20")')[0].text

    # Print the extracted data
    print(first_line)

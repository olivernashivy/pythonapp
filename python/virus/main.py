import os
import PyPDF2
# read all pdf files in a directory
def read_pdf_files(path):
    # loop through all the files in the directory
    for file in os.listdir(path):
        # get the file name and extension
        file_name, file_extention = os.path.splitext(file)
        # if the file is a pdf file
        if file_extention == ".pdf":
            # read the pdf file
            with open (os.path.join(path, file), "rb") as pdf_file:
                pdf_reader = PyPDF2.PdfFileReader(pdf_file )
                # get the number of pages in the pdf file
                number_of_pages = pdf_reader.getNumPages()
                # loop through all the pages in the pdf file
                for page in range(number_of_pages):
                    # get the page
                    page = pdf_reader.getPage(page)
                    # extract the text from the page
                    page_content = page.extractText()
                    # store the content of the page in a text file
                    with open(os.path.join(path, file_name + ".txt"), "a") as text_file:
                        text_file.write(page_content)

read_pdf_files(os.getcwd())

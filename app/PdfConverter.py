''' Important classes to remember
PDFParser - fetches data from pdf file
PDFDocument - stores data parsed by PDFParser
PDFPageInterpreter - processes page contents from PDFDocument
PDFDevice - translates processed information from PDFPageInterpreter to whatever you need
PDFResourceManager - Stores shared resources such as fonts or images used by both PDFPageInterpreter and PDFDevice
LAParams - A layout analyzer returns a LTPage object for each page in the PDF document
PDFPageAggregator - Extract the decive to page aggregator to get LT object elements
'''

import os
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
# From PDFInterpreter import both PDFResourceManager and PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
# Import this to raise exception whenever text extraction from PDF is not allowed
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.layout import LAParams, LTTextBox, LTTextLine
from pdfminer.converter import PDFPageAggregator

''' This is what we are trying to do:
1) Transfer information from PDF file to PDF document object. This is done using parser
2) Open the PDF file
3) Parse the file using PDFParser object
4) Assign the parsed content to PDFDocument object
5) Now the information in this PDFDocumet object has to be processed. For this we need
   PDFPageInterpreter, PDFDevice and PDFResourceManager
 6) Finally process the file page by page 
'''

class PdfConverter():
    def __init__(self, my_file, log_file, password):
        self.my_file = my_file
        self.log_file = log_file
        self.password = password

    def toTxtfile(self):
        extracted_text = self.convert()
        with open(self.log_file, "w") as my_log:
            my_log.write(extracted_text)

    def convert(self):
        extracted_text = ""

        # Open and read the pdf file in binary mode
        with open(self.my_file, "rb") as fp:
            # Create parser object to parse the pdf content
            parser = PDFParser(fp)

            # Store the parsed content in PDFDocument object
            document = PDFDocument(parser, self.password)

            # Check if document is extractable, if not abort
            if not document.is_extractable:
                raise PDFTextExtractionNotAllowed
                
            # Create PDFResourceManager object that stores shared resources such as fonts or images
            rsrcmgr = PDFResourceManager()

            # set parameters for analysis
            laparams = LAParams()

            # Create a PDFDevice object which translates interpreted information into desired format
            # Device needs to be connected to resource manager to store shared resources
            # device = PDFDevice(rsrcmgr)
            # Extract the decive to page aggregator to get LT object elements
            device = PDFPageAggregator(rsrcmgr, laparams=laparams)

            # Create interpreter object to process page content from PDFDocument
            # Interpreter needs to be connected to resource manager for shared resources and device 
            interpreter = PDFPageInterpreter(rsrcmgr, device)

            # Ok now that we have everything to process a pdf document, lets process it page by page
            for page in PDFPage.create_pages(document):
                # As the interpreter processes the page stored in PDFDocument object
                interpreter.process_page(page)
                # The device renders the layout from interpreter
                layout = device.get_result()
                # Out of the many LT objects within layout, we are interested in LTTextBox and LTTextLine
                for lt_obj in layout:
                    if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
                        extracted_text += lt_obj.get_text()

        return extracted_text
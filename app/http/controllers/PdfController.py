""" A PdfControllerController Module """
from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from app.Pdf import Pdf
from masonite.response import Response
from masonite import Upload
from app.jobs.FileStorage import FileStorage

class PdfController(Controller):
    """Class Docstring Description
    """

    def show(self, filename, response: Response, view: View):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", PdfControllerController
        """
        import os
        pdf_file_dir = os.path.abspath('storage/uploads/pdf_files')
        
        return view.render(pdf_file_dir + "/" + filename)


    def index(self, view: View):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", PdfControllerController
        """
        
        pdfs = Pdf.all()
        
        return view.render("pdfs/index.html", {'pdfs': pdfs})

    def create(self, view: View):
        """Show form to create new resource listings
         ex. Get().route("/create", PdfControllerController
        """
        return view.render("pdfs/create.html")

    def store(self, response: Response, upload: Upload):
        """Create a new resource listing
        ex. Post target to create new Model
            Post().route("/store", PdfControllerController)
        """
        # queue.push(FileStorage(request()))
        file = upload.accept("pdf").store(request().input('pdf_file'), location='storage/uploads/pdf_files')
        # dd(request().input('pdf_file').filename)

        from app.PdfConverter import PdfConverter
        import os
        import hashlib
        txtfilename = hashlib.md5(file.encode('utf-8')).hexdigest()

        pdf_file_dir = os.path.abspath('storage/uploads/pdf_files')

        converter = PdfConverter(pdf_file_dir + "/" + file, pdf_file_dir + "/" + txtfilename + ".txt",  "")
        
        converter.toTxtfile()

        Pdf.create(name= request().input('pdf_file').filename, pdf_path=file, txt_path=txtfilename + ".txt", html_path='')
        
        return response.redirect('/pdfs/index')

    def edit(self):
        """Show form to edit an existing resource listing
        ex. Get().route("/edit", PdfControllerController)
        """

        pass

    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", PdfControllerController)
        """

        pass

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", PdfControllerController)
        """

        pass
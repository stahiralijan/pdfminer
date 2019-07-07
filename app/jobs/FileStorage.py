"""A FileStorage Queue Job."""

from masonite.queues import Queueable
from masonite import Upload

class FileStorage(Queueable):
    """A FileStorage Job."""

    def __init__(self, request):
        """A FileStorage Constructor."""
        # dd(request.input('pdf_file'))
        self.request = request

    def handle(self):
        """Logic to handle the job."""
        self.upload.accept('pdf').store(self.request.input('pdf_file'), location='storage/uploads/pdf_files')
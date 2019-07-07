"""A ConvertPdf Queue Job."""

from masonite.queues import Queueable


class ConvertPdf(Queueable):
    """A ConvertPdf Job."""

    def __init__(self):
        """A ConvertPdf Constructor."""
        pass

    def handle(self):
        """Logic to handle the job."""
        pass

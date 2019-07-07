"""Pdf Model."""

from config.database import Model


class Pdf(Model):
    """Pdf Model."""
    __fillable__ = ['name', 'pdf_path', 'txt_path', 'html_path']
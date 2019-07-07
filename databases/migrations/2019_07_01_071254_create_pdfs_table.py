from orator.migrations import Migration


class CreatePdfsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('pdfs') as table:
            table.increments('id')
            table.string('name')
            table.string('pdf_path')
            table.string('txt_path')
            table.string('html_path')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('pdfs')

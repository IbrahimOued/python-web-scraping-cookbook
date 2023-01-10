""" Implements the IBlobWriter interface to write the blob to a file """

from core.i_blob_writer import IBlobWriter

class FileBlobWriter(IBlobWriter):
    def __init__(self, location="."):
        self._location = location

    def write(self, filename, contents):
        full_filename = self._location + "/" + filename
        print ("Attempting to write {0} bytes to {1}:".format(len(contents), filename))

        with open(full_filename, 'wb') as outfile:
            outfile.write(contents)

        print("The write was successful")

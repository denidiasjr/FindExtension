#
#  CopyExtension v1.0
#  Developed by denidiasjr
#  https://github.com/denidiasjr/copy-extension
#

# Import libraries
import sys
import os
import shutil

class CopyExtension:

    # Constructor
    def __init__(self):
        self._extension = ""
        self._source = ""
        self._destination = ""
        self.srcFiles = []
        self.destFiles = []
        self.recursive = False

    # Setters
    def setSource(self, source):
        if not os.path.exists(source) or not os.path.isdir(source):
            print "ERROR: Source path not exists"
            return
        self._source = source

    def setDestination(self, destination):
        if not os.path.exists(destination):
            os.mkdir(destination)
            return

        # Apply bar in the end of destination
        if not destination.endswith("/"):
            destination += "/"
        self._destination = destination

    def setExtension(self, extension):
        if '.' not in extension:
            extension = '.' + extension
        self._extension = extension

    def setRecursive(self, recursive):
        self.recursive = recursive

    def _printFileSize(self, copyFile, fileSize):
        size = float(fileSize / 1000000000)
        meter = " GB"
        if size < 1:
            meter = " MB"
            size = float(fileSize / 1000000)
            if size < 1:
                meter = " KB"
                size = float(fileSize / 1000)
        print copyFile + ": " + str(size) + meter
        return

    # Map files
    def mapFiles(self):

        # copy[0] represents all the folder inside the one passed by parameter
        # copy[2] represents all files inside the folders
        for copy in os.walk(self._source):

            # If the path is equals the dest path, don't copy it again!
            if self._destination == copy[0]:
                continue

            # If path is trash files, forget it
            # if ".local/share/Trash/files" in copy[0]:
            #    continue

            # Get all files of a path
            for copyFile in copy[2]:

                # Check if copyFile ends with the extension
                if not copyFile.endswith(self._extension):
                    continue

                # Set the absolute path of the src file
                if copy[0].endswith("/"):
                    srcFile = copy[0] + copyFile
                else:
                    srcFile = copy[0] + "/" + copyFile
                
                # Set the absolute path of the dest file
                destFile = self._destination + copyFile

                # Check if have a file with the same name in destination
                if destFile in self.destFiles:

                    # If exists, rename it with the folder name
                    fileInsert = srcFile[:srcFile.rfind('.')]
                    fileInsert += " (" + srcFile.split('/')[-2] + ")"
                    fileInsert += srcFile[srcFile.rfind('.'):]
                    destFile = fileInsert

                # Insert source and destination files in array
                self.srcFiles.insert(0, srcFile)
                self.destFiles.insert(0, destFile)

            
            # If recursive not set, end here
            if not self.recursive:
                return self.srcFiles

        return self.srcFiles

    # Copy files
    def copy(self):
        if not self.srcFiles:
            self.mapFiles()
        for i in range(0, len(self.destFiles)):
            shutil.copy(self.srcFiles[i], self.destFiles[i])
            print self.srcFiles[i] + " copied successfully!"

    # Print all source files 
    def printSourceFiles(self):
        if len(self.srcFiles) == 0:
            print "Source files not set!"
            return

        for file in self.srcFiles:
            self._printFileSize(file, os.path.getsize(file))

    # Print all destination files 
    def printDestinationFiles(self):
        if len(self.destFiles) == 0:
            print "Destination files not set!"
            return

        for file in self.destFiles:
            self._printFileSize(file, os.path.getsize(file))

#copyExtension = CopyExtension('pdf')
#copyExtension.setSource('/home/deni/Downloads')
#copyExtension.setDestination('/home/deni/Desktop/teste/')
#copyExtension.setRecursive(True)
#opyExtension.mapFiles()
#copyExtension.printSourceFiles()
#copyExtension.copy()

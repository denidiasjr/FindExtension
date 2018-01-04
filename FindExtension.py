#
# FindExtension v1.0
# Developed by denidiasjr
#
# Fork it and contribute with this command
# https://github.com/denidiasjr/FindExtension
# 

# Import libraries
import sys
import os
import shutil
import time

class FindExtension:
    
    BACKSLASH = ''

    def __init__(self):
        self._extensions = None
        self._source = None
        if os.name == 'posix':
            self.BACKSLASH = '/'
        else:
            self.BACKSLASH = '\\'

    def help(self):
        print '\nJust a simple way to find files by extension. Thanks for enjoy it!'
        print '\nUsage: findext EXTENSION(S)'
        print 'Mandatory arguments to long options are mandatory for short options too.'
        print '   -a or --all                    search for the extension in the entire disk'
        print '   -s or --source                 set the source directory that you want to find files'
        print '   -help or --help                display this help and exit'
        print 'If you want to contribute with this project, fork it on GitHub :)'
        print 'Repository: https://github.com/denidiasjr/FindExtension\n'

    def getFileSize(self, path):
        
        # Check if path parameter exists
        if not os.path.exists(path):
            print "Ops! File path not exists"
            return "ERROR"
        
        # Get file size in bytes
        size_bytes = os.path.getsize(path)
        len_size = len(str(size_bytes))

        # Check file length and convert it
        if len_size <= 3:
            return str(size_bytes) + " Bytes" 
        if len_size >= 4 and len_size < 7 :
            return '{:.2f}'.format(size_bytes/1000.0) + ' KB'
        elif len_size >= 7 and len_size < 10:
            return '{:.2f}'.format(size_bytes/1000000.0) + ' MB'
        elif len_size >= 10 and len_size < 13:
            return '{:.2f}'.format(size_bytes/1000000000.0) + ' GB'
        elif len_size >= 13:
            return '{:.2f}'.format(size_bytes/1000000000000.0) + ' TB'

        return "ERROR"

    def setExtensions(self, extensions):
        self._extensions = extensions

    def setSource(self, source):
        if not os.path.exists(source) or not os.path.isdir(source):
            print "Ops! Source path not exists :("
            return
        self._source = source

    def search(self):

        # Check if extensions is set
        if self._extensions == None:
            print "Ops! Extensions not set"
            sys.exit()

        # Set current folder as source, if its not set
        if self._source == None:
            self._source = os.getcwd()

        print 'Searching...'

        # files[0] represents all the folder inside the one passed by parameter
        # files[2] represents all files inside the folders
        for files in os.walk(self._source):

            # Iterate files inside folders            
            for fileFolder in files[2]:

                # Iterate extensions
                for extension in self._extensions:

                    # Check if file ends with the extension
                    if not fileFolder.endswith(extension):
                        continue

                    # Get absolute path of file
                    file = files[0] + self.BACKSLASH + fileFolder

                    # Print where the file is
                    print file + " (" + self.getFileSize(file) + ")"
        
        print 'Finish search!'


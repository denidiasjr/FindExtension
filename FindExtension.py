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

class FindExtension:
    
    def __init__(self):
        self._extensions = []
        self._source = None

    def help(self):
        print '\nJust a simple way to find files by extension. Thanks for enjoy it!'
        print '\nUsage: findext EXTENSION(S)'
        print 'Mandatory arguments to long options are mandatory for short options too.'
        print '   -a or --all                    search for the extension in the entire disk'
        print '   -s or --source                 set the source directory that you want to find files'
        print '   -help or --help                display this help and exit'
        print 'If you want to contribute with this project, fork it on GitHub :)'
        print 'Repository: https://github.com/denidiasjr/FindExtension\n'

    def setExtensions(self, extensions):
        self._extensions = extensions

    def setSource(self, source):
        if not os.path.exists(source) or not os.path.isdir(source):
            print "Ops! Source path not exists :("
            return
        self._source = source

    def search(self):
        
        # Set current folder as source, if its not set
        if self._source == None:
            self._source = os.getcwd()

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

                    # Print where the file is
                    print files[0] + "/" + fileFolder

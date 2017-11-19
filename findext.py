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
from FindExtension import FindExtension

# Object of FindExtension class
findExtension = FindExtension()

# Check if command has arguments
if len(sys.argv) < 2:
    findExtension.help()
    sys.exit()

# Check if first argument is a --help 
if '-help' == sys.argv[1] or '--help' == sys.argv[1]:
    findExtension.help()
    sys.exit()

# Get extensions and convert it into list 
extensions = sys.argv[1]

if extensions.find(',') == -1:
    findExtension.setExtensions([extensions])
else:
    findExtension.setExtensions(extensions.split(','))

# If this doesn't have anymore arguments, search for the extensions!
if len(sys.argv) < 3:
    try:
        findExtension.search()
    except KeyboardInterrupt:
        print "\nOps! Operation aborted"
    sys.exit()

# Check for --all argument
if sys.argv[2] == '-a' or sys.argv[2] == '--all':
    if os.name == 'posix':
        findExtension.setSource('/')
    else:
        findExtension.setSource('C:/')
    try:
        findExtension.search()
    except KeyboardInterrupt:
        print "\nOps! Operation aborted"
    sys.exit()

# Check for --search argument
if sys.argv[2] == '-s' or sys.argv[2] == '--source':
    if len(sys.argv) < 4:
        print "Ops! You need to enter with the search folder :)"
        sys.exit()
    folder = sys.argv[3]
    findExtension.setSource(folder)

# Run it
try:
    findExtension.search()
except KeyboardInterrupt:
    print "\nOps! Operation aborted"
#
#  CopyExtension v1.0
#  Developed by denidiasjr
#  https://github.com/denidiasjr/copy-extension
#

# Imports
import sys
import os
from CopyExtension import CopyExtension

# Set null index
indexExtension = -1
indexSource = -1

copyExtension = CopyExtension()

# Capture help message
if '--help' in sys.argv or '-h' in sys.argv:
    copyExtension.help()
    sys.exit()

# Check extension
if '-ext' in sys.argv:
    indexExtension = sys.argv.index('-ext')
else:
    print 'ERROR: Extension not set'
    sys.exit()

# Check source
if '-s' in sys.argv:
    indexSource = sys.argv.index('-s')
else:
    print 'ERROR: Source not set'
    sys.exit()

# Check index extension
if indexExtension == -1 or (indexExtension+1) >= len(sys.argv):
    print 'ERROR: Extension not set'
    sys.exit()
else:
    copyExtension.setExtension(sys.argv[indexExtension])

if indexExtension == -1 or (indexExtension+1) >= len(sys.argv):
    print 'ERROR: Extension not set'
    sys.exit()
else:
    copyExtension.setExtension(sys.argv[indexExtension+1])

# Check index source
if indexSource == -1 or (indexSource+1) >= len(sys.argv):
    print 'ERROR: Source not set'
    sys.exit()
else:
    copyExtension.setSource(sys.argv[indexSource+1])

# Check destination
if '-d' in sys.argv:
    indexDestination = sys.argv.index('-d')
    if (indexDestination+1) < len(sys.argv):
        copyExtension.setDestination(sys.argv[indexDestination+1])
    else:
        print 'ERROR: Destination not set'
        sys.exit()
else:
    copyExtension.setDestination(os.getcwd())

# Check recursive
if '-R' in sys.argv or '--recursive' in sys.argv:
    copyExtension.setRecursive(True)

# Check map
if '-m' in sys.argv or '--map' in sys.argv:
    copyExtension.mapFiles()
    copyExtension.printSourceFiles()
    sys.exit()

copyExtension.copy()
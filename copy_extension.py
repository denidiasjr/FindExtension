# Import libraries
import sys
import os
import shutil

# Check if all arguments was entered
if len(sys.argv) < 3:
    print "ERROR: Enter with all arguments"
    exit()

# Path to copy files
srcPath = sys.argv[1]

# Path to paste files
destPath = sys.argv[2]

# Extensions to search
extension = sys.argv[3]

# Add dot to extension if not set
if '.' not in extension:
    extension = '.' + extension

# Check if the two first arguments exists and are directories
if not os.path.exists(srcPath) and not os.path.isdir(srcPath):
    print "ERROR: Copy path not exists"
    exit()
elif not os.path.exists(destPath) or not os.path.isdir(destPath):
    # Create dest path if not exists
    os.mkdir(destPath)

# Get all the paths files recursively from the directory
srcPaths = os.walk(srcPath)

# Files that will be copied
files = []

# copy[0] represents all the folder inside the one passed by parameter
# copy[2] represents all files inside the folders
for copy in srcPaths:

    # If the path is equals the dest path, don't copy it again!
    if destPath == copy[0]:
        continue

    # If path is trash files, forget it
    if ".local/share/Trash/files" in copy[0]:
        continue

    # Get all files of a path
    for copyFile in copy[2]:

        # Check if copyFile ends with the extension
        if not copyFile.endswith(extension):
            continue

        # Set the absolute path of the src file
        if copy[0].endswith("/"):
            srcFile = copy[0] + copyFile
        else:
            srcFile = copy[0] + "/" + copyFile

        # Set the absolute path of the dest file
        destFile = destPath + "/" + copyFile

        # Check if a file with the same name already exists
        if copyFile in files:

            # If exists, rename it with the folder name
            fileInsert = srcFile[:srcFile.rfind('.')]
            fileInsert += " ("+srcFile.split('/')[-2]+")"
            fileInsert += srcFile[srcFile.rfind('.'):]
            destFile = fileInsert
        else:
            # If no exists, add it to files
            files.insert(0,copyFile)

        # Copy file!
        shutil.copy(srcFile, destFile)
        print srcFile + " copied!"

# Finished :)
print "All "+extension+" copied successfully!"

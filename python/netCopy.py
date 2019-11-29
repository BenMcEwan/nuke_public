# --------------------------------------------------------------
#  netCopy.py
#  Version: 4.0.0
#  Last Updated: July 4th, 2019
#  Author: Ben McEwan
# --------------------------------------------------------------

import nuke
import getpass
import os
import time



# --------------------------------------------------------------
# -----  CLEANUP  ----------------------------------------------
# --------------------------------------------------------------

def remove(path):
    """
    Remove the file or directory
    """
    if os.path.isdir(path):
        try:
            os.rmdir(path)
        except OSError:
            print "Unable to remove folder: %s" % path
    else:
        try:
            if os.path.exists(path):
                os.remove(path)
        except OSError:
            print "Unable to remove file: %s" % path
 


def cleanup(number_of_days, path):
    """
    Removes files from the passed in path that are older than or equal 
    to the number_of_days
    """
    time_in_secs = time.time() - (number_of_days * 24 * 60 * 60)
    for root, dirs, files in os.walk(path, topdown=False):
        for file_ in files:
            full_path = os.path.join(root, file_)
            stat = os.stat(full_path)
 
            if stat.st_mtime <= time_in_secs:
                remove(full_path)
 
        if not os.listdir(root):
            remove(root)
            
            
            

# --------------------------------------------------------------
# -----  NETCOPY  ----------------------------------------------
# --------------------------------------------------------------



def netCopy():
  
    # Define temp directory on the network.
    dir = '/data/share/nuke/netCopy/'
    usr = getpass.getuser()
    fPath = dir + usr

    # Make sure nodes are selected
    if nuke.selectedNodes() == []:
        nuke.message("Please select some nodes")
        return

    else:

        # Check to see if the directory exists, and if not, create it.
        if not os.path.isdir(fPath):
            os.makedirs(fPath)

        # Ask user for a NetCopy name
        txt = nuke.getInput('<font color=red><b>WARNING:</b></font> NetCopies will be removed after 60 days.\n\nNetCopy Name', '')

        # If no NetCopy name is entered, throw an error
        if txt == '':
            nuke.message("Please provide a name for your NetCopy")
            return

        # If the Cancel button is clicked, do nothing.
        if txt == None:
            return

        # Export selected nodes to a nuke script labelled with the user's username.
        fileName = os.path.join(os.path.normpath(fPath), txt)

        # If the NetCopy already exists, ask if it should be overwritten. Otherwise, save the NetCopy.
        if os.path.exists(fileName):
            if nuke.ask('NetCopy already exists, would you like to overwrite?'):
                nuke.nodeCopy(fileName)
                
        else:
            nuke.nodeCopy(fileName)
	
	# Run cleanup
	cleanup(60, '/data/share/nuke/netCopy/')
	
	
	
# --------------------------------------------------------------
# -----  NETPASTE  ---------------------------------------------
# --------------------------------------------------------------


def netPaste():
    # Define temp directory on the network.
    filePath = '/data/share/nuke/netCopy/'
    fileList = nuke.getFileNameList(filePath)

    # Opens dialog box with pulldown choice of username.
    result = nuke.choice("NetPaste", "Pick Username", fileList)

    # If nothing is selected, do nothing.
    if result is None:
        return

    # Otherwise, select username and move to next step
    choice = fileList[result]

    # Define user file directory
    filePath2 = (os.path.join(filePath, choice))
    fileList2 = nuke.getFileNameList(filePath2)

    # Opens dialog box with pulldown choice.
    result2 = nuke.choice("NetPaste", "Pick NetCopy", fileList2)

    # If the Cancel button is pressed, do nothing.
    if result is None or result2 is None:
        return

    # Otherwise, import script of selected username.
    choice2 = fileList2[result2]
    nuke.nodePaste(os.path.join(filePath2, choice2))
    
    # Run cleanup
    cleanup(60, '/data/share/nuke/netCopy/')


# Add to Edit menu
nuke.menu('Nuke').addCommand('Image Engine/NetCopy', 'netCopy.netCopy()', 'ctrl+shift+c')
nuke.menu('Nuke').addCommand('Image Engine/NetPaste', 'netCopy.netPaste()', 'ctrl+shift+v')
nuke.menu('Nuke').addCommand('Image Engine/-', "", "") # Add separator

# --------------------------------------------------------------
#  bm_NodeComment.py
#  Version: 1.0.0
#  Author: Ben McEwan
#
#  Last Modified by: Ben McEwan
#  Last Updated: March 5th, 2019
# --------------------------------------------------------------

# --------------------------------------------------------------
#  USAGE:
#
#  Adds meta+c shortcut to create a node's label, so you don't
#  waste valuable clicks opening a node and switching to the Node
#  label!
# --------------------------------------------------------------

import nuke

def bm_NodeComment():
    selectedNode = nuke.selectedNode()
    oldComment = selectedNode.knob('label').value()
    newComment = nuke.getInput('Node comment', oldComment)

    # If the user has hit 'Cancel', use the previous comment rather than wiping it
    if newComment == None:
        selectedNode.knob('label').setValue(oldComment)
    else:
        selectedNode.knob('label').setValue(newComment)

# Add menu items
nuke.menu('Nuke').addCommand('Edit/Shortcuts/Add Comment to Node', 'bm_NodeComment.bm_NodeComment()', 'meta+c')

# --------------------------------------------------------------
#  bm_ShuffleShortcuts.py
#  Version: 2.0.0
#  Author: Ben McEwan
#
#  Last Modified by: Ben McEwan
#  Last Updated: November 8th, 2021
# --------------------------------------------------------------

# --------------------------------------------------------------
#  USAGE:
#
#  Creates a shuffle node that shuffle RGBA channels into the Green channel.
#  Updated to use Shuffle2...
# --------------------------------------------------------------

import nuke

# Define the function
def createShuffleShortcut(in_red, out_red, in_green, out_green, in_blue, out_blue, in_alpha, out_alpha, rColor, gColor, bColor, label):

    myShuffle = nuke.createNode("Shuffle2")


    # Set 'in' channel to RGBA out.
    myShuffle.knob('mappings').setValue([(in_red, out_red), (in_green, out_green), (in_blue, out_blue), (in_alpha, out_alpha)])

    # Change the node colour to green (we have to convert Nuke's weird hex colour values to RGB to be a bit more human-readable)
    myShuffle['tile_color'].setValue(int('%02x%02x%02x%02x' % (rColor*255,gColor*255,bColor*255,1),16))

    # Add a node label
    myShuffle['label'].setValue(label)



# Define the function
def shuffleRGBchannels():

    # Create a variable for the selected node, before creating any shuffle nodes.
    selectedNode = nuke.selectedNode()

    # Get the X-Position and y-Position of the selected node.
    selectedNode_xPos = selectedNode['xpos'].value()
    selectedNode_yPos = selectedNode['ypos'].value()

    # Create our Red, Green & Blue Shuffle nodes, and assign them to a variable after creation.
    createShuffleShortcut('rgba.red', 'rgba.red', 'rgba.red', 'rgba.green', 'rgba.red', 'rgba.blue', 'rgba.red', 'rgba.alpha', 1, 0, 0, 'Red to All')
    redShuffle = nuke.selectedNode()
    createShuffleShortcut('rgba.green', 'rgba.red', 'rgba.green', 'rgba.green', 'rgba.green', 'rgba.blue', 'rgba.green', 'rgba.alpha', 0, 1, 0, 'Green to All')
    greenShuffle = nuke.selectedNode()
    createShuffleShortcut('rgba.blue', 'rgba.red', 'rgba.blue', 'rgba.green', 'rgba.blue', 'rgba.blue', 'rgba.blue', 'rgba.alpha', 0, 0, 1, 'Blue to All')
    blueShuffle = nuke.selectedNode()

    # Set the input of the Red Shuffle node to the selected node, and Transform the Red Shuffle node down and to the left.
    redShuffle.setInput(0, selectedNode)
    redShuffle['xpos'].setValue(selectedNode_xPos-150)
    redShuffle['ypos'].setValue(selectedNode_yPos+150)

    # Set the input of the Green Shuffle node to the selected node, and Transform the Green Shuffle node down.
    greenShuffle.setInput(0, selectedNode)
    greenShuffle['xpos'].setValue(selectedNode_xPos)
    greenShuffle['ypos'].setValue(selectedNode_yPos+150)

    # Set the input of the Blue Shuffle node to the selected node, and Transform the Blue Shuffle node down and to the right.
    blueShuffle.setInput(0, selectedNode)
    blueShuffle['xpos'].setValue(selectedNode_xPos+150)
    blueShuffle['ypos'].setValue(selectedNode_yPos+150)

    # Create merge node and set the operation to max, connect the inputs to our 3 shuffle nodes, then Transform the Merge node into place.
    mergeNode = nuke.createNode("Merge2")
    mergeNode['operation'].setValue("plus")
    mergeNode.setInput(0, redShuffle)
    mergeNode.setInput(1, greenShuffle)
    mergeNode.setInput(3, blueShuffle)
    mergeNode['xpos'].setValue(selectedNode_xPos)
    mergeNode['ypos'].setValue(selectedNode_yPos+300)



# Add menu items to the Channel nodes menu
nuke.menu('Nodes').addCommand("Channel/Shuffle (Red to All)", "bm_ShuffleShortcuts.createShuffleShortcut('rgba.red', 'rgba.red', 'rgba.red', 'rgba.green', 'rgba.red', 'rgba.blue', 'rgba.red', 'rgba.alpha', 1, 0, 0, 'Red to All')", "meta+r", icon="redShuffle.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Green to All)", "bm_ShuffleShortcuts.createShuffleShortcut('rgba.green', 'rgba.red', 'rgba.green', 'rgba.green', 'rgba.green', 'rgba.blue', 'rgba.green', 'rgba.alpha', 0, 1, 0, 'Green to All')", "meta+g", icon="greenShuffle.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Blue to All)", "bm_ShuffleShortcuts.createShuffleShortcut('rgba.blue', 'rgba.red', 'rgba.blue', 'rgba.green', 'rgba.blue', 'rgba.blue', 'rgba.blue', 'rgba.alpha', 0, 0, 1, 'Blue to All')", "meta+b", icon="blueShuffle.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Alpha to All)", "bm_ShuffleShortcuts.createShuffleShortcut('rgba.alpha', 'rgba.red', 'rgba.alpha', 'rgba.green', 'rgba.alpha', 'rgba.blue', 'rgba.alpha', 'rgba.alpha', 1, 1, 1, 'Alpha to All')", "meta+a", icon="alphaToAll.png", shortcutContext=2)

nuke.menu('Nodes').addCommand("Channel/Shuffle (White Alpha)", "bm_ShuffleShortcuts.createShuffleShortcut('rgba.red', 'rgba.red', 'rgba.green', 'rgba.green', 'rgba.blue', 'rgba.blue', 'white', 'rgba.alpha', 1, 1, 1, 'White Alpha')", "meta+1", icon="alpha1Shuffle.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Black Alpha)", "bm_ShuffleShortcuts.createShuffleShortcut('rgba.red', 'rgba.red', 'rgba.green', 'rgba.green', 'rgba.blue', 'rgba.blue', 'black', 'rgba.alpha', 0, 0, 0, 'Black Alpha')", "meta+`", icon="alpha0Shuffle.png", shortcutContext=2)

nuke.menu('Nodes').addCommand("Channel/Shuffle (Split RGB channels)", "bm_ShuffleShortcuts.shuffleRGBchannels()", "meta+s", icon="ShuffleSplitRGB.png", shortcutContext=2)

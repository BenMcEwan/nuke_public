# --------------------------------------------------------------
#  bm_ShuffleShortcuts.py
#  Version: 1.0.0
#  Author: Ben McEwan
#
#  Last Modified by: Ben McEwan
#  Last Updated: June 3rd, 2019
# --------------------------------------------------------------

# --------------------------------------------------------------
#  USAGE:
#
#  Creates shuffle node shortcuts for shuffling a single channel to all other channels.
# --------------------------------------------------------------

import nuke

# Define the function
def createCustomShuffle(in_channel, out_channel, set_channel, rColor, gColor, bColor):

    # Create a new shuffle node, and assign it to a variable so we can change some things...
    myShuffle = nuke.createNode("Shuffle")

    # Change the input & output channels to what is defined in the in_channel and out_channel arguments.
    myShuffle['in'].setValue(in_channel)
    myShuffle['out'].setValue(out_channel)

    # Change the relevant knobs to shuffle the RGBA channels to the green channel.
    myShuffle['red'].setValue(set_channel)
    myShuffle['green'].setValue(set_channel)
    myShuffle['blue'].setValue(set_channel)
    myShuffle['alpha'].setValue(set_channel)

    # Change the node colour to green (we have to convert Nuke's weird hex colour values to RGB to be a bit more human-readable)
    myShuffle['tile_color'].setValue(int('%02x%02x%02x%02x' % (rColor*255,gColor*255,bColor*255,1),16))

    # Add a node label
    myShuffle['label'].setValue("[value red] > [value out]")



# Define the function
def shuffleRGBchannels():

    # Create a variable for the selected node, before creating any shuffle nodes.
    selectedNode = nuke.selectedNode()

    # Get the X-Position and y-Position of the selected node.
    selectedNode_xPos = selectedNode['xpos'].value()
    selectedNode_yPos = selectedNode['ypos'].value()

    # Create our Red, Green & Blue Shuffle nodes, and assign them to a variable after creation.
    createCustomShuffle('rgba', 'rgba', 'red', 1, 0, 0)
    redShuffle = nuke.selectedNode()
    createCustomShuffle('rgba', 'rgba', 'green', 0, 1, 0)
    greenShuffle = nuke.selectedNode()
    createCustomShuffle('rgba', 'rgba', 'blue', 0, 0, 1)
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
    mergeNode['operation'].setValue("max")
    mergeNode.setInput(0, redShuffle)
    mergeNode.setInput(1, greenShuffle)
    mergeNode.setInput(3, blueShuffle)
    mergeNode['xpos'].setValue(selectedNode_xPos)
    mergeNode['ypos'].setValue(selectedNode_yPos+300)



# Add menu items to the Channel nodes menu
nuke.menu('Nodes').addCommand("Channel/Shuffle (Red to All)", "bm_ShuffleShortcuts.createCustomShuffle('rgba', 'rgba', 'red', 1, 0, 0)", "meta+r", icon="redShuffle.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Green to All)", "bm_ShuffleShortcuts.createCustomShuffle('rgba', 'rgba', 'green', 0, 1, 0)", "meta+g", icon="greenShuffle.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Blue to All)", "bm_ShuffleShortcuts.createCustomShuffle('rgba', 'rgba', 'blue', 0, 0, 1)", "meta+b", icon="blueShuffle.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Alpha to All)", "createCustomShuffle('alpha', 'rgba', 'alpha', 1, 1, 1)", "meta+a", icon="alphaToAll.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Alpha to 0)", "bm_ShuffleShortcuts.createCustomShuffle('alpha', 'alpha', 'black', 0, 0, 0)", "meta+`", icon="alpha0Shuffle.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Alpha to 1)", "bm_ShuffleShortcuts.createCustomShuffle('alpha', 'alpha', 'white', 1, 1, 1)", "meta+1", icon="alpha1Shuffle.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Split RGB channels)", "bm_ShuffleShortcuts.shuffleRGBchannels()", "meta+s", icon="ShuffleSplitRGB.png", shortcutContext=2)

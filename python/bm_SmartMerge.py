# --------------------------------------------------------------
#  bm_SmartMerge.py
#  Version: 1.2.2
#  Author: Ben McEwan
#
#  Last Modified by: Ben McEwan
#  Last Updated: October 22nd, 2019
# --------------------------------------------------------------

# --------------------------------------------------------------
#  USAGE:
#
#  Makes the m hotkey context-dependent:
#  - If a set of 2D nodes & Deeps are selected, create DeepRecolor nodes.
#    If you have multiple sets of Reads & DeepReads selected, SmartMerge will hook the pairs up based on
#    how similarly the filenames of the Reads & DeepReads are named.
#
#  - If only Deep nodes are selected, create a DeepMerge node.
#  - If a ScanlineRender node is selected, intelligently choose whether to Merge or DeepMerge
#    depending on other nodes that are selected.
#
#  - If only 3D nodes are selected, create a Scene node.
#  - If only 2D nodes are selected, or if nothing is selected, create a vanilla Merge node as per usual.
# --------------------------------------------------------------

import nuke


def bm_SmartMerge():

    # ---------------------------------------------------------------
    #  Start by sorting nodes into lists depending on the data type
    # ---------------------------------------------------------------

    # We want nodes of these classes to be flexible...
    wildcard_classes = ['Dot', 'NoOp', 'ScanlineRender']

    # Create lists to hold certain types of nodes.
    twoD_nodes = []
    threeD_nodes = []
    deep_nodes = []
    wildcard_nodes = []

    nodes = nuke.selectedNodes()
    # Reverse the order of the list to match nuke's selection behaviour.
    nodes.reverse()

    # We're going to test the data type based off if a node of a certain type can
    # connect to each of our connected nodes.
    test_3D = nuke.createNode('Scene')
    test_deep = nuke.createNode('DeepReformat')

    # Loop through all selected nodes and test the connections.
    for node in nodes:

        # Sort Wildcard nodes into wildcard_nodes list.
        if node.Class() in wildcard_classes:
            wildcard_nodes.append(node)

        # Sort Deep nodes into deep_nodes list.
        if test_deep.canSetInput(0, node):
            if node not in wildcard_nodes:
                deep_nodes.append(node)

        # Sort 3D nodes into threeD_nodes list.
        if test_3D.canSetInput(0, node):
            if node not in wildcard_nodes:
                threeD_nodes.append(node)

        # Run a check to see if there are any selected nodes that haven't been sorted.
        # For said unsorted nodes, put them into the twoD_nodes list.
        if node not in twoD_nodes and node not in threeD_nodes and node not in deep_nodes and node not in wildcard_nodes:
            twoD_nodes.append(node)
    
    # Delete the nodes we created for the connection test.
    nuke.delete(test_deep)
    nuke.delete(test_3D)

    # Output some handy data into the Script Editor.
    print "\n\n######################################\n  I have sorted the nodes as follows\n######################################"

    print "\n2D NODES ("+str(len(twoD_nodes))+" found):"
    for node in twoD_nodes:
        print "- "+node.name()

    print "\n3D NODES ("+str(len(threeD_nodes))+" found):"
    for node in threeD_nodes:
        print "- "+node.name()

    print "\nDEEP NODES ("+str(len(deep_nodes))+" found):"
    for node in deep_nodes:
        print "- "+node.name()

    print "\nWILDCARD NODES ("+str(len(wildcard_nodes))+" found):"
    for node in wildcard_nodes:
        print "- "+node.name()

    print "\n\n# -------------------------------------\n\n"



    # --------------------------------------------------------------
    #  Now let's do the things!
    # --------------------------------------------------------------

    # If no nodes are selected, we should do the default function and create a merge node.
    if len(nodes) == 0:
        nuke.createNode('Merge2')
        return


    # If only 2D nodes are selected, we will create a regular Merge node.
    if len(twoD_nodes) + len(wildcard_nodes) == len(nodes):

        for i in twoD_nodes:
            i.setSelected(True)
        for j in wildcard_nodes:
            j.setSelected(True)

        # We should sort the selection based off the order nodes are selected, so that things connect up predictably.
        # We can hack this by sorting our selection using the original 'nodes' variable / list, and then
        # de-select & re-select the nodes in the newly-sorted order.
        nodes_sorted = nuke.selectedNodes()
        nodes_sorted.sort(key = lambda x: nodes.index(x))
        for node in nodes_sorted:
        	node.setSelected(False)
        	node.setSelected(True)

    	# Create the Merge node, and output a confirmation of what happened in the Script Editor.
        nuke.createNode('Merge2')       
        print "Merging "+str(len(twoD_nodes))+" 2D nodes with "+str(len(wildcard_nodes))+" wildcard nodes."
        return


    # If only 3D nodes are selected, we will create a Scene node.
    if len(threeD_nodes) + len(wildcard_nodes) == len(nodes):

        for i in threeD_nodes:
            i.setSelected(True)
        for j in wildcard_nodes:
            j.setSelected(True)

        # We should sort the selection based off the order nodes are selected, so that things connect up predictably.
        # We can hack this by sorting our selection using the original 'nodes' variable / list, and then
        # de-select & re-select the nodes in the newly-sorted order.
        nodes_sorted = nuke.selectedNodes()
        nodes_sorted.sort(key = lambda x: nodes.index(x))
        for node in nodes_sorted:
        	node.setSelected(False)
        	node.setSelected(True)

    	# Create the Scene node, and output a confirmation of what happened in the Script Editor.
        nuke.createNode('Scene')
        print "Merging "+str(len(threeD_nodes))+" 3D nodes with "+str(len(wildcard_nodes))+" wildcard nodes."
        return


    # If only Deep nodes are selected, we will create a DeepMerge node.
    if len(deep_nodes) + len(wildcard_nodes) == len(nodes):

        for i in deep_nodes:
            i.setSelected(True)
        for j in wildcard_nodes:
            j.setSelected(True)

        # We should sort the selection based off the order nodes are selected, so that things connect up predictably.
        # We can hack this by sorting our selection using the original 'nodes' variable / list, and then
        # de-select & re-select the nodes in the newly-sorted order.
        nodes_sorted = nuke.selectedNodes()
        nodes_sorted.sort(key = lambda x: nodes.index(x))
        for node in nodes_sorted:
        	node.setSelected(False)
        	node.setSelected(True)

    	# Create the DeepMerge node, and output a confirmation of what happened in the Script Editor.
        nuke.createNode('DeepMerge')
        print "Merging "+str(len(deep_nodes))+" Deep nodes with "+str(len(wildcard_nodes))+" wildcard nodes."
        return



    # Now we can get a little bit fancy. If we have an equal amount of 2D Nodes & Deep Nodes selected, let's create a DeepRecolor.
    if len(deep_nodes) == len(twoD_nodes) and len(threeD_nodes) == 0:

        # We have to sort the list alphabetically, for easier matching when there are pairs of Beauty renders and DeepReads.
        # We're splitting the name before the version number, because in some instances, the minor name difference is enough to
        # cause the beauty and the deeps to be sorted differently...

        # In this case, both lists will be sorted to be in the same order using the same index number.
        # But we also retain the flexibility to DeepRecolor any 2D data stream with any Deep data stream.
        twoD_nodes.sort(key = lambda x: x.name().split('_v')[0])
        deep_nodes.sort(key = lambda x: x.name().split('_v')[0])

        # Now we're going to create a bunch of DeepRecolor nodes, and connect them up based off the
        # previously-sorted Read & Deep lists. We also want to force the position of the new DeepRecolor node
        # to be in a sensible spot in the Node Graph.
        for y in range(0, len(deep_nodes)):

            dr = nuke.createNode('DeepRecolor')

            dr.setInput(0, deep_nodes[y])
            dr.setInput(1, twoD_nodes[y])

            xPos, yPos = twoD_nodes[y].knob('xpos').value(), twoD_nodes[y].knob('ypos').value()
            dr.knob('xpos').setValue(xPos)
            dr.knob('ypos').setValue(yPos+95)

		# Of course, we will output a confirmation of what happened in the Script Editor.
        print str(len(deep_nodes))+" beautys & deeps matched and paired"
        return



    # Lastly, if there are too many random nodes selected, throw an error message.
    else:
        nuke.message("You have "+str(len(twoD_nodes))+" 2D nodes, "+str(len(threeD_nodes))+" 3D nodes, "+str(len(deep_nodes))+" Deep nodes and "+str(len(wildcard_nodes))+" Wildcard nodes selected, so I'm not sure what to do...\n\nPlease select similar types of nodes to Merge them correctly.")
        return




# Add to the edit menu, and overwrite the "m" hotkey.
nuke.menu('Nuke').addCommand('Edit/Smart Merge', 'bm_SmartMerge.bm_SmartMerge()', 'm')

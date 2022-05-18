# --------------------------------------------------------------
#  bm_OperationSwitcher.py
#  Version: 1.0.4
#  Author: Ben McEwan
#
#  Last Modified by: Ben McEwan
#  Last Updated: May 17th, 2022
# --------------------------------------------------------------

# --------------------------------------------------------------
#  USAGE:
#
#  Ctrl+Alt+S toggles between over/under, mask/stencil, plus/from, etc.
# --------------------------------------------------------------

import nuke

# Define function
def bm_OperationSwitcher():

	# Create variable for easier access to nuke.selectedNode()
    try:
        node = nuke.selectedNode()

    # If no node is selected, create an Invert node.
    except:
        nuke.createNode('Invert')
        return

    # Create Dictionary with keys & values being the opposite operations
    merge_ops = {'over':'under', 'mask':'stencil', 'plus':'from', 'multiply':'divide', 'max':'min', 'conjoint-over':'disjoint-over'}

    # Check if the selected node is a Merge node
    if node.Class() == "Merge2":

        # Set a variable that holds the current value of the 'operation' knob
        current_op = node['operation'].value()

        # Search for the current value of the 'operation' knob in our dictionary's keys
        if current_op in merge_ops.keys():

            # If a match is found, (e.g. the current operation is 'mask', and there is a key in our dictionary called 'mask'),
            # get the value of the matching key from our dictionary ('stencil', in this example), and set the operation knob of
            # our selected node to said value.
            node['operation'].setValue(merge_ops[node['operation'].value()])

            # However if no match is found, do the same thing but search the keys in the dictionary & set the matching value instead.
        elif current_op in merge_ops.values():
            # Works in Python 2
            #node['operation'].setValue(merge_ops.keys()[merge_ops.values().index(current_op)])

            # Works in Python 3 only + Python 2.
            node['operation'].setValue(list(merge_ops.keys())[list(merge_ops.values()).index(current_op)])

    # If a node is selected that isn't a Merge node, create an Invert node.
    else:
        nuke.createNode('Invert')
        return


# Add menu item
nuke.menu('Nuke').addCommand('Edit/Shortcuts/Toggle Operation to Opposite', 'bm_OperationSwitcher.bm_OperationSwitcher()', 'ctrl+alt+s')

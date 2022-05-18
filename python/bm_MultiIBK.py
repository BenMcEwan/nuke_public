# --------------------------------------------------------------
#  bm_MultiIBK.py
#  Version: 0.5.1
#  Author: Ben McEwan
#
#  Last Modified by: Ben McEwan
#  Last Updated: June 24th, 2019
#
# --------------------------------------------------------------

# --------------------------------------------------------------
#  USAGE:
#
#  Creates the usual IBK setup with 6 expression-linked IBKColour duplicates
# --------------------------------------------------------------

import nuke

# Define function.
def bm_MultiIBK():

    # If a node is selected, and nodes are created, for some reason the manual setting
    # of xpos and ypos screws up. So we have to check if a node is selected, create a dot,
    # then manually set it's xpos and ypos to be something sensible...
    try:
        n = nuke.selectedNode()
        n.setSelected(False)

        dot = nuke.createNode('Dot')
        dot.knob('xpos').setValue(n.knob('xpos').value()+34)
        dot.knob('ypos').setValue(n.knob('ypos').value()+100)
        dot.setInput(0, n)

    # But if no node is selected, then we just create the dot.
    except:
        dot = nuke.createNode('Dot')

    # Create the first IBKColour and position it down and to the right in the Node Graph.
    colour = nuke.createNode('IBKColourV3', 'screen_type green')
    colour.knob('xpos').setValue(dot.knob('xpos').value()+100)
    colour.knob('ypos').setValue(dot.knob('ypos').value()+100)

    # Create 6 more IBKColour nodes with expression links which set all the knobs' values to
    # the same thing as their input node's knobs.
    # Positioning in the node graph is automatic as each copy of the node will be selected upon creation.
    for i in range(0,6):

        colour_linked = nuke.createNode('IBKColourV3', 'screen_type green', inpanel = False)
        colour_linked.knob('Size').setExpression('input.Size')
        colour_linked.knob('off').setExpression('input.off')
        colour_linked.knob('mult').setExpression('input.mult')
        colour_linked.knob('erode').setExpression('input.erode')

    # Create the IBKGizmo node, set it's position in the Node Graph, then set the 'fg' and 'c' inputs to
    # the Dot and the last IBKColour node respectively.
    gizmo = nuke.createNode('IBKGizmoV3', 'st C-green')
    gizmo.knob('xpos').setValue(dot.knob('xpos').value()-34)
    gizmo.knob('ypos').setValue(dot.knob('ypos').value()+325)
    gizmo.setInput(0, dot)
    gizmo.setInput(1, colour_linked)


# Add a menu item
nuke.menu('Nodes').addCommand('Keyer/IBK Setup', 'bm_MultiIBK.bm_MultiIBK()', icon="IBKGizmo.png")

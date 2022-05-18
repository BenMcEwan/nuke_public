# --------------------------------------------------------------
#  bm_PulldownKnobCycler.py
#  Version: 1.0.0
#  Author: Ben McEwan
#
#  Last Modified by: Ben McEwan
#  Last Updated: November 9th, 2021
# --------------------------------------------------------------

"""
Cycle the primary pulldown knob on common nodes.
"""

import nuke


def cyclePulldown(direction):

    # We'll always operate on the selected node.
    node = nuke.selectedNode()

    # Check if the node in question has a 'channels' knob. If yes, we'll run specific cycler code.
    if node.knob('channels'):
        knob = node.knob('channels')

        # Query all the layers (channels) in the nuke script, and if there's a match with "knob",
        # we'll cycle through them...
        if knob.value() in nuke.layers():
            current_index = nuke.layers().index(knob.value())
            try:
                knob.setValue(nuke.layers()[current_index+direction])

            # If anything goes wrong, we'll force 'rgba' to be the value.
            except:
                knob.setValue('rgba')

        # If the value is none, it can cause the above code to fail for some nodes. This hardcodes
        # a switch to 'rgba' in these instances...
        elif knob.value() == 'none':
            knob.setValue('rgba')



    # The operation knob is the other common one. Let's check for that and run some specific cycler code.
    elif node.knob('operation'):
        knob = node.knob('operation')
        # If we get to the end of the list, and want to go "next", we have to force it to go back to the top of the list...
        if knob.value() == "xor" and direction == 1:
            knob.setValue("atop")
        # Similarly, if we get to the start of the list, and want to go "previous", we have to force it to go back to the bottom of the list...
        elif knob.value() == "atop" and direction == -1:
            knob.setValue("xor")
        else:
        # Otherwise, cycle as normal.
            knob.setValue(int(node.knob('operation').getValue()+direction))



    # If 'channels' or 'operation' knobs aren't found, we should print a message and do nothing.
    else:
        print("channels or operation knobs not found, so I have nothing to cycle")
        return



# Add menu items + hotkeys.
nuke.menu('Nuke').addCommand('Edit/Shortcuts/Cycle Pulldown Knob on Selected Node (forward)', 'bm_PulldownKnobCycler.cyclePulldown(-1)', 'PgUp', shortcutContext=2)
nuke.menu('Nuke').addCommand('Edit/Shortcuts/Cycle Pulldown Knob on Selected Node (backward)', 'bm_PulldownKnobCycler.cyclePulldown(1)', 'PgDown', shortcutContext=2)

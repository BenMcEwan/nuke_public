# --------------------------------------------------------------
#  bm_Smoothie.py
#  Version: 1.0.1
#  Last Updated: July 20th, 2020
# --------------------------------------------------------------

# --------------------------------------------------------------
#  USAGE:
#
# - Easily smooth curves in Nuke's curve editor.
#
# --------------------------------------------------------------

import nuke

# Define the function.
def bm_Smoothie(direction):

    # Set up a variable for easy use.
    node = nuke.thisNode()

    # Create a list to hold selected keyframes.
    selected_keys = []
    
    # Find animated keyframes on the active node...
    for knob in node.knobs():
        if node.knob(knob).isAnimated():
            
            # ... then, if they're selected, add them to our selected_keys list.
            for i in range(0, len(node.knob(knob).animation(0).keys())):
                if node.knob(knob).animation(0).keys()[i].selected == True:
                    selected_keys.append(node.knob(knob).animation(0).keys()[i])



    # If no curves / keyframes are selected, throw an error message.
    if selected_keys == [] or nuke.animations() == ():
        nuke.message("Please select at least one keyframe in the curve editor to smooth.")
        return



    # Loop through all selected keys and do the thing!
    for keyframe in selected_keys:

        # Check if keyframe interpolation is linear, and if yes, set it to smooth.
        if keyframe.interpolation == nuke.LINEAR:
            keyframe.interpolation = nuke.SMOOTH

        # Easy-ease in / out functionality
        if direction == "in":
            keyframe.lslope = 0

        elif direction == "out":
            keyframe.rslope = 0
            
        # Set some boundaries. Values over 3 usually make a curve go nuts, so if that happens we reset to 1.
        if keyframe.la < 1 or keyframe.la > 3:
            keyframe.la = 1
            keyframe.ra = 1

        # Otherwise we'll get the current value, and increment by 0.5.
        else:
            keyframe.la = keyframe.la+0.5
            keyframe.ra = keyframe.ra+0.5



        # Hack to force-update the viewer.
        if node.knob('fringe'):

            if node.knob('fringe').value() == 0:
                node.knob('fringe').setValue(1)
                node.knob('fringe').setValue(0)
            else:        
                node.knob('fringe').setValue(0)
                node.knob('fringe').setValue(1)
        else:
            return



# Add our functions to the Curve Editor's right-click menu and assign hotkeys.
nuke.menu('Animation').addCommand("Interpolation/Easy-Ease/Smooth Selected Keyframes", 'bm_Smoothie.bm_Smoothie(None)', "f9")
nuke.menu('Animation').addCommand("Interpolation/Easy-Ease/Easy-Ease In", 'bm_Smoothie.bm_Smoothie("in")', "shift+f9")
nuke.menu('Animation').addCommand("Interpolation/Easy-Ease/Easy-Ease Out", 'bm_Smoothie.bm_Smoothie("out")', "ctrl+shift+f9")

# --------------------------------------------------------------
#  bm_QuickKeys.py
#  Version: 2.0.1
#  Author: Ben McEwan
#
#  Last Modified by: Ben McEwan
#  Last Updated: November 18th, 2019
# --------------------------------------------------------------

# --------------------------------------------------------------
#  USAGE:
#
#  Adds an easy way to set on/off keyframes on mix knobs & switch nodes
# --------------------------------------------------------------

import nuke
import nukescripts

def bm_QuickKeys(type):

    # Set some initial variables for later use.
    node = nuke.selectedNode()
    frame = nuke.frame()

    # Find the correct knob based on the node's class. If it's not specified, presume the user
    # wants to use the shortcut on the mix knob.
    dict = {'Switch':'which','Dissolve':'which','Roto':'opacity','RotoPaint':'opacity'}    

    if node.Class() in dict.keys():
        knob = node.knob(dict[node.Class()])
    else:
        knob = node.knob('mix')

    # If the mix knob has a non-zero value we should use it, but if it's zero things can break so we'll use 1 instead.
    if knob.value() != 0:
    	knob_value = knob.value()
    else:
    	knob_value = 1


    # Now, let's make things work!

    # "on" is the function's argument. We're using it as an easy way to set shortcuts,
    # But there is no error-checking because users won't be seeing / setting them.

    # "on" sets a keyframe with the current value on the current frame, and a keyframe with a value of 0 on the previous frame.
    if type == "on":

        # Prime node for animation
        knob.setAnimated(0)
        knob_anim = knob.animations()[0]

        knob_anim.setKey(frame, knob_value)
        knob_anim.setKey(frame-1, 0)
        return


    # "off" sets a keyframe with the current value on the current frame, and a keyframe with a value of 0 on the next frame. 
    elif type == "off":

        # Prime node for animation
        knob.setAnimated(0)
        knob_anim = knob.animations()[0]

        knob_anim.setKey(frame, knob_value)
        knob_anim.setKey(frame+1, 0)
        return


    # "offonoff" sets a keyframe with the current value on the current frame, and a keyframe with a value of 0 on both the next and the previous frames.
    elif type == "offonoff":

        # Prime node for animation
        knob.setAnimated(0)
        knob_anim = knob.animations()[0]

        knob_anim.setKey(frame-1, 0)
        knob_anim.setKey(frame, knob_value)
        knob_anim.setKey(frame+1, 0)
        return


    # "onoffon" sets a keyframe with a value of 0 on the current frame, and a keyframe with the current value on both the next and the previous frames.
    elif type == "onoffon":

        # Prime node for animation
        knob.setAnimated(0)
        knob_anim = knob.animations()[0]

        knob_anim.setKey(frame-1, knob_value)
        knob_anim.setKey(frame, 0)
        knob_anim.setKey(frame+1, knob_value)
        return



    # "custom" is a little more involved, as it opens a panel. You can set whatever values you want, including a "fade" option to make transitions
    # not-so-instant.
    elif type == "custom":        

        # Create the panel
        panel = nukescripts.PythonPanel("Quick Keys")

        # Add the knobs, position them on the pop-up window and set default values
        on_frame_input = nuke.Int_Knob('on_frame_input', 'First Frame')
        on_frame_input.setValue(frame)
        panel.addKnob(on_frame_input)

        on_frame_value = nuke.Double_Knob('on_frame_value', '   Set value')
        on_frame_value.setValue(knob_value)
        on_frame_value.clearFlag(nuke.STARTLINE)
        panel.addKnob(on_frame_value)

        on_chk = nuke.Boolean_Knob('on_chk', 'enable', True)
        panel.addKnob(on_chk)

        off_frame_input = nuke.Int_Knob('off_frame_input', 'Last Frame')
        off_frame_input.setValue(frame+10)
        panel.addKnob(off_frame_input)

        off_frame_value = nuke.Double_Knob('off_frame_value', '   Set value')
        off_frame_value.setValue(knob_value)
        off_frame_value.clearFlag(nuke.STARTLINE)
        panel.addKnob(off_frame_value)

        off_chk = nuke.Boolean_Knob('off_chk', 'enable', True)
        panel.addKnob(off_chk)

        fade_input = nuke.Int_Knob('fade_frame_input', 'Fade Duration', frame)
        panel.addKnob(fade_input)

        fade_chk = nuke.Boolean_Knob('fade_chk', 'enable', True)
        panel.addKnob(fade_chk)


        # If the window successfully opens and the ok button is pressed, do the things.
        if panel.showModalDialog() == True:

            # Prime node for animation
            knob.setAnimated(0)
            knob_anim = knob.animations()[0]

            # If there's no fading happening, we need to force an offset of 1 frame so keyframes don't overwrite each other.
            if fade_chk.value() == False or fade_input.value() == 0:
                fade_input.setValue(1)

            if on_chk.value() == True:                
                knob_anim.setKey(on_frame_input.value(), on_frame_value.value())
                knob_anim.setKey(on_frame_input.value()-(fade_input.value()), 0)

            if off_chk.value() == True:
                knob_anim.setKey(off_frame_input.value(), off_frame_value.value())
                knob_anim.setKey(off_frame_input.value()+(fade_input.value()), 0)


        # Otherwise, if the cancel button is pressed, don't do anything...
        else:
            return



# Add to Edit menu, with all the shortcuts!
nuke.menu('Nuke').addCommand('Edit/Shortcuts/Quick Keys/On', 'bm_QuickKeys.bm_QuickKeys("on")', "meta+,")
nuke.menu('Nuke').addCommand('Edit/Shortcuts/Quick Keys/Off', 'bm_QuickKeys.bm_QuickKeys("off")', "meta+.")
nuke.menu('Nuke').addCommand('Edit/Shortcuts/Quick Keys/Off On Off', 'bm_QuickKeys.bm_QuickKeys("offonoff")', "ctrl+meta+,")
nuke.menu('Nuke').addCommand('Edit/Shortcuts/Quick Keys/On Off On', 'bm_QuickKeys.bm_QuickKeys("onoffon")', "ctrl+meta+.")
nuke.menu('Nuke').addCommand('Edit/Shortcuts/Quick Keys/Range', 'bm_QuickKeys.bm_QuickKeys("custom")', "meta+/")

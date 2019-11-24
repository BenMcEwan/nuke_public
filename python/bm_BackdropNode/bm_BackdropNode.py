# --------------------------------------------------------------
#  bm_BackdropNode.py
#  Version: 1.0.0
#  Last Updated: June 17th, 2019
# --------------------------------------------------------------

# --------------------------------------------------------------
#  USAGE:
#
# - Better version of the default Backdrop Node in Nuke.
# - Added features include: colour presets, buttons to change the size.
#
# --------------------------------------------------------------

import nuke
import bm_NukeColourConverter
import random

def bm_BackdropNode(label, sizeBuffer, colorR, colorG, colorB, text_size, zOrder):
    # Create list of nodes to Backdrop
    nodeList = []

    for i in nuke.selectedNodes():
        nodeList.append(i)

    # Find horizontal bounds of selection
    def sortXpos(node):
        return node.knob('xpos').value()

    nodeList.sort(key=sortXpos)

    min_posX = nodeList[0].knob('xpos').value()
    max_posX = nodeList[-1].knob('xpos').value()
    width = max_posX - min_posX

    # Find vertical bounds of selection
    def sortYpos(node):
        return node.knob('ypos').value()

    nodeList.sort(key=sortYpos)

    min_posY = nodeList[0].knob('ypos').value()
    max_posY = nodeList[-1].knob('ypos').value()
    height = max_posY - min_posY

    # Create Backdrop
    backdrop = nuke.createNode('BackdropNode')

    # Set position.
    # Width +80 and height +19 are to accound for the sizes of nodes.
    # SizeBuffer is extra on height to make room for the label.
    backdrop.knob('xpos').setValue(min_posX - sizeBuffer)
    backdrop.knob('ypos').setValue(min_posY - (sizeBuffer * 2))
    backdrop.knob('bdwidth').setValue(width + 80 + (sizeBuffer * 2))
    backdrop.knob('bdheight').setValue(height + 19 + (sizeBuffer * 3))

    # Add Knobs
    backdrop.addKnob(nuke.Multiline_Eval_String_Knob('new_label', "Label"))
    backdrop.addKnob(nuke.Int_Knob('new_z_order', "Z Order"))
    backdrop.addKnob(nuke.Int_Knob('new_note_font_size', "Text Size"))

    # Set Backdrop knobs
    backdrop.knob('new_note_font_size').setValue(int(text_size))
    backdrop.knob('new_label').setValue(label)
    backdrop.knob('new_note_font_size').setValue(text_size)
    backdrop.knob('tile_color').setValue(bm_NukeColourConverter.hex_colour_to_rgb(colorR, colorG, colorB))
    backdrop.knob('note_font_color').setValue(bm_NukeColourConverter.hex_colour_to_rgb(colorR + 0.2, colorG + 0.2, colorB + 0.2))
    backdrop.knob('new_z_order').setValue(zOrder)

    # Add size adjust buttons
    backdrop.addKnob(nuke.Int_Knob('size_int', "Scale Amount"))
    backdrop.knob('size_int').setValue(sizeBuffer)

    backdrop.addKnob(nuke.PyScript_Knob('size_up', "+",
                                        'nuke.thisNode().knob("xpos").setValue(nuke.thisNode().knob("xpos").value()-nuke.thisNode().knob("size_int").value())\nnuke.thisNode().knob("ypos").setValue(nuke.thisNode().knob("ypos").value()-nuke.thisNode().knob("size_int").value())\nnuke.thisNode().knob("bdwidth").setValue(nuke.thisNode().knob("bdwidth").value()+nuke.thisNode().knob("size_int").value()*2)\nnuke.thisNode().knob("bdheight").setValue(nuke.thisNode().knob("bdheight").value()+nuke.thisNode().knob("size_int").value()*2)'))
    backdrop.addKnob(nuke.PyScript_Knob('size_up', "-",
                                        'nuke.thisNode().knob("xpos").setValue(nuke.thisNode().knob("xpos").value()+nuke.thisNode().knob("size_int").value())\nnuke.thisNode().knob("ypos").setValue(nuke.thisNode().knob("ypos").value()+nuke.thisNode().knob("size_int").value())\nnuke.thisNode().knob("bdwidth").setValue(nuke.thisNode().knob("bdwidth").value()-nuke.thisNode().knob("size_int").value()*2)\nnuke.thisNode().knob("bdheight").setValue(nuke.thisNode().knob("bdheight").value()-nuke.thisNode().knob("size_int").value()*2)'))

    backdrop.addKnob(nuke.Double_Knob('brightness_mult', "Preset Brightness"))
    backdrop.knob('brightness_mult').setValue(1)

    # Link original knobs to the new ones with callbacks
    backdrop.knob('knobChanged').setValue("nuke.thisNode().knob('label').setValue(nuke.thisNode().knob('new_label').value())\nnuke.thisNode().knob('note_font_size').setValue(nuke.thisNode().knob('new_note_font_size').value())\nnuke.thisNode().knob('z_order').setValue(nuke.thisNode().knob('new_z_order').value())")

    # Hide original knobs
    backdrop.knob('label').setFlag(nuke.INVISIBLE)
    backdrop.knob('note_font').setFlag(nuke.INVISIBLE)
    backdrop.knob('note_font_size').setFlag(nuke.INVISIBLE)
    backdrop.knob('note_font_color').setFlag(nuke.INVISIBLE)
    backdrop.knob('z_order').setFlag(nuke.INVISIBLE)
    backdrop.knob('bookmark').setFlag(nuke.INVISIBLE)





    # Divider Line
    backdrop.addKnob(nuke.Text_Knob('', ""))


    # Add preset colour buttons



    backdrop.addKnob(nuke.PyScript_Knob('bmBackdrop_preset_red', "<img src='bmBackdrop_preset_red.png'>", 'nuke.thisNode().knob("tile_color").setValue(bm_NukeColourConverter.hex_colour_to_rgb(0.5*nuke.thisNode()["brightness_mult"].value(),0*nuke.thisNode()["brightness_mult"].value(),0*nuke.thisNode()["brightness_mult"].value()))\nnuke.thisNode().knob("note_font_color").setValue(bm_NukeColourConverter.hex_colour_to_rgb(1*nuke.thisNode()["brightness_mult"].value(),0.2*nuke.thisNode()["brightness_mult"].value(),0.2*nuke.thisNode()["brightness_mult"].value()))'))
    backdrop.knob('bmBackdrop_preset_red').setFlag(nuke.STARTLINE)

    backdrop.addKnob(nuke.PyScript_Knob('bmBackdrop_preset_orange', "<img src='bmBackdrop_preset_orange.png'>", 'nuke.thisNode().knob("tile_color").setValue(bm_NukeColourConverter.hex_colour_to_rgb(0.5*nuke.thisNode()["brightness_mult"].value(),0.2*nuke.thisNode()["brightness_mult"].value(),0*nuke.thisNode()["brightness_mult"].value()))\nnuke.thisNode().knob("note_font_color").setValue(bm_NukeColourConverter.hex_colour_to_rgb(1*nuke.thisNode()["brightness_mult"].value(),0.5*nuke.thisNode()["brightness_mult"].value(),0.2*nuke.thisNode()["brightness_mult"].value()))'))
    backdrop.addKnob(nuke.PyScript_Knob('bmBackdrop_preset_yellow', "<img src='bmBackdrop_preset_yellow.png'>", 'nuke.thisNode().knob("tile_color").setValue(bm_NukeColourConverter.hex_colour_to_rgb(0.5*nuke.thisNode()["brightness_mult"].value(),0.5*nuke.thisNode()["brightness_mult"].value(),0*nuke.thisNode()["brightness_mult"].value()))\nnuke.thisNode().knob("note_font_color").setValue(bm_NukeColourConverter.hex_colour_to_rgb(1*nuke.thisNode()["brightness_mult"].value(),1*nuke.thisNode()["brightness_mult"].value(),0.2*nuke.thisNode()["brightness_mult"].value()))'))
    backdrop.addKnob(nuke.PyScript_Knob('bmBackdrop_preset_lime', "<img src='bmBackdrop_preset_lime.png'>", 'nuke.thisNode().knob("tile_color").setValue(bm_NukeColourConverter.hex_colour_to_rgb(0.25*nuke.thisNode()["brightness_mult"].value(),0.5*nuke.thisNode()["brightness_mult"].value(),0*nuke.thisNode()["brightness_mult"].value()))\nnuke.thisNode().knob("note_font_color").setValue(bm_NukeColourConverter.hex_colour_to_rgb(0.5*nuke.thisNode()["brightness_mult"].value(),1*nuke.thisNode()["brightness_mult"].value(),0.2*nuke.thisNode()["brightness_mult"].value()))'))
    backdrop.addKnob(nuke.PyScript_Knob('bmBackdrop_preset_green', "<img src='bmBackdrop_preset_green.png'>", 'nuke.thisNode().knob("tile_color").setValue(bm_NukeColourConverter.hex_colour_to_rgb(0*nuke.thisNode()["brightness_mult"].value(),0.5*nuke.thisNode()["brightness_mult"].value(),0*nuke.thisNode()["brightness_mult"].value()))\nnuke.thisNode().knob("note_font_color").setValue(bm_NukeColourConverter.hex_colour_to_rgb(0.2*nuke.thisNode()["brightness_mult"].value(),1*nuke.thisNode()["brightness_mult"].value(),0.2*nuke.thisNode()["brightness_mult"].value()))'))
    backdrop.addKnob(nuke.PyScript_Knob('bmBackdrop_preset_teal', "<img src='bmBackdrop_preset_teal.png'>", 'nuke.thisNode().knob("tile_color").setValue(bm_NukeColourConverter.hex_colour_to_rgb(0*nuke.thisNode()["brightness_mult"].value(),0.5*nuke.thisNode()["brightness_mult"].value(),0.3*nuke.thisNode()["brightness_mult"].value()))\nnuke.thisNode().knob("note_font_color").setValue(bm_NukeColourConverter.hex_colour_to_rgb(0.2*nuke.thisNode()["brightness_mult"].value(),1*nuke.thisNode()["brightness_mult"].value(),0.7*nuke.thisNode()["brightness_mult"].value()))'))
    backdrop.addKnob(nuke.PyScript_Knob('bmBackdrop_preset_cyan', "<img src='bmBackdrop_preset_cyan.png'>", 'nuke.thisNode().knob("tile_color").setValue(bm_NukeColourConverter.hex_colour_to_rgb(0*nuke.thisNode()["brightness_mult"].value(),0.5*nuke.thisNode()["brightness_mult"].value(),0.5*nuke.thisNode()["brightness_mult"].value()))\nnuke.thisNode().knob("note_font_color").setValue(bm_NukeColourConverter.hex_colour_to_rgb(0.2*nuke.thisNode()["brightness_mult"].value(),1*nuke.thisNode()["brightness_mult"].value(),1*nuke.thisNode()["brightness_mult"].value()))'))
    backdrop.addKnob(nuke.PyScript_Knob('bmBackdrop_preset_blue', "<img src='bmBackdrop_preset_blue.png'>", 'nuke.thisNode().knob("tile_color").setValue(bm_NukeColourConverter.hex_colour_to_rgb(0*nuke.thisNode()["brightness_mult"].value(),0*nuke.thisNode()["brightness_mult"].value(),0.5*nuke.thisNode()["brightness_mult"].value()))\nnuke.thisNode().knob("note_font_color").setValue(bm_NukeColourConverter.hex_colour_to_rgb(0.4*nuke.thisNode()["brightness_mult"].value(),0.4*nuke.thisNode()["brightness_mult"].value(),1*nuke.thisNode()["brightness_mult"].value()))'))
    backdrop.addKnob(nuke.PyScript_Knob('bmBackdrop_preset_purple', "<img src='bmBackdrop_preset_purple.png'>", 'nuke.thisNode().knob("tile_color").setValue(bm_NukeColourConverter.hex_colour_to_rgb(0.2*nuke.thisNode()["brightness_mult"].value(),0*nuke.thisNode()["brightness_mult"].value(),0.5*nuke.thisNode()["brightness_mult"].value()))\nnuke.thisNode().knob("note_font_color").setValue(bm_NukeColourConverter.hex_colour_to_rgb(0.8*nuke.thisNode()["brightness_mult"].value(),0.5*nuke.thisNode()["brightness_mult"].value(),1*nuke.thisNode()["brightness_mult"].value()))'))
    backdrop.addKnob(nuke.PyScript_Knob('bmBackdrop_preset_magenta', "<img src='bmBackdrop_preset_magenta.png'>", 'nuke.thisNode().knob("tile_color").setValue(bm_NukeColourConverter.hex_colour_to_rgb(0.5*nuke.thisNode()["brightness_mult"].value(),0*nuke.thisNode()["brightness_mult"].value(),0.5*nuke.thisNode()["brightness_mult"].value()))\nnuke.thisNode().knob("note_font_color").setValue(bm_NukeColourConverter.hex_colour_to_rgb(1*nuke.thisNode()["brightness_mult"].value(),0.2*nuke.thisNode()["brightness_mult"].value(),1*nuke.thisNode()["brightness_mult"].value()))'))

    backdrop.addKnob(nuke.PyScript_Knob('bmBackdrop_preset_random', "<img src='bmBackdrop_preset_random.png'>", 'nuke.thisNode().knob("tile_color").setValue(bm_NukeColourConverter.hex_colour_to_rgb(random.random()*nuke.thisNode()["brightness_mult"].value(),random.random()*nuke.thisNode()["brightness_mult"].value(),random.random()*nuke.thisNode()["brightness_mult"].value()))\nnuke.thisNode().knob("note_font_color").setValue(bm_NukeColourConverter.hex_colour_to_rgb(random.random()*nuke.thisNode()["brightness_mult"].value(),random.random()*nuke.thisNode()["brightness_mult"].value(),random.random()*nuke.thisNode()["brightness_mult"].value()))'))
    backdrop.knob('bmBackdrop_preset_random').setFlag(nuke.STARTLINE)
    backdrop.addKnob(nuke.PyScript_Knob('bmBackdrop_preset_black', "<img src='bmBackdrop_preset_black.png'>", 'nuke.thisNode().knob("tile_color").setValue(bm_NukeColourConverter.hex_colour_to_rgb(0,0,0))\nnuke.thisNode().knob("note_font_color").setValue(bm_NukeColourConverter.hex_colour_to_rgb(0.2,0.2,0.2))'))
    backdrop.addKnob(nuke.PyScript_Knob('bmBackdrop_preset_darkgrey', "<img src='bmBackdrop_preset_darkgrey.png'>", 'nuke.thisNode().knob("tile_color").setValue(bm_NukeColourConverter.hex_colour_to_rgb(0.25,0.25,0.25))\nnuke.thisNode().knob("note_font_color").setValue(bm_NukeColourConverter.hex_colour_to_rgb(0.5,0.5,0.5))'))
    backdrop.addKnob(nuke.PyScript_Knob('bmBackdrop_preset_midgrey', "<img src='bmBackdrop_preset_midgrey.png'>", 'nuke.thisNode().knob("tile_color").setValue(bm_NukeColourConverter.hex_colour_to_rgb(0.5,0.5,0.5))\nnuke.thisNode().knob("note_font_color").setValue(bm_NukeColourConverter.hex_colour_to_rgb(0,0,0))'))
    backdrop.addKnob(nuke.PyScript_Knob('bmBackdrop_preset_lightgrey', "<img src='bmBackdrop_preset_lightgrey.png'>", 'nuke.thisNode().knob("tile_color").setValue(bm_NukeColourConverter.hex_colour_to_rgb(0.75,0.75,0.75))\nnuke.thisNode().knob("note_font_color").setValue(bm_NukeColourConverter.hex_colour_to_rgb(0.25,0.25,0.25))'))
    backdrop.addKnob(nuke.PyScript_Knob('bmBackdrop_preset_white', "<img src='bmBackdrop_preset_white.png'>", 'nuke.thisNode().knob("tile_color").setValue(bm_NukeColourConverter.hex_colour_to_rgb(1,1,1))\nnuke.thisNode().knob("note_font_color").setValue(bm_NukeColourConverter.hex_colour_to_rgb(0.2,0.2,0.2))'))




    # Divider Line
    backdrop.addKnob(nuke.Text_Knob('', ""))


nuke.menu('Nodes').addMenu('Other').addCommand('Backdrop', 'bm_BackdropNode.bm_BackdropNode(" ", 100, 0.25, 0.25, 0.25, 50, 0)', "alt+b", icon="Backdrop.png", shortcutContext=2)
nuke.menu('Nodes').addMenu('Other').addCommand('Backdrop Random', 'bm_BackdropNode.bm_BackdropNode(" ", 100, random.random(), random.random(), random.random(), 50, 0)', "ctrl+alt+b", icon="Backdrop.png", shortcutContext=2)

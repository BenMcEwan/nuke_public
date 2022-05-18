# --------------------------------------------------------------
#  bm_DefaultBackdrop.py
#  Version: 1.1.2
#  Last Updated: May 17th, 2022
# --------------------------------------------------------------

# --------------------------------------------------------------
#  USAGE:
#
# - Adds better backdrop node defaults & presets
#
# --------------------------------------------------------------

# --------------------------------------------------------------
#  BACKDROP NODE SHORTCUTS :::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

import nuke
import random
import bm_NukeColourConverter

def defaultBackdrop(name, bgColR, bgColG, bgColB, tColR, tColG, tColB, sizemultX, sizemultY, zIndex, font, font_size, nodes = None):

    # Define Colors
    bgColor = int('%02x%02x%02x%02x' % (int(bgColR*255),int(bgColG*255),int(bgColB*255),255),16)
    textColor = int('%02x%02x%02x%02x' % (int(tColR*255),int(tColG*255),int(tColB*255),255),16)
    if name == "ask":
        try:
            name = " "+nuke.getInput("Name your backdrop")
        except:
            return

    if nodes is None:
        nodes = nuke.selectedNodes()
    if len(nodes) == 0:
        dot = nuke.createNode("Dot")
        nodes = nuke.selectedNodes()

    # Calculate bounds for the backdrop node.
    bdX = min([node.xpos() for node in nodes])
    bdY = min([node.ypos() for node in nodes])
    bdW = max([node.xpos() + node.screenWidth() for node in nodes]) - bdX
    bdH = max([node.ypos() + node.screenHeight() for node in nodes]) - bdY

    # Expand the bounds to leave a little border. Elements are offsets for left, top, right and bottom edges respectively
    left, top, right, bottom = (-70*int(sizemultX), -140*int(sizemultY), 70*int(sizemultX), 70*int(sizemultY))
    bdX += left
    bdY += top
    bdW += (right - left)
    bdH += (bottom - top)

    # Set backdrop parameters
    n = nuke.nodes.BackdropNode(xpos = bdX,
                              bdwidth = bdW,
                              ypos = bdY,
                              bdheight = bdH,
                              z_order = zIndex,
                              tile_color = bgColor,
                              note_font_color = textColor,
                              note_font_size=font_size,
                              label=name,
                              name=' ',
                note_font=font)

    # Revert to previous selection
    for node in nodes:
        node['selected'].setValue(True)

    try:
        nuke.delete(dot)
    except:
        pass

    # Ensure backdrop is selected, to make moving easier
    n['selected'].setValue(True)

    nuke.show(n)
    return n





def backdrop_scale(increment):

    if nuke.selectedNode().Class() == "BackdropNode":
        backdrop = nuke.selectedNode()
    else:
        nuke.message("Please select a backdrop node")
        return


    xpos = backdrop.knob('xpos').value()
    ypos = backdrop.knob('ypos').value()
    width = backdrop.knob('bdwidth').value()
    height = backdrop.knob('bdheight').value()

    backdrop.knob('xpos').setValue(xpos-increment)
    backdrop.knob('ypos').setValue(ypos-increment)
    backdrop.knob('bdwidth').setValue(width+(increment*2))
    backdrop.knob('bdheight').setValue(height+(increment*2))




def backdrop_randomcolour():

    if nuke.selectedNode().Class() == "BackdropNode":
        backdrop = nuke.selectedNode()
    else:
        nuke.message("Please select a backdrop node")
        return


    backdrop.knob('tile_color').setValue(bm_NukeColourConverter.hex_colour_to_rgb(random.random(), random.random(), random.random()))
    backdrop.knob('note_font_color').setValue(bm_NukeColourConverter.hex_colour_to_rgb(random.random(), random.random(), random.random()))


def TILEtoRGB(V):

    R = (0xFF & V >> 24) / 255.0
    G = (0xFF & V >> 16) / 255.0
    B = (0xFF & V >> 8) / 255.0

    return R,G,B


def backdrop_lumachange(lumaChangeValue):

    if nuke.selectedNode().Class() == "BackdropNode":
        backdrop = nuke.selectedNode()
    else:
        nuke.message("Please select a backdrop node")
        return

    cur_tile_color = TILEtoRGB(backdrop.knob('tile_color').value())
    cur_font_color = TILEtoRGB(backdrop.knob('note_font_color').value())
    backdrop.knob('tile_color').setValue(bm_NukeColourConverter.hex_colour_to_rgb((cur_tile_color[0]+lumaChangeValue), (cur_tile_color[1]+lumaChangeValue), (cur_tile_color[2]+lumaChangeValue)))
    backdrop.knob('note_font_color').setValue(bm_NukeColourConverter.hex_colour_to_rgb((cur_font_color[0]+lumaChangeValue), (cur_font_color[1]+lumaChangeValue), (cur_font_color[2]+lumaChangeValue)))






# ----- BACKDROP NODES TOOLBAR -----------------------------------

# Add Menu
bm_BackdropMenu = nuke.menu('Nodes').addMenu('bmBackdrops', icon='Backdrop_HighRes.png')

bm_BackdropMenu.addCommand('Generic', 'bm_DefaultBackdrop.defaultBackdrop(0.267, 0.267, 0.267, 0.498, 0.498, 0.498, 1.5, 1.5, 0, "Arial", 60)', 'alt+b', icon="Backdrop_HighRes.png")
bm_BackdropMenu.addCommand('Random Colour', 'bm_DefaultBackdrop.defaultBackdrop(random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), 1.5, 1.5, 0, "Arial", 60)', 'ctrl+alt+b', icon="Backdrop_Rainbow.png")

bm_BackdropMenu.addCommand('-', "", "")  ###  Add separator  ###

bm_BackdropMenu.addCommand('Generic', 'bm_DefaultBackdrop.defaultBackdrop("ask", 0.267, 0.267, 0.267, 0.498, 0.498, 0.498, 1.5, 1.5, 0, "Arial", 60)', 'alt+b', icon="Backdrop.png")
bm_BackdropMenu.addCommand('Random Colour', 'bm_DefaultBackdrop.defaultBackdrop("ask", random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), 1.5, 1.5, 0, "Arial", 60)', 'ctrl+alt+b', icon="Backdrop.png")

bm_BackdropMenu.addCommand('-', "", "")  ###  Add separator  ###

bm_BackdropMenu.addCommand('Reference', 'bm_DefaultBackdrop.defaultBackdrop(" Reference", 0.267, 0.267, 0.267, 0.498, 0.498, 0.498, 1.5, 1.5, 0, "Arial", 60)', icon="Backdrop20Grey.png")
bm_BackdropMenu.addCommand('Last Comp Version', 'bm_DefaultBackdrop.defaultBackdrop(" Last Comp Version", 0.267, 0.267, 0.267, 0.498, 0.498, 0.498, 1.5, 1.5, 0, "Arial", 60)', icon="Backdrop20Grey.png")
bm_BackdropMenu.addCommand('Last Client Version', 'bm_DefaultBackdrop.defaultBackdrop(" Last Client Version", 0, 0.35, 0, 0, .8, 0, 1.5, 1.5, 0, "Arial", 60)', icon="Backdrop20Grey.png")
bm_BackdropMenu.addCommand('Output', 'bm_DefaultBackdrop.defaultBackdrop(" Output", 0.55, 0.51, 0, 0.908, 0.92, 0.177, 1.5, 1.5, 0, "Arial", 60)', icon="Backdrop20Grey.png")

bm_BackdropMenu.addCommand('-', "", "")  ###  Add separator  ###

bm_BackdropMenu.addCommand('Red', 'bm_DefaultBackdrop.defaultBackdrop("ask", 0.5, 0, 0, 1, 0.2, 0.2, 1.5, 1.5, 0, "Arial", 60)', icon="BackdropRed.png")
bm_BackdropMenu.addCommand('Orange', 'bm_DefaultBackdrop.defaultBackdrop("ask", 0.5, 0.267, 0, 1, 0.53, 0.2, 1.5, 1.5, 0, "Arial", 60)', icon="BackdropOrange.png")
bm_BackdropMenu.addCommand('Yellow', 'bm_DefaultBackdrop.defaultBackdrop("ask", 0.55, 0.51, 0, 0.908, 0.92, 0.177, 1.5, 1.5, 0, "Arial", 60)', icon="BackdropYellow.png")
bm_BackdropMenu.addCommand('Green', 'bm_DefaultBackdrop.defaultBackdrop("ask", 0, 0.55, 0, 0.188, 1, 0.22, 1.5, 1.5, 0, "Arial", 60)', icon="BackdropGreen.png")
bm_BackdropMenu.addCommand('Cyan', 'bm_DefaultBackdrop.defaultBackdrop("ask", 0, 0.55, 0.54, 0.192, 0.98, 1, 1.5, 1.5, 0, "Arial", 60)', icon="BackdropCyan.png")
bm_BackdropMenu.addCommand('Blue', 'bm_DefaultBackdrop.defaultBackdrop("ask", 0, 0.18, 0.55, 0.212, 0.49, 1, 1.5, 1.5, 0, "Arial", 60)', icon="BackdropBlue.png")
bm_BackdropMenu.addCommand('Purple', 'bm_DefaultBackdrop.defaultBackdrop("ask", 0.306, 0, 0.549, 0.71, 0.322, 1, 1.5, 1.5, 0, "Arial", 60)', icon="BackdropPurple.png")
bm_BackdropMenu.addCommand('Pink', 'bm_DefaultBackdrop.defaultBackdrop("ask", 0.55, 0, 0.447, 1, 0.318, 0.886, 1.5, 1.5, 0, "Arial", 60)', icon="BackdropPink.png")
bm_BackdropMenu.addCommand('White', 'bm_DefaultBackdrop.defaultBackdrop("ask", 1, 1, 1, 0, 0, 0, 1.5, 1.5, 0, "Arial", 60)', icon="BackdropWhite.png")
bm_BackdropMenu.addCommand('80% Grey', 'bm_DefaultBackdrop.defaultBackdrop("ask", 0.8, 0.8, 0.8, 0, 0, 0, 1.5, 1.5, 0, "Arial", 60)', icon="Backdrop80Grey.png")
bm_BackdropMenu.addCommand('60% Grey', 'bm_DefaultBackdrop.defaultBackdrop("ask", 0.6, 0.6, 0.6, 0.9, 0.9, 0.9, 1.5, 1.5, "Arial", 60)', icon="Backdrop60Grey.png")
bm_BackdropMenu.addCommand('40% Grey', 'bm_DefaultBackdrop.defaultBackdrop("ask", 0.4, 0.4, 0.4, 0.7, 0.7, 0.7, 1.5, 1.5, 0, "Arial", 60)', icon="Backdrop40Grey.png")
bm_BackdropMenu.addCommand('20% Grey', 'bm_DefaultBackdrop.defaultBackdrop("ask", 0.2, 0.2, 0.2, 0.5, 0.5, 0.5, 1.5, 1.5, 0, "Arial", 60)', icon="Backdrop20Grey.png")
bm_BackdropMenu.addCommand('Black', 'bm_DefaultBackdrop.defaultBackdrop("ask", 0, 0, 0, 1, 1, 1, 1.5, 1.5, 0, "Arial", 60)', icon="BackdropBlack.png")

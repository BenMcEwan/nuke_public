# --------------------------------------------------------------
#  bm_AutoContactSheet.py
#  Version: 1.2.1
#  Last Updated: July 10th, 2019
# --------------------------------------------------------------


# --------------------------------------------------------------
#  USAGE:
#
# - Sets better defaults for the ContactSheet node in nuke, to automate all of the settings
# - Creates a second text node option that automatically sets bounding box & label
# - Finally, combines all this code together (and repeats in some areas for clarity) to make a fully-automatic ContactSheet node with the click of a button!
#
# (Temporarily removing $gui from font)
#
# --------------------------------------------------------------

import nuke

def bm_AutoContactSheet():

    # Start by creating lists to hold certain information -- this will become clear as we get into things
    nodeList = []
    xVals = []
    yVals = []

    # Loop through all selected nodes in the node graph
    for node in nuke.selectedNodes():

        # Label our text nodes to be whatever the top-most Read node is...
        textValue = " [basename [file rootname [value [topnode].file]]]"

        # Creates a text node underneath every selected node & connects its input accordingly
        textNode = nuke.createNode("Text2")
        textNode.setInput(0, node)

        # Set the bbox of the text node to match the input format
        textNode['box'].setValue(0, 0)
        textNode['box'].setValue(0, 1)
        textNode['box'].setExpression("input.width", 2)
        textNode['box'].setExpression("input.height", 3)
        textNode['xjustify'].setValue("left")
        textNode['yjustify'].setValue("bottom")

        # Add relevant label as per the if/else statement above
        textNode['message'].setValue(textValue)
        textNode['shadow_opacity'].setValue('1')
        textNode['label'].setValue('[value message]')

        # Add selected nodes to a list
        nodeList.append(textNode)

        # Add the X and Y position of all selected nodes to their respective lists
        xVals.append(node['xpos'].value())
        yVals.append(node['ypos'].value())


    # Create a contact sheet node. This will come in with the new defaults we set above!
    cs = nuke.createNode("ContactSheet")

    # Add better knob defaults to Contact Sheet
    cs['width'].setExpression("input.width * columns * resMult")
    cs['height'].setExpression("input.height * rows * resMult * aspect")
    cs['roworder'].setValue("TopBottom")
    cs['colorder'].setValue("LeftRight")
    cs['rows'].setExpression("ceil(inputs/columns)")
    cs['columns'].setExpression("ceil(sqrt(inputs))")

    # Add custom knobs to the User tab to allow some control of our text nodes (User tab is created automatically by Nuke)
    cs.addKnob(nuke.Text_Knob('',''))
    cs.addKnob(nuke.Double_Knob('resMult', "Resolution Multiplier"))
    cs.addKnob(nuke.Double_Knob('aspect', "Aspect Ratio"))
    cs['resMult'].setValue(1)
    cs['aspect'].setValue(1)
    cs.addKnob(nuke.Text_Knob('',''))
    cs.addKnob(nuke.Boolean_Knob('showText', 'Show Text', True))
    textBG_ops = "None", "Shadow", "Solid"
    cs.addKnob(nuke.Enumeration_Knob('textBG', 'Text Background', textBG_ops))
    cs.addKnob(nuke.Double_Knob('textSize', 'Text Size'))
    cs['textSize'].setValue(1)
    cs.addKnob(nuke.Text_Knob('',''))

    iterator = 0

    # Add relevant expressions to our text nodes, so the Text size & background options work as expected
    for nodes in nodeList:

        cs.setInput(iterator, nodes)
        nodes['enable_background'].setExpression(cs['name'].value()+".textBG == 2 ? 1 : 0")
        nodes['enable_shadows'].setExpression(cs['name'].value()+".textBG == 1 ? 1 : 0")
        nodes['disable'].setExpression(cs['name'].value()+".showText == 1 ? 0 : 1")
        nodes['global_font_scale'].setExpression(cs['name'].value()+".textSize")

        iterator = iterator + 1

    # Find the average of all selected nodes' X and Y positions
    avgXpos = sum(xVals) / len(nodeList)
    avgYpos = sum(yVals) / len(nodeList)

    # Force set the position of our newly created contact sheet in the node graph
    cs['xpos'].setValue(avgXpos)
    cs['ypos'].setValue(avgYpos+200)


# Add to Comp Toolbox menu
nuke.menu('Nodes').addCommand("Merge/Auto Contact Sheet", "bm_AutoContactSheet.bm_AutoContactSheet()", icon="ContactSheet.png")

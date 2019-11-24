# --------------------------------------------------------------
#  bm_NodeSandwich.py
#  Version: 1.2.7
#  Author: Ben McEwan
#
#  Last Modified by: Ben McEwan
#  Last Updated: October 23rd, 2019
# --------------------------------------------------------------

# --------------------------------------------------------------
#  USAGE:
#
#  Sandwiches selected node between two nodes (like an unpremult/premult, or lin2log/log2lin conversion)
# --------------------------------------------------------------

import nuke

def bm_NodeSandwich(node_before, node_after):

	# Setup some lists for later use.
	nodes = nuke.selectedNodes()
	new_input_nodes = []
	double_input_classes = ['Merge2', 'Keymix', 'Switch', 'Dissolve', 'Copy', 'ShuffleCopy', 'AddMix', 'SplineWarp']

	# If no nodes are selected, throw an error message.
	if len(nodes) == 0:
		nuke.message("Please select at least one node to fill the sandwich.")
		return
	
	# If they are, we want to sort them from first selection to last. Using the y-position in the node graph
	# is a hack but it seems to work!
	else:    
		nodes.sort(key=lambda item: item['ypos'].value())

	# Now that the nodes are sorted we can easily get the first and last nodes in the selection, for later use.
	top_node = nodes[0]
	bottom_node = nodes[-1]



	# ----------  Let's figure out which nodes will get a "node_before" created  ----------

	# Find any connected input that isn't part of our original selection, or isn't plugged into
	# a 'mask' input, and add them to a new list.
	input_nodes = []

	for node in nodes:

		# We're relying on Nuke's in-built logic for how nodes are connected upon creation when another is selected.
		# We should deselect all of our nodes to make sure nothing funky happens...
		node.setSelected(False)

		# Add dependent nodes to the list, if they're not part of the originally-selected nodes.
		for x in node.dependencies():
			if x not in nodes:
				input_nodes.append(x)
	
		# Check for nodes connected to mask inputs, and remove those from our list.
		if node.Class() in double_input_classes:
			if len(node.dependencies()) > 2:
				input_nodes.remove(node.dependencies()[2])
		elif len(node.dependencies()) > 1:
			input_nodes.remove(node.dependencies()[1])
	
	# Lastly, remove any duplicates in the list.
	input_nodes = list(dict.fromkeys(input_nodes))
	


	# --------------------  Now we can get onto the node creation fun  --------------------

	# If the first node's input isn't connected, we should create & connected a node manually.
	if top_node.input(0) == None:

		# Create and hook up 'node_before'.
		in_node = nuke.createNode(node_before)
		in_node.setSelected(False)
		top_node.setInput(0, in_node)

		# Force the node's position	in the node graph.
		if top_node.input(0).Class() == 'Dot':
			in_node.knob('xpos').setValue(i.input(0).xpos())
		else:
			in_node.knob('xpos').setValue(top_node.xpos())

		in_node.knob('ypos').setValue(top_node.ypos()-50)

		# Add all in_nodes to our previously-created list.
		new_input_nodes.append(in_node)



	# For any other circumstance, this is where the magic happens. We'll loop through all the nodes that
	# are connected to our originally-selected nodes' inputs' and do the same thing to each...
	for i in input_nodes:

		# Select the input node, then create the 'node_before' (its input & output should auto-connect based off the selection),
		# then deselect the node in preperation for creating the next node.
		i.setSelected(True)
		in_node = nuke.createNode(node_before)
		in_node.setSelected(False)

		# Force the node's position to be directly underneath the input node...
		in_node.knob('ypos').setValue(i.ypos()+50)

		# For the x-position, if the node is a dot, it'll screw things up, so we have to account for that.
		if i.Class() == 'Dot':
			if i.input(0):
				in_node.knob('xpos').setValue(i.input(0).xpos())
			else:        	
				in_node.knob('xpos').setValue(i.xpos())

		# Add all in_nodes to our previously-created list.
		new_input_nodes.append(in_node)
	        


	# In a case where we have a node with multiple inputs, the user would likely already have their Nuke script
	# laid out in right-angles. Using a Merge node as an example, adding our new node underneath the node that's
	# connected to the Merge's A input would mess up the artists' nice layout. This is a quick hack to say:
	# 'if the A input is connected, shift the originally-selected node down to line up again.'
	if node.input(1):
		if node.input(1).ypos() >= node.ypos():
			node.knob('ypos').setValue(node.input(1).ypos())    

	

	# -------------  Now we can create our Output node, which is far simpler!  ------------------------------------

	# Once again we'll select the originally-selected node to take advantage of the built-in automatic node connection.
	bottom_node.setSelected(True)

	# Then we create the node, and force it's position in the node graph relative to the originally-selected node.
	out_node = nuke.createNode(node_after)

	if bottom_node.Class() == 'Dot':
		out_node.knob('xpos').setValue(bottom_node.input(0).xpos())
	else:
		out_node.knob('xpos').setValue(node.xpos())

	out_node.knob('ypos').setValue(node.ypos()+50)



	# -------  Lastly, if we create a Log Sandwich, we have to set specific knob values for our nodes  --------

	for x in new_input_nodes:
		if x.Class() == 'Log2Lin':
			x.knob('operation').setValue("lin2log")
			out_node.knob('operation').setValue("log2lin")
		else:
			return




# Lastly, let's add some sandwiches to the appropriate menus!        
nuke.menu('Nodes').addCommand('Color/Log Sandwich', 'bm_NodeSandwich.bm_NodeSandwich("Log2Lin", "Log2Lin")', "ctrl+shift+l", icon="bm_NodeSandwich.png")
nuke.menu('Nodes').addCommand('Merge/Premult Sandwich', 'bm_NodeSandwich.bm_NodeSandwich("Unpremult", "Premult")', "ctrl+shift+p", icon="bm_NodeSandwich.png")

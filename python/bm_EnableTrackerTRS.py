# --------------------------------------------------------------
#  bm_EnableTrackerTRS.py
#  Version: 1.0.1
#  Author: Ben McEwan
#
#  Last Modified by: Ben McEwan
#  Last Updated: May 17th, 2022
# --------------------------------------------------------------

# --------------------------------------------------------------
#  USAGE:
#
#  Adds a meta+t hotkey to enable all T, R & S checkboxes in a selected Tracker node.
# --------------------------------------------------------------


import nuke

def bm_EnableTrackerTRS():
	#ENABLE TRANSLATE, ROTATE AND SCALE IN SELECTED TRACKER
	t = [8, 39, 70, 101, 132, 163, 194, 225, 256, 287, 318, 7, 38, 69, 100, 131, 162, 193, 224, 255, 286, 317, 6, 37, 68, 99, 130, 161, 192, 223, 254, 285, 316, 349, 380, 411, 442, 473, 504, 535, 566, 597, 628, 659, 348, 379, 410, 441, 472, 503, 534, 565, 596, 627, 658, 347, 378, 409, 440, 471, 502, 533, 564, 595, 626, 657]
	try:
		nuke.selectedNode()
	except:
		nuke.message("Select a Tracker to enable Translate, Rotate & Scale")

	if nuke.selectedNode().Class() == 'Tracker4':
		for n in t:
			nuke.selectedNode()['tracks'].setValue(True, n)
	else:
		nuke.message("Select a Tracker to enable Translate, Rotate & Scale")


# Add menu items
nuke.menu('Nuke').addCommand('Edit/Shortcuts/Enable Tracker T-R-S', 'bm_EnableTrackerTRS.bm_EnableTrackerTRS()', 'meta+t')

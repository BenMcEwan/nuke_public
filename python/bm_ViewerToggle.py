# --------------------------------------------------------------
#  bm_ViewerToggle.py
#  Version: 1.0.2
#  Author: Ben McEwan
#
#  Last Modified by: Ben McEwan
#  Last Updated: July 4th, 2019
# --------------------------------------------------------------

# --------------------------------------------------------------
#  USAGE:
#
#  ALT+Q toggles viewer exposure & gamma between custom value and default.
# --------------------------------------------------------------

import nuke

gain_vals = {1:1}
gamma_vals = {1:1}

def bm_ViewerToggle():

    global gain_vals
    global gamma_vals
    
    viewer = nuke.activeViewer().node()
    gain = viewer.knob('gain')
    gamma = viewer.knob('gamma')

    if gain.value() != 1 or gamma.value() != 1:
        gain_vals[1] = gain.value()
        gamma_vals[1] = gamma.value()
        gain.setValue(1)
        gamma.setValue(1)

    else:
        gain.setValue(gain_vals[1])
        gamma.setValue(gamma_vals[1])
        


# Add to menu
nuke.menu("Viewer").addCommand("Toggle Viewer Gain & Gamma", 'bm_ViewerToggle.bm_ViewerToggle()', "alt+q")
nuke.menu("Nuke").addCommand("Viewer/Toggle Viewer Gain & Gamma", 'bm_ViewerToggle.bm_ViewerToggle()', "alt+q")

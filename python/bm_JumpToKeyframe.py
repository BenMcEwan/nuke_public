# --------------------------------------------------------------
#  bm_JumpToKeyframe.py
#  Version: 2.0.0
#  Author: Ben McEwan
#
#  Last Modified by: Ben McEwan
#  Last Updated: March 5th, 2019
# --------------------------------------------------------------

# --------------------------------------------------------------
#  USAGE:
#
#  Map Up and Down arrow keys to jump between next & previous keyframes
# --------------------------------------------------------------

import nuke

def bm_JumpToKeyframe(arg):

    if arg == "next":
        nuke.activeViewer().frameControl(-4)
    elif arg == "prev":
        nuke.activeViewer().frameControl(+4)
    else:
        nuke.message("No keyframes to jump between")

# Add menu items
nuke.menu('Viewer').addCommand('Next Keyframe', 'bm_JumpToKeyframe.bm_JumpToKeyframe("next")', 'Up')
nuke.menu('Viewer').addCommand('Previous Keyframe', 'bm_JumpToKeyframe.bm_JumpToKeyframe("prev")', 'Down')

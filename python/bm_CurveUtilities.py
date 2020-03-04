# --------------------------------------------------------------
#  bm_CurveUtilities.py
#  Version: 0.0.2
#  Author: Ben McEwan
#
#  Last Modified by: Ben McEwan
#  Last Updated: January 22nd, 2020
# --------------------------------------------------------------

# --------------------------------------------------------------
#  USAGE:
#
#  Adds some handy animation shortcuts to a knob's right-click menu.
#  "Respeed" option currently uncommented, as it's currently not working as intended...
# --------------------------------------------------------------

import nuke


# FrameHold
def curve_framehold():
    nuke.thisKnob().setExpression('curve('+str(nuke.frame())+')')

nuke.menu('Animation').addCommand("Curve Utilities/FrameHold on Current Frame", "bm_CurveUtilities.curve_framehold()")



# Reference Frame
def curve_refFrame():
    nuke.thisKnob().setExpression('curve-(curve('+str(nuke.frame())+'))')

nuke.menu('Animation').addCommand("Curve Utilities/Set Reference Frame to Current Frame", "bm_CurveUtilities.curve_refFrame()")



# Curve remapper
def curve_remapper():
    #Adds python into expression knob, which evalutes and finds the answer
    curveMin = min((key.y for key in nuke.thisKnob().animation(0).keys()))
    curveMax = max((key.y for key in nuke.thisKnob().animation(0).keys()))

    nuke.thisKnob().setExpression('lerp('+str(curveMin)+',0,'+str(curveMax)+',1, curve)')

nuke.menu('Animation').addCommand("Curve Utilities/Remap values between 0 and 1", "bm_CurveUtilities.curve_remapper()")



"""
# % Respeed -- Currently a broken WIP.
def curve_respeed():
    anim = nuke.thisKnob().animation(0)
    respeed = int(nuke.getInput("% Respeed"))
    print "\n\nFirst Frame = "+str(anim.keys()[0].x)
    print "Last Frame = "+str(anim.keys()[-1].x)
    if respeed > 100:
    	anim.keys()[-1].x = anim.keys()[-1].x-((anim.keys()[-1].x-anim.keys()[0].x)/(respeed*0.01))
    elif respeed < 100:
    	anim.keys()[-1].x = anim.keys()[-1].x+(((anim.keys()[-1].x-anim.keys()[0].x)/(respeed*0.01))/2)
    else:
		nuke.message("No respeed happening")
    anim.keys()[-1].extrapolation = nuke.LINEAR
    print "\n"+str(respeed)+"% Respeed, Last Frame = "+str(anim.keys()[-1].x)
nuke.menu('Animation').addCommand("Curve Utilities/% Respeed Curve", "bm_CurveUtilities.curve_respeed()")
"""

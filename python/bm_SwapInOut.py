# --------------------------------------------------------------
#  bm_SwapInOut.py
#  Version: 1.0.0
#  Author: Ben McEwan
#
#  Last Modified by: Ben McEwan
#  Last Updated: March 21st, 2019
# --------------------------------------------------------------

# --------------------------------------------------------------
#  USAGE:
#
#  Easily fix scripts that use in & out, instead of mask & stencil.
# --------------------------------------------------------------

import nuke
import nukescripts

def bm_SwapInOut():

  n = nuke.allNodes()

  for i in n:
      if i.Class() == 'Merge2':
		  if i['operation'].value() == 'in':
		      i['operation'].setValue('mask')
		      nukescripts.swapAB(i)
		  elif i['operation'].value() == 'out':
		      i['operation'].setValue('stencil')
		      nukescripts.swapAB(i)

		      

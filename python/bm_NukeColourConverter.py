# --------------------------------------------------------------
#  bm_NukeColourConverter.py
#  Version: 1.0.0
#  Author: Ben McEwan
#
#  Last Modified by: Ben McEwan
#  Last Updated: June 24th, 2019
# --------------------------------------------------------------

# --------------------------------------------------------------
#  USAGE:
#
#  Convert Nuke's hex colour to easier web-based hex, or RGB integer
#  based off the colour sliders we're used to using.
# --------------------------------------------------------------

import nuke

def hex_colour_to_int(hexValue):
    return int(hexValue+'00', 16)

def hex_colour_to_rgb(red, green, blue):
    return int('%02x%02x%02x%02x' % (red*255, green*255, blue*255, 255),16)

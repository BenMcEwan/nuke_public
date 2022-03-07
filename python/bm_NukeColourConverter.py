# --------------------------------------------------------------
#  bm_NukeColourConverter.py
#  Version: 1.1.0
#  Author: Ben McEwan
#
#  Last Modified by: Ben McEwan
#  Last Updated: March 7th, 2022
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
    return int('%02x%02x%02x%02x' % (int(red*255), int(green*255), int(blue*255), 255),16)

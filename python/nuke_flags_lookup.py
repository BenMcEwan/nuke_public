#############  Pulled from NUKE 16.0's Knob.h file.  #############
# 
### Suggested Usage:
# 
# from nuke_flags_lookup import get_nuke_flag_from_name as flag
# 
# nuke.toNode("Grade1")["mix"].setFlag(flag("DISABLED"))
# 
##################################################################


def get_nuke_flag_from_name(flag_name):
    """
    Returns a hexadecimal flag, given the string input.
    """

    # fmt:off
    knob_flags_dict = {
        
        # -----  General Flags  ----------------------------------------------------------------------------------------
        
        "DISABLED": 0x0000000000000080,                 # Grey out and lock interface. Prevents copy/paste (see READ_ONLY to allow this).
        "NO_ANIMATION": 0x0000000000000100,             # Disable right click and button animation menu.
        "DO_NOT_WRITE": 0x0000000000000200,             # Disables calling to_script. No writing to script file or copy/paste.
        "INVISIBLE": 0x0000000000000400,                # Disables param and viewer widgets. Cannot be made visible again. See HIDDEN for this.
        "RESIZABLE": 0x0000000000000800,                # Allows more complex knobs to resize param panel to fill available space.
        "STARTLINE": 0x0000000000001000,                # Start a new line in the param panel before knob widget.
        "ENDLINE": 0x0000000000002000,                  # Start a new line in the param panel after knob widget.
        "NO_RERENDER": 0x0000000000004000,              # Removes knob from Op hash calculation, preventing rerendering on value change.
        "NO_HANDLES": 0x0000000000008000,               # Disables viewer widget handles from drawing.
        "KNOB_CHANGED_ALWAYS": 0x0000000000010000,      # Always calls knob_changed, regardless of whether it has previously returned false.
        "NO_KNOB_CHANGED": 0x0000000000020000,          # Prevents knob_changed being called on value change. Set if prev knob_changed returned false.
        "HIDDEN": 0x0000000000040000,                   # Disables param panel and viewer widgets. Can be managed dynamically with show/hide.
        "NO_UNDO": 0x0000000000080000,                  # Disables laying down of undo/redo points.
        "ALWAYS_SAVE": 0x0000000000100000,              # Forces data to always be written regardless. Deprecated. Override not_default instead.
        "NODE_KNOB": 0x0000000000200000,                # For internal use only.
        "HANDLES_ANYWAY": 0x0000000000400000,           # Force viewer widgets to be visible regardless of current node tab.
        "INDETERMINATE": 0x0000000000800000,            # Presents a blacked out undefined value interface on supporting knobs.
        "COLOURCHIP_HAS_UNSET": 0x0000000001000000,     # Defines whether a color chip can be in the 'unset' state. Defaults to false.
        "SMALL_UI": 0x0000000002000000,                 # Switches param panel widget to be more viewer Toolbar friendly in supported knobs (eg Button).
        "NO_NUMERIC_FIELDS": 0x0000000004000000,        # Disables numeric input box widget on supported knobs.
        "KNOB_CHANGED_RECURSIVE": 0x0000000008000000,   # Recursive knob_changed calls are prevented unless overriden using this flag.
        "READ_ONLY": 0x0000000010000000,                # As with DISABLED, except value can be copied from and expression linked against.
        "NO_CURVE_EDITOR": 0x0000000020000000,          # Disables curve editor.
        "NO_MULTIVIEW": 0x0000000040000000,             # Disables view menu and splitting when in a multiview script.
        "EARLY_STORE": 0x0000000080000000,              # Forces early synchronisation of data allowing usage in pre-op calls such as split_input().
        "MODIFIES_GEOMETRY": 0x0000000100000000,        # Should be set on all knobs which modify geometry or associated transforms.
        "OUTPUT_ONLY": 0x0000000200000000,              # Similar to READ_ONLY & NO_RERENDER together - data changes don't count as a script change.
        "NO_KNOB_CHANGED_FINISHED": 0x0000000400000000, # Prevents knob_changed_finished being called on value change. Set if prev call returned false.
        "SET_SIZE_POLICY": 0x0000000800000000,          # Do not use.
        "EXPAND_TO_WIDTH": 0x0000001000000000,          # Force knob to expand to fill available space. - only for Enum knobs currently
        "NEVER_DRAW_HANDLES": 0x0000002000000000,       # Disables viewer widget handles from drawing. Unlike the NO_HANDLES flag, the state of this flag will never change internally within Nuke
        "KNOB_CHANGED_RIGHTCONTEXT": 0x0000004000000000,# Always call knob_changed on a properly cooked Op, even if KNOB_CHANGED_ALWAYS is on
        "DONT_SAVE_TO_NODEPRESET": 0x0000008000000000,  # This value of this knob should never be saved to a NodePreset. Can be used, for example, for data knobs.
        "RESERVED_COLORCHIP_KNOB": 0x0000010000000000,  # DO NOT USE. This value is used by the colorchip knob.
        "READ_ONLY_IN_SCRIPTS": 0x0000020000000000,     # Prevents knobs from being modified from Python/Tcl
        "ALWAYS_ALIGN_LABEL_TOP": 0x0000040000000000,   # Label is always aligned to the top of the Knob
        "TINY_SLIDER": 0x0000080000000000,              # Modifies SLIDER to be a tiny slider underneath lineedit. Should be a numeric knob flag but we've overrun the < 0x80 condition.
        "HIDE_ANIMATION_AND_VIEWS": 0x0000100000000000, # Prevents Animation Curve_Knob and Views being shown. Animation is still possible, unless NO_ANIMATION is set of course.
        "NO_COLOR_DROPDOWN": 0x0000200000000000,        # Prevents Color Panel Dropdown from being available. Popup color panel will stil be available.
        "NODEGRAPH_ONLY": 0x0000400000000000,           # Indicate that this knob should only be displayed when using the NodeGraph, since the Timeline uses gpuEngine, which might not support all the same knobs.
        "NO_SCRIPT_EXECUTE": 0x0000800000000000,        # Prevents 'execute' being called on the knob
        "MODIFIES_TIME": 0x0001000000000000,            # Should be set on all knobs which modify timing
        "TOOLBAR_BUTTON_DRAWSTYLE": 0x0002000000000000, # This knob must be drawn in the style of Viewer toolbar knobs
        "FLAGS_LOCKED": 0x0004000000000000,             # Used to lock modifications to this knobs flags
        "DO_NOT_READ": 0x0008000000000000,              # Skip reading the knob from script, must be set before loading from script Enumeration_Knob only
        "FROM_ASSET": 0x0010000000000000,               # This knob's value is supplied from an asset
        "RESERVED_NUMERIC_KNOB": 0x0020000000000000,    # DO NOT USE. This value is used by numeric knobs.
        
        
        # -----  Knob-specific Flags  ----------------------------------------------------------------------------------
        
        # Numeric knobs:
        "MAGNITUDE": 0x0000000000000001,                # Enables switchable numeric box & slider to multiple boxes (array knob derived numeric knobs).
        "SLIDER": 0x0000000000000002,                   # Enables slider on single numeric knob, or array knob with MAGNITUDE set (numeric knobs).
        "LOG_SLIDER": 0x0000000000000004,               # Switches linear slider to log slider, or cubic depending on range (numeric knobs with SLIDER).
        "STORE_INTEGER": 0x0000000000000008,            # Stores and presents integer value rather than float (numeric knobs).
        "FORCE_RANGE": 0x0000000000000010,              # Forces stored and presented value to be clamped to range set (numeric knobs).
        "ANGLE": 0x0000000000000020,                    # Switches widget for angle UI (single value numeric knobs).
        "NO_PROXYSCALE": 0x0000000000000040,            # Disables proxyscaling on knobs supporting it (XY_Knob & WH_Knob derivatives).
        "NO_PIXELASPECTSCALE": 0x0020000000000000,      # Disables pixel aspect scaling on knobs supporting it (XY_Knob & WH_Knob derivatives).
        
        # String Knobs
        "GRANULAR_UNDO": 0x0000000000000001,            # Disables concatenation of minor undo events (string knobs)
        "NO_RECURSIVE_PATHS": 0x0000000000000002,       # Badly named. Actually disables relative paths (string knobs).
        "NO_TCL_ERROR": 0x0000000000000004,             # For strings containing TCL expressions, don't replace with TCL error messages if an error occurs
        
        # Enumeration
        "SAVE_MENU": 0x0000000002000000,                # Forces menu entries to be written to script. Used by dynamic menus (enumeration knobs).
        "EXPAND_TO_CONTENTS": 0x0000000000000001,       # Make Enumeration knobs adjust their width to the size of the largest munu item.
        "EXACT_MATCH_ONLY": 0x0000000000000002,         # Make Enumeration knobs use exact match when setting a value. If an attempt is made to set an invalid value, the knob will be put into an Error state.
        "STRIP_CASCADE_PREFIX": 0x0000000000000004,     # Make Cascading Enumeration knobs not serialise out cascading prefixes
        
        # SceneView / Path knob
        "SINGLE_SELECTION_ONLY": 0x0000000000000001,    # Knob only allows one item to be selected at a time
        "SHOW_BUTTONS": 0x0000000000000002,             # Show Add Layer/Delete Layer buttons
        "SHOW_SCENE_PICK_BUTTON": 0x0000000000000008,   # Show Scene Graph Dialog button to choose Prim(s) from the Scene
        
        # BeginGroup
        "CLOSED": 0x0000000000000001,                   # Stores the open/closed state of group knobs (group knobs).
        "TOOLBAR_GROUP": 0x0000000000000002,            # Make the group into a viewer toolbar. General used via BeginToolbar (group knobs).
        "TOOLBAR_LEFT": 0x0000000000000000,             # Defines which side of viewer toolbar appears on. Pick one at toolbar construction time (toolbar).
        "TOOLBAR_TOP": 0x0000000000000010,              # Defines which side of viewer toolbar appears on. Pick one at toolbar construction time (toolbar).
        "TOOLBAR_BOTTOM": 0x0000000000000020,           # Defines which side of viewer toolbar appears on. Pick one at toolbar construction time (toolbar).
        "TOOLBAR_RIGHT": 0x0000000000000030,            # Defines which side of viewer toolbar appears on. Pick one at toolbar construction time (toolbar).
        "TOOLBAR_POSITION": 0x0000000000000030,         # A mask for the position part of the flags
        
        # ChannelSet/Channel:
        "NO_CHECKMARKS": 0x0000000000000001,            # Disable individual channel checkbox widgets (channel/channelset knobs).
        "NO_ALPHA_PULLDOWN": 0x0000000000000002,        # Disable 4th channel pulldown widget (channel/channelset knobs).
        "FULL_LAYER_ENABLED": 0x0000000000000004,       # channel/channelset knobs will always consider every channel in a layer to be enabled.
        "FORCE_RGBA_LAYER": 0x0000000000000008,         # Disables the layer selection dropdown. Forces the layer to always be RGBA.
        
        # Format knob
        "PROXY_DEFAULT": 0x0000000000000001,            # Sets default knob value from script proxy format rather than full res (format knob).
        
        # ColorChip knob
        "COLORCHIP_PRESERVE_ALPHA": 0x0000010000000000, # The ColorChip_knob discards alpha values by default. Set this flag to make it keep them, instead.
        
        # Colorspace Knob
        "ALLOW_NUKE_COLORSPACES": 0x0000000000000001,   # Allows the knob to display Nuke's native colorspaces if Color Management is set to Nuke.
        
        # Text knob
        "WORD_WRAP": 0x0000000000000001,                # Enable word wrapping-wrapping for the Text_knob
        
        # Eyedropper knob
        "CHECKED": 0x0000000000000001,                  # Tick checkbox in the ticker
    }
    
    # Convert to uppercase to help the user.
    flag_name = flag_name.upper()
    
    if flag_name in knob_flags_dict:
        return knob_flags_dict.get(flag_name)
    
    else:
        print(f"Could not find a flag named {flag_name}")

    return False

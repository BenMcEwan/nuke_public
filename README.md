<!--<a href="https://benmcewan.com"><img src="https://www.benmcewan.com/images/github_img/bm_logo.png"></a>

# nuke_public-->
<a href="https://www.benmcewan.com">Ben McEwan</a>'s Gizmos & Python Scripts for Nuke.

<!--
# Table of Contents

- [Gizmos](#gizmos)
  - [Breakdownerizationer](#breakdownerizationer)
  - [Cloudtastic](#cloudtastic)
  - [DeepMerge_Advanced](#deepmerge_advanced)
  - [bm_CameraShake](#bm_camerashake)
  - [bm_CurveRemapper](#bm_curveremapper)
  - [bm_EdgeMatte](#bm_edgematte)
  - [bm_OpticalLightwrap](#bm_opticallightwrap)
  - [bm_MatteCheck](#bm_mattecheck)
  - [bm_NoiseGen](#bm_noisegen)
  - [bm_OpticalGlow](#bm_opticalglow)
- [Python](#python)
  - [bm_AutoContactSheet.py](#bm_autocontactsheetpy)
  - [bm_CurveUtilities.py](#bm_curveutilitiespy)
  - [bm_DefaultBackdrop.py](#bm_DefaultBackdroppy)
  - [bm_EnableTrackerTRS.py](#bm_enabletrackertrspy)
  - [bm_JumpToKeyframe.py](#bm_jumptokeyframepy)
  - [bm_MultiIBK.py](#bm_multiibkpy)
  - [bm_NodeComment.py](#bm_nodecommentpy)
  - [bm_NodeSandwich.py](#bm_nodesandwichpy)
  - [bm_NukeColourConverter.py](#bm_nukecolourconverterpy)
  - [bm_OperationSwitcher.py](#bm_operationswitcherpy)
  - [bm_QuickKeys.py](#bm_quickkeyspy)
  - [bm_PulldownKnobCycler.py](#bm_PulldownKnobCyclerpy)
  - [bm_SmartMerge.py](#bm_smartmergepy)
  - [bm_ShuffleShortcuts.py](#bm_shuffleshortcutspy)
  - [bm_Smoothie.py](#bm_smoothiepy)
  - [bm_SwapInOut.py](#bm_swapinoutpy)
  - [bm_ViewerToggle.py](#bm_viewertogglepy)
  - [bm_netCopy.py](#bm_netcopypy)
<br>


# Gizmos

## Breakdownerizationer
A tool to automate the creation of simple breakdowns in Nuke. No bloated features, just does what it says on the tin.  

*Usage Notes:*
- Currently only supports pre-rendered layers.
- Breakdown types include:
  - Wipe Left-to-Right
  - Dissolve
  - Slide Layer In, Top-to-Bottom  

<a href="#"><img src="https://benmcewan.com/images/github_img/Breakdownerizationer_github.png"></a>

## Cloudtastic
A light-weight, element-based atmospheric fog box scriptlet.  

*Usage Notes:*
- See "Usage:" notes on CLOUDTASTIC_CONTROLS NoOp _(pictured below)_
- Expects atmospheric fog or cloud elements from your elements library.
- Trades off having heavy animated particles for randomly scattered sprites, which are frameheld for speed.
- ScanlineRender node outputs deep data so you can use in conjunction with deep renders, but please note:
  - If your camera flies through elements, they will pop on/off as the particles are just simple cards. Cloudtastic has a "kill area size" to prevent this, or you can use <a href="https://github.com/CreativeLyons/NukeSurvivalToolkit_publicRelease/blob/master/NukeSurvivalToolkit/NukepediaTools/12_Deep/NST_DeepCropSoft.gizmo">DeepCropSoft</a> to fade them on/off as they move closer.
  - If you have a deep render that moves through Cloudtastic's space, you may also see popping as it travels through the particles. As Cloudtastic is a light-weight hack, the best way to deal with this is to use a normalized depth pass (0 - 1 range), and mult it into the output render of Cloudtastic. While not 100% accurate, is it usually close enough when you need a quick solution!
  - If you need more accuracy, buy your FX department a beer to render true, deep volumetrics! :)  

<a href="#"><img src="https://benmcewan.com/images/github_img/Cloudtastic_github.png"></a>

## DeepMerge_Advanced
Like the DeepMerge node, with an option to soften the blend point.  

<a href="#"><img src="https://benmcewan.com/images/github_img/DeepMerge_Advanced_github.png"></a>

## bm_CameraShake
A replacement for Nuke's default camera shake node. Offers more control over 3 different frequencies of camera shake, and also shakes the centre-point, giving more detail to sub-frame motionblur. Also has options for how to deal with edge-of-frame pixels, so pushing-in isn't always your best option anymore!  

<a href="#"><img src="https://benmcewan.com/images/github_img/bm_CameraShake_github.png"></a>

## bm_CurveRemapper
Useful for remapping arbitrary animation curves, such as those from the CurveTool. Automatically detect an animation curve's min & max values, then remap them to new min & max values.  

<a href="#"><img src="https://benmcewan.com/images/github_img/bm_CurveRemapper_github.png"></a>

## bm_EdgeMatte
A simple gizmo to create an edge-outline from an existing rotoshape/matte.  
_(there are plenty of newer gizmos like this one with different features. If you have a better one, please let me know!)_  

<a href="#"><img src="https://benmcewan.com/images/github_img/bm_EdgeMatte_github.png"></a>

## bm_OpticalLightwrap
Like bm_OpticalGlow, this adds exponentially-increasing blurs together to produce a more optically-correct, natural lightwrap.  

<a href="#"><img src="https://benmcewan.com/images/github_img/bm_OpticalLightwrap_github.png"></a>

## bm_MatteCheck
A simple gizmo to help QC roto and keys, by overlaying a transparent colour, viewing a premultiplied image over grey or a checkerboard (for light and dark values).  

<a href="#"><img src="https://benmcewan.com/images/github_img/bm_MatteCheck_github.png"></a>

## bm_NoiseGen
Generates a random noise curve based on a minimum, maximum & frequency value.  

<a href="#"><img src="https://benmcewan.com/images/github_img/bm_NoiseGen_github.png"></a>

## bm_OpticalGlow
Adds exponentially-increasing blurs together to produce a more optically-correct, natural glow.  

<a href="#"><img src="https://benmcewan.com/images/github_img/bm_OpticalGlow_github.png"></a>


<br><br><br>


# Python

## bm_AutoContactSheet.py
Powers up Nuke's default contact sheet with features such as:
- Automatically lays out your images to maximize screen coverage, with no gaps.
- Automatically labels what each input is.
- Automatically sets its own resolution, based off your Project Settings' format.
- Adds a User knob for easy resolution scaling in case you want more detail, or more speed.
- Adds a few controls to adjust our automated text nodes.

<a href="https://benmcewan.com/blog/2018/08/26/power-up-your-contact-sheets/" target="_blank">Click here</a> for a tutorial on how I made this.  

## bm_DefaultBackdrop.py
Adds better backdrop node defaults & presets.
```ALT+B``` is the shortcut, or you can use the menu to grab a specific colour.

<a href="#"><img src="https://benmcewan.com/images/github_img/bmbackdrop.PNG"></a>

## bm_CurveUtilities.py
Adds some handy animation shortcuts to a knob's right-click menu:
- FrameHold animation.
- Set this frame as reference frame.
- Remap values between 0 and 1.

<a href="#"><img src="https://benmcewan.com/images/github_img/bm_CurveUtilities_github.png"></a>

## bm_EnableTrackerTRS.py
Adds a ```META+T``` hotkey to enable all T, R & S checkboxes in a selected Tracker node.  

## bm_JumpToKeyframe.py
Map ```Up``` and ```Down``` arrow keys to jump between next & previous keyframes.  

## bm_MultiIBK.py
Creates the usual IBK setup with 6 expression-linked IBKColour duplicates.  

## bm_NodeComment.py
Adds ```META+C``` shortcut to create a node's label, so you don't waste valuable clicks opening a node and switching to the Node label.  

## bm_NodeSandwich.py
Sandwiches selected node between two nodes (like an unpremult/premult, or lin2log/log2lin conversion).  
- ```CTRL+SHIFT+L``` creates a Log2Lin / Lin2Log sandwich.
- ```CTRL+SHIFT+P``` creates an Unpremult / Premult sandwich.

## bm_NukeColourConverter.py
Convert Nuke's hex colour to easier web-based hex, or RGB integer based off the colour sliders we're used to using in Nuke.  

## bm_OperationSwitcher.py
```CTRL+ALT+S``` toggles a Merge node's operation between over/under, mask/stencil, plus/from, etc.  

## bm_PulldownKnobCycler.py
```PGUP``` and ```PGDOWN``` cycles through operation and channels knobs on any selected node.

## bm_QuickKeys.py
Adds an easy way to set on/off keyframes on mix knobs & switch nodes.  
- ```META+,``` sets the current frame "on", and the previous frame "off".
- ```META+.``` sets the current frame "on", and the next frame "off".
- ```CTRL+META+,``` sets the current frame "on", and both the next & previous frames "off".
- ```CTRL+META+.``` sets the current frame "off", and both the next & previous frames "on".
- ```META+/``` opens a dialog box to manaully set a first frame, last frame, and a fade duration with values other than 0 or 1.

<a href="#"><img src="https://benmcewan.com/images/github_img/bm_QuickKeys_github.png"></a>

## bm_ShuffleShortcuts.py
Creates shuffle node shortcuts for shuffling a single channel to all other channels.  
_Note: Currently uses the old Shuffle node..._

## bm_SmartMerge.py
Upgrades Nuke's default ```m``` hotkey to be context-aware:
- If a set of 2D nodes & Deeps are selected, create DeepRecolor nodes.
  - If you have multiple sets of Reads & DeepReads selected, SmartMerge will hook the pairs up based on how similarly the filenames of the Reads & DeepReads are named.
- If only Deep nodes are selected, create a DeepMerge node.
- If a ScanlineRender node is selected, intelligently choose whether to Merge or DeepMerge depending on other nodes that are selected.
- If only 3D nodes are selected, create a Scene node.
- If only 2D nodes are selected, or if nothing is selected, create a vanilla Merge node as per usual.

<a href="#"><img src="https://benmcewan.com/images/github_img/bm_SmartMerge_github.gif"></a>

## bm_Smoothie.py
Easily smooth curves in Nuke's curve editor. Currently only supports single knobs _(e.g. multiply that hasn't been split into RGBA knobs, mix knobs, etc.)_.  
<a href="https://benmcewan.com/blog/2020/08/03/programmatically-editing-animation-curves-in-nuke/" target="_blank">Click here</a> to read a tutorial on how this was created, and how to programatically edit animation curves in Nuke.

<a href="#"><img src="https://benmcewan.com/images/github_img/bm_Smoothie_github.gif"></a>

## bm_SwapInOut.py
Easily fix scripts that use in & out, instead of mask & stencil.  
If you do this, <a href="https://conradolson.com/nuke-using-in-out-nodes" target="_blank">Conrad Olson's video</a> is required watching.

## bm_ViewerToggle.py
Adds `ALT+Q` shortcut to toggle viewer exposure & gamma between custom value and default.

## bm_netCopy.py
Share a selection of nodes with other users on the same network.  
Say goodbye to copy/pasting lines of text via IM or Email!
-->

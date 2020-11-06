# nuke_public
Ben McEwan's Gizmos & Python Scripts for Nuke.

- [nuke_public](#nuke-public)
- [Gizmos](#gizmos)
  * [Breakdownerizationer](#breakdownerizationer)
  * [Cloudtastic](#cloudtastic)
  * [DeepMerge_Advanced](#deepmerge_advanced)
  * [bm_CameraShake](#bm_camerashake)
  * [bm_CurveRemapper](#bm_curveremapper)
  * [bm_EdgeMatte](#bm_edgematte)
  * [bm_Lightwrap](#bm_lightwrap)
  * [bm_MatteCheck](#bm_mattecheck)
  * [bm_NoiseGen](#bm_noisegen)
  * [bm_OpticalGlow](#bm_opticalglow)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


# Gizmos

## Breakdownerizationer
A tool to automate the creation of simple breakdowns in Nuke. No bloated features, just does what it says on the tin.  
*Usage Notes:*
- Currently only supports pre-rendered layers.
- Breakdown types include:
  - Wipe Left-to-Right
  - Dissolve
  - Slide Layer In, Top-to-Bottom  

<a href="#"><img src="https://benmcewan.com/images/github/Breakdownerizationer.png"></a>

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

<a href="#"><img src="https://benmcewan.com/images/github/Cloudtastic.png"></a>

## DeepMerge_Advanced
Like the DeepMerge node, with an option to soften the blend point.  

<a href="#"><img src="https://benmcewan.com/images/github/DeepMerge_Advanced.png"></a>

## bm_CameraShake
A replacement for Nuke's default camera shake node. Offers more control over 3 different frequencies of camera shake, and also shakes the centre-point, giving more detail to sub-frame motionblur. Also has options for how to deal with edge-of-frame pixels, so pushing-in isn't always your best option anymore!  

<a href="#"><img src="https://benmcewan.com/images/github/bm_CameraShake.png"></a>

## bm_CurveRemapper
Useful for remapping arbitrary animation curves, such as those from the CurveTool. Automatically detect an animation curve's min & max values, then remap them to new min & max values.  

<a href="#"><img src="https://benmcewan.com/images/github/bm_CurveRemapper.png"></a>

## bm_EdgeMatte
A simple gizmo to create an edge-outline from an existing rotoshape/matte.  
_(there are plenty of newer gizmos like this one with different features. If you have a better one, please let me know!)_  

<a href="#"><img src="https://benmcewan.com/images/github/bm_EdgeMatte.png"></a>

## bm_Lightwrap
Like bm_OpticalGlow, this adds exponentially-increasing blurs together to produce a more optically-correct, natural lightwrap.  

<a href="#"><img src="https://benmcewan.com/images/github/bm_Lightwrap.png"></a>

## bm_MatteCheck
A simple gizmo to help QC roto and keys, by overlaying a transparent colour, viewing a premultiplied image over grey or a checkerboard (for light and dark values).  

<a href="#"><img src="https://benmcewan.com/images/github/bm_MatteCheck.png"></a>

## bm_NoiseGen
Generates a random noise curve based on a minimum, maximum & frequency value.  

<a href="#"><img src="https://benmcewan.com/images/github/bm_NoiseGen.png"></a>

## bm_OpticalGlow
Adds exponentially-increasing blurs together to produce a more optically-correct, natural glow.  

<a href="#"><img src="https://benmcewan.com/images/github/bm_OpticalGlow.png"></a>

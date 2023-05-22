#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: \modify1.py
# Created Date: Friday, August 12th 2022, 7:53:19 am
# Author: Christian Perwass (CR/AEC5)
# <LICENSE id="CC BY 4.0">

#   Image-Render Workspace 'simple'
#   Copyright 2022 Robert Bosch GmbH and its subsidiaries
  
#   This work is licensed under the 
  
#       Creative Commons Attribution 4.0 International License.
  
#   To view a copy of this license, visit 
#       http://creativecommons.org/licenses/by/4.0/ 
#   or send a letter to 
#       Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
  

# </LICENSE>
###

from pathlib import Path
pathFile = Path(__file__)

print("\n==============================================================================")
print(f"Evaluator Script '{pathFile.name}': START\n")

import bpy
import mathutils
import anyblend.viewlayer

print(f"__name__: {__name__}")
print(f"__file__: {__file__}")

if __name__ == "__main__":
    sTitle = "Test"
    sObject = "Object"
    lScale = [1, 1, 1]
    render = {}
# endif

print(f"sTitle: {sTitle}")
print(f"sObject: {sObject}")
print(f"lScale: {lScale}")

objX = bpy.data.objects.get(sObject)
if objX is None:
    raise RuntimeError(f"Object '{sObject}' not found")
# endif

# 'render' is a dictionary defined by the render script and passed
# to this script as a global variable
iTrgFrame = render["target-frame"]
lScale[1] *= iTrgFrame + 1

objX.scale = mathutils.Vector(lScale)

# Should call viewlayer update after modifying an object's location, euler angles or scale
# so that the world matrix is re-calculated.
anyblend.viewlayer.Update()

# This dictionary is the result of this evaluator script
dicResult = {
    "lPosition": list(objX.location)
}

print(f"\nEvaluator Script '{pathFile.name}': END")
print("==============================================================================\n")

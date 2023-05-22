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

# This if-block is only executed when the script is called directly in Blender.
# If this script is executed from a Catharsys modifier, the if-block is not
# executed.
if __name__ == "__main__":
    iSeed = 1
    sObject = "Test"
# endif

print(f"iSeed: {iSeed}")
print(f"sObject: {sObject}")

objX = bpy.data.objects.get(sObject)
if objX is None:
    raise RuntimeError(f"Object '{sObject}' not found")
# endif

fScale = iSeed * 0.5 + 1.0
objX.scale = (fScale, fScale, fScale)

print(f"\nEvaluator Script '{pathFile.name}': END")
print("==============================================================================\n")

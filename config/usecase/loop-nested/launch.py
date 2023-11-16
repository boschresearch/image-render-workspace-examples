#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: \launch.py
# Created Date: Tuesday, May 9th 2023, 8:26:14 am
# Author: Christian Perwass (CR/AEC5)
# <LICENSE id="CC BY 4.0">
#   #   Copyright 2022 Robert Bosch GmbH and its subsidiaries
#   This work is licensed under the
#       Creative Commons Attribution 4.0 International License.
#   To view a copy of this license, visit
#       http://creativecommons.org/licenses/by/4.0/
#   or send a letter to
#       Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
# </LICENSE>
###

# %% Load Workspace

# Load the Catharsys API module
import catharsys.api as capi

# Create a workspace object for the workspace this file is located in
wsX = capi.CWorkspace()
# Print information about this workspace
wsX.PrintInfo()


# %%
# Create the test configuration object
prjTest = wsX.Project("usecase/loop-randomize")
# Print the available actions
prjTest.PrintActions()

# %%
# Create an action object for the action 'render'
actRender = prjTest.Action("render")

# Get the job configuration. If the action has already been executed,
# this allows you to get the information on the result data location
# without re-executing the action.
jobRender = actRender.GetJobConfig()

# This job configuration data can also be saved and loaded
# jobRender.Save()

# %%
# Extract loop config info
dicCfg: dict
for iCfgIdx, dicCfg in enumerate(jobRender.lConfigs):
    dicData: dict = dicCfg["mConfig"]["mData"]
    lLoops: list = dicData["manifest/control/loop/*:1"]
    dicMod: dict = dicData["blender/modify:1"][0]
    # for iLoopIdx, dicLoop in enumerate(lLoops):
    #     dicGlobals: dict = dicLoop["__globals__"]
    #     sId = dicLoop["sId"]
    #     lVars = [f"{x} = {(dicGlobals.get(x))}" for x in dicGlobals if x.startswith("f")]
    #     sVars += ", " + ", ".join(lVars)
    # # endfor
    dicGlobals: dict = dicMod["__globals__"]
    lVars = [f"{x} = {(dicGlobals.get(x))}" for x in dicGlobals if x.startswith("f")]
    sVars = ", ".join(lVars)

    print(f"{iCfgIdx}: {sVars}")
# endfor

pass

# %%
# The launch function also return the job configuration
# jobRender = actRender.Launch(bPrintOutput=True)

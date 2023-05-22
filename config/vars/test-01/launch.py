#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: \launch.py
# Created Date: Friday, September 2nd 2022, 10:15:00 am
# Author: Christian Perwass (CR/AEC5)
# <LICENSE id="All-Rights-Reserved">
# Copyright (c) 2022 Robert Bosch GmbH and its subsidiaries
# </LICENSE>
###


# Load the Catharsys API module
import catharsys.api as capi

# Create a workspace object for the workspace this file is located in
wsX = capi.CWorkspace()
# Print information about this workspace
wsX.PrintInfo()

# Create the test configuration object
prjTest = wsX.Project("vars/test-01")
# Print the available actions
prjTest.PrintActions()

# Create an action object for the action 'render'
actRender = prjTest.Action("run")

# Get the job configuration. If the action has already been executed,
# this allows you to get the information on the result data location
# without re-executing the action.
jobRender = actRender.GetJobConfig()

# This job configuration data can also be saved and loaded
jobRender.Save()

# You can now open the saved json file, to see the content of the configuration variables.
# In the json file you find the processed "vars-01.json" under:
#   lConfigs -> mConfig -> mData -> "vars-test:1"

import json

# Write just the processed content of "vars-01.json" to a json file.
# Setting bStripVars = True, removes the local and global variables stored in the config.
dicVars = jobRender.ToDict(bStripVars=False)["lConfigs"][0]["mConfig"]["mData"]["vars-test:1"][0]
pathFile = prjTest._xPrjCfg.pathLaunch / "_proc-vars-01.json"

pathFile.write_text(json.dumps(dicVars, indent=4))

print("Processed 'vars-01.json' written to:\n{}".format(pathFile))

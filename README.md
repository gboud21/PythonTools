# PythonTools
This repository contains several tools created using python to perform process improvement tasks.

# Table of Contents
[Requirements Manager](#requirements-manager)

# Requirements Manager
## Purpose
This tool provides a way of taking a System Requirements Specification and using it to automatically update the requirement allocation in a Software Requirements Specification. While updating, it will also identify the following:
1) All System Requirements that have been changed since the last update
2) All new System Requirements that have been been added in update
3) All System Requirements that have been deleted in the update
4) All Software Requirements that have been orphaned by deleted System Requirements

## Inputs
- Configuration file that details the following:
    - The Path to the System Requirement Specification
    - The Path to the Software Requirements Specification
    - (Optional) The path to the output directory. The default path is the path to the Software Requirements Specification

## Outputs
- The Software Requirements Specification with the updated allocation to the System Requirements
- A file containing the following data:
    - A table with all the System Requirements that have been updated
    - A table with all the System Requirements that have been added
    - A table with all the System Requirements that have been deleted.
    - A table with all the Software Requirements that do not trace to a System Requirement
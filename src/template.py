#!/usr/bin/env python
# title:				template.py
# description:		Template for any programm
# author:			Authors seperated by comma
# license:			License for the programm
# date:				Date of creation
# version:			Versionnumber
# usage:				Description of how to use the programm quickly
# notes:				Notes for parameters, thanks (...)
# dependencies:		Preinstalled packages
# known_issues:		Known issues in this version
# python_version:	Compatible (tested) python version
# ==============================================================================

# IMPORTS

# Importing the time for benchmarking purposes
import time
from datetime import date

# CODE (FUNCTIONS)


# EXECUTION
if __name__ == '__main__':
    # Print welcoming message
    print("Hello world")

    # For benchmarking starting the timer now
    start_time = time.time()

    # Get parameters, call functions, execute program (...)

# BENCHMARKING [END]
sec = time.time() - start_time
print("The program took " + str(sec) + " seconds (" + str(sec/60) + " minutes) for execution.")

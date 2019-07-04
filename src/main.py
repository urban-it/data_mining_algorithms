#!/usr/bin/env python
# title:				main.py
# description:
# author:			Conrad Großer
# license:			https://github.com/tchemn/miner/blob/master/LICENSE
# date:				02.06.2018
# version:			0.1
# usage:				PENDING
# notes:
# dependencies:
# known_issues:
# python_version:	3.x
# ==============================================================================

# IMPORTS

# Importing the time for benchmarking purposes
import time

# CODE


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

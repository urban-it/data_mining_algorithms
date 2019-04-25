#!/usr/bin/env python
# title:              randomI2.1.py
# description:        Personal
# author:             Tillmann Brendel, Conrad Großer
# license:            Pending
# date:               26.05.2018
# version:            1.0
# usage:              python pyscript.py
# notes:
# known_issues:
# python_version:    3.x
# ==============================================================================

# For random generation of numbers import randint
from random import randint

# Importing the time for benchmarking purposes
import time
from datetime import date

# Importing for multi core processing
import multiprocessing


# randomI function which creates each file
def randomI(units, rows, rowLength, partstart, cluster):
    for setcounter in range(0, units):
        writeFile(generateFile(rows, rowLength, cluster), setcounter, partstart)
    return True


# Function for generating the content of one single file
def generateFile(rows, rowLength, cluster):
    content = []
    for entry in rows:
        if entry == 0:
            if randint(1, cluster) == 1:
                content.append(generate09())
            else:
                content.append(generatePLZ())
        else:
            content.append(generateRow(rowLength))
    return content


# Function for generating the content of one single row randomly
def generateRow(rowLength):
    row = ''
    for z in range(0, rowLength):
        row += str(randint(0, 9))
    return row


# Function for writing data into a file (content = string, setcount and partstart are for better naming)
def writeFile(content, setcounter, partstart):
    filenumber = int(setcounter) + int(partstart)
    file = open('testdata/file' + str(filenumber) + '.txt', 'w')

    for line in content:
        file.write(line + '\n')
    return True


if __name__ == '__main__':
    # Getting the user input
    print('Hello World')
    units = int(input('How many units would you like to generate? '))
    rows = int(input('How many rows should each unit have? '))
    rowLength = int(input('How long should each row be? '))
    cores = int(input('How many cores do you want to use? '))
    cluster = int(input('What fraction of postal codes should be in the 09xxx cluster? 1/'))

    # Splitting up the units
    count = 0
    partsize = units / cores

    # For benchmarking starting the timer now
    start_time = time.time()

    # Initialize and prepare cores for process
    while count < cores:
        partstart = partsize * count
        globals()['p' + str(count)] = multiprocessing.Process(
            target=randomI,
            args=(int(partsize), rows, rowLength, partstart, cluster)
            )
        count += 1

    # Starting each core
    count = int(0)
    while count < cores:
        globals()['p' + str(count)].start()
        print('Core ' + str(count) + ' started.')
        count += 1

    print('Working...')

    # Joining each core for the process
    count = 0
    while count < cores:
        globals()['p' + str(count)].join()
        count += 1

    # Finishing up the process
    sec = time.time() - start_time
    print('Data is generated. Have fun!')
    print('randomI took ' + str(sec) + ' seconds for execution.')

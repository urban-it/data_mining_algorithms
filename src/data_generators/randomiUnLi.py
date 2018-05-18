# Meet randomI, a random data generator for test data generation
from random import randint
import multiprocessing
import time
from datetime import date
from typing import Any, Union


def main(div, a, b, o):
    for x in range(0, int(div)):
        writeFile(generateFile(a, b), x, o)


def generateFile(rows, lenghtOfRows):
    content = []
    for y in range(0, rows):
        content.append(generateRow(lenghtOfRows))
    return content

def generateRow(lenghtOfRows):
    row = ""
    for z in range(0, lenghtOfRows):
        row = row + str(randint(0, 9))
    return row

def writeFile(content, x, o):
    file = open("testdata/file" + str(x+o) + ".txt", "w")
    for w in range(0, len(content)):
        file.write(content[w] + "\n")

if __name__ == '__main__':
    print("Hello World")
    i = int(input("How many units would you like to generate? "))
    a = int(input("How many rows should each unit have? "))
    b = int(input("How long should each row be? "))
    c = int(input("How many threads do you want to use?"))
    print('preparing')
    counter = int(0)
    div = i/c

    while counter < c:
        o = div * counter
        print('thread ' + str(counter) + ' set to start at ' + str(o))
        globals()["p" + str(counter)] = multiprocessing.Process(target=main, args=(div, a, b, o))
        counter = counter +1
    counter = int(0)
    start_time = time.time()
    print('starting')

    while counter < c:
        globals()["p" + str(counter)].start()
        print('thread number ' +str(counter) + ' just started')
        counter = counter + 1
    counter = int(0)

    while counter < c:
        globals()["p" + str(counter)].join()
        print('thread number ' + str(counter) + ' just finished')
        counter = counter + 1
    print('working, this might take a while')
    print("Data is generated. Have fun!")
    sec = time.time() - start_time
    minutes = sec / 60
    print("randomI took " + str(sec) + " seconds (" + str(minutes) + " minutes) for execution.")
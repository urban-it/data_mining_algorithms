# Meet randomI, a random data generator for test data generation
from random import randint
import multiprocessing
import time
from datetime import date


def main(i, a, b, o):
    print('go')
    for x in range(0, int(i)):
        content = generateFile(a, b)
        writeFile(content, x, o)


def generateFile(rows, lenghtOfRows):
    content = []
    for y in range(0, int(rows)):
        content.append(generateRow(int(lenghtOfRows)))
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
    q = input("How many datapieces would you like to generate? ")
    a = input("How many rows should each datapiece have? ")
    b = input("How long should each row be? ")
    start_time = time.time()
    q = int(q)
    i = q / 4
    o = 0
    print('preparing')
    p1 = multiprocessing.Process(target=main, args=(i, a, b, o))
    o = q / 4
    p2 = multiprocessing.Process(target=main, args=(i, a, b, o))
    o = q / 2
    p3 = multiprocessing.Process(target=main, args=(i, a, b, o))
    o = q / 2 + q / 4
    p4 = multiprocessing.Process(target=main, args=(i, a, b, o))
    print('starting')
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    print("Data is generated. Have fun!")
    sec = time.time() - start_time
    minutes = sec / 60
    print("randomI took " + str(sec) + " seconds (" + str(minutes) + " minutes) for execution.")

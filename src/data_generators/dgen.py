
from random import randint
def main():
    print('Hello world!')
def printer(r):
    r = r +(r - 1)
    return r
def rand (v, b):
    r = randint(v, b)
    return r
if __name__ == '__main__':
    main()
v = input ("von ")
b = input ("bis ")
v = int (v)
b = int(b)
r = 0
r = rand (v, b)
r = str(r)
print(r)


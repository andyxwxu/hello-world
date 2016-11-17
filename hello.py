#!/usr/bin/python

import sys


def Hello(name):
    if name == 'andyxu' or name == 'Andyxu':
        print('andyxu: andyxu mode')
        name = name + '???'
    else:
        DesNotExist(name)
    name = name + '!!!!!'
    print('hello', name)


def main():
    Hello(sys.argv[1])


if __name__ == "__main__":
    main()

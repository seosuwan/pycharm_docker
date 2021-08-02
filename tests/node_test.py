import sys
import math
import unittest


class Node(unittest.TestCase):


    width = 2  # the number of cells on the X axis
    height = 2
    cells = ['']# 높이
    for y in range(height):
        cells[y] = [''] #너비
        line = [0, 0]
        for x in range(width):
            cells[y][x] = line[x] #list 생성! >_<

    for y in range(height):
        print(cells[y],file=sys.stderr)



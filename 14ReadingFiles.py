# -*- coding: utf8 -*-

with open('a.txt') as f:
#w, h = [int(x) for x in next(f).split()] # read first line
    array = []
    for line in f: # read rest of lines
        array.append([int(x) for x in line.split()])

print(array)

with open('mazenospace.txt') as f:
#w, h = [int(x) for x in next(f).split()] # read first line
    maze = []
    for line in f: # read rest of lines
        maze.append([str(x) for x in line.split()])
print(maze)

# -*- coding: utf8 -*-

with open('a.txt') as f:
    a = []
    for line in f: # read rest of lines
        a.append([int(x) for x in line.split()])

with open('b.txt') as f:
    b = []
    for line in f: # read rest of lines
        b.append([int(x) for x in line.split()])
r=[]
for i in range(len(a)):
        r.append([a[i][j] + b[i][j] for j in range(len(a[i]))])
        
for i in range(len(r)):
    print(r[i])

"""
with open('a.txt') as f:
#w, h = [int(x) for x in next(f).split()] # read first line
    c = []
    for line in f: # read rest of lines
        for x in line.split():
            c.append(int(x))
print(c)
"""

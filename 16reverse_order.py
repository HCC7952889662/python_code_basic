# -*- coding: utf8 -*-

with open('text_in.txt') as f:
    txt = []
    for line in f: # read rest of lines
        txt.append([str(x) for x in line.split(" ")])
print(txt[0])

with open('text_out.txt', 'w') as fout:
    for p in range(len(txt)):
        for i in range(0, len(txt[p])):
            fout.write(txt[p][len(txt[p])-2-i])
            if(i < len(txt[p])-1):
                fout.write(" ")
            #print(txt[p][len(txt[p])-2-i], end = " ")
    

for p in range(len(txt)):
    for i in range(0, len(txt[p])):
        print(txt[p][len(txt[p])-2-i], end = " ")
    #print("\n")
    

"""
for i in range(0, len(txt[0])):
    print(txt[0][len(txt[0])-2-i], end = " ")
print("\n")
"""
"""
a = [0,1,2,3]
for i in range(0, 4):
    print(a[3-i], end = "")

"""


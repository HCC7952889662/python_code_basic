# -*- coding: utf8 -*-

#File Opening
with open('text_in.txt') as f:
    txt = [] #save in a list
    for line in f: # read rest of lines
        txt.append([str(x) for x in line.split(" ")])

with open('text_out3.txt', 'w') as fout:
    for p in range(len(txt)):
        for i in range(0, len(txt[p])-1):
            for j in range(0, len(txt[p][i])):
                encrypt = (ord(txt[p][i][j])-33+62)%94+33 #encrypting!
                fout.write(chr(encrypt))
            if(i < len(txt[p])-2):
                fout.write(" ")
            else:
                fout.write("\n")
"""
s = "The University of Southern California is a private research university in Los Angeles, California."
print(s[len(s)-1])
print(ord('l'))
for p in range(0, len(s)):
    encrypt = (ord(s[p])-33+24)%94+33
    if s[p] == ' ':
        print(end = " ")
    else:
        print((chr(encrypt)), end = "")
"""

"""

for p in range(len(txt)):
    for i in range(0, len(txt[p])):
        for j in range(0, len(txt[p][i])):
            encrypt = (ord(txt[p][i][j])-33+62)%94+33
            print(chr(encrypt), end = "")
        if(i < len(txt[p])-1):
            print(end = " ")
    #print("\n")
"""

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


# -*- coding: utf8 -*-


with open('text_in.txt') as f:
    txt = []
    for line in f: # read rest of lines
        txt.append([str(x) for x in line.split(" ")])
#print(txt)

  
h = {}
for p in range(len(txt)):
    for i in range(0, len(txt[p])-1):#prevent calculate '\n'
        #print(len(txt[p][i]))
        if len(txt[p][i]) in h:
            h[len(txt[p][i])] += 1
        else:
            h[len(txt[p][i])] = 1
#print(h)
print('Word Length {:<5} Count'.format(' '))
for i in sorted(h.keys()) :
    print('{:<18}{:<30}'.format(i,h[i]))

with open('text_out2.txt', 'w') as fout:
    fout.write('Word Length {:<5} Count'.format(' '))
    fout.write('\n')
    for i in sorted(h.keys()) :
        fout.write('{:<18}{:<30}'.format(i,h[i]))
        fout.write('\n')

"""
h = sorted(h.items(), key=lambda kv: kv[1])
print(h)
"""
"""
a = [0,1,2,3]
for i in range(0, 4):
    print(a[3-i], end = "")



with open('text_out.txt', 'w') as fout:
  for p in range(len(txt)):
      for i in range(0, len(txt[p])):
          fout.write(txt[p][len(txt[p])-2-i])
          fout.write(" ")
          #print(txt[p][len(txt[p])-2-i], end = " ")
"""

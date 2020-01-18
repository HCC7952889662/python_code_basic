#read files version2

f5 = open('test1.txt', "r")

line = f5.readlines()

x=len(line)
for i in range(x):
  print line[i]  

print line[1][4]
f5.close()


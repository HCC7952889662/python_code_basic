# -*- coding: utf8 -*-


with open('input.txt') as f:
#w, h = [int(x) for x in next(f).split()] # read first line
    maze = []
    for line in f: # read rest of lines
        maze.append([str(x) for x in line.split()])
print(maze)

count_list = []
count = 0
#Naive way
for i in range(len(maze)-1):#1st row
    for j in range(1,len(maze)):#2nd row
        for k in maze[i]:
            for l in maze[j]:
                if k == l:
                    count = count +1;
        count_list.append(count);
        count = 0;

print(max(count_list))

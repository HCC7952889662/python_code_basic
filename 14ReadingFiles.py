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


"""
with open('candyshop_dataset.txt') as f:
    for line in f: # read rest of lines
        k = line.split(',')
        population.append(float(k[0]))
        profit.append(float(k[1]))

#print(population[96])
#print(profit[96])
plt.figure()
ori = sns.scatterplot(x=population,y=profit, color = "green")
plt.xlabel('Population')
plt.ylabel('Profit')
plt.show()
"""

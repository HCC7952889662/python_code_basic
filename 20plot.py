import matplotlib.pyplot as plt
import numpy as np
import math
import random

# import seaborn
import seaborn as sns
sns.set(color_codes=True,style="white")
# settings for seaborn plot sizes
sns.set(rc={'figure.figsize':(10,10)})


def ecdf(data):
    """ Compute ECDF """
    x = np.sort(data)
    n = x.size
    y = np.arange(1, n+1) / n
    return(x,y)
class norml_plt:
    def __init__(self, ran):
        self.mu = np.mean(ran)
        self.sigma = np.std(ran)
        self.size = len(ran)
        self.ran = ran
    def curve(self, color):
        #n, bins, patches = plt.hist(self.ran, int(self.size/resolution_bits), density = 1)
        sns.distplot(self.ran, (1 / (np.sqrt(2 * np.pi) * self.sigma)) *
            np.exp( - (self.ran - self.mu)**2 / (2 * self.sigma**2) ), color= color, hist= False)
    #plt.show()

plt.figure()
plt.subplot2grid((2, 2), (0, 0), colspan=2)

mu1 = 0
sigma1 = 5
size1 = 1000
#x = np.random.normal(mu1, sigma1, size1)
x = sigma1 * np.random.randn(size1) + mu1
#print(x)
p1 = norml_plt(x)
plt.subplot2grid((2, 2), (0, 0))
p1.curve('g')

mu2 = 0
sigma2 = 5
size2 = 1000
#y = np.random.normal(mu2, sigma2, size2)
y = sigma2 * np.random.randn(size2) + mu2
#print(y)
p2 = norml_plt(y)

p2.curve('r')


z = np.convolve(x,y)
print(z)
pr = norml_plt(z)
plt.subplot2grid((2, 2), (0, 1))
#pr.curve('b')
sns.distplot(z, hist=False, color = "black");

plt.subplot2grid((2, 2), (1, 0))
(datax, cdfx) = ecdf(x)
plt.plot(datax, cdfx, color = "green")
(datay, cdfy) = ecdf(y)
plt.subplot2grid((2, 2), (1, 1))
a= plt.plot(datay, cdfy, color = "black")
plt.xlabel('Input:Green/Red, Output:Black')

(dataz, cdfz) = ecdf(z)
"""
plt.subplot2grid((2, 2), (1, 1))
(dataz, cdfz) = ecdf(z)
plt.plot(dataz, cdfz, color = "blue")
"""

"""
p1 = norml_plt(x)
p1.curve('b')
"""
x.sort()
y.sort()
px=[]
for k in x:
    px.append((1 / (np.sqrt(2 * np.pi) * sigma1)) * np.exp( - (k - mu1)**2 / (2 * sigma1**2)))
py=[]
for k in y:
    py.append((1 / (np.sqrt(2 * np.pi) * sigma2)) * np.exp( - (k - mu2)**2 / (2 * sigma2**2)))

z=[]
zpdf=[]


def max(A, B):
    YPDF = 0
    YCDF = 0
    XPDF = 0
    XCDF = 0
    for i in range (size1-1):
        z.append(x[i])
        for j in range (size2-1):
            if(z[i]>=y[j]):
                YCDF = cdfy[j]
                YPDF = py[j]
        if(z[i]>x[size1-1]):
            YPDF = 0
            YCDF = 1
        elif(z[i]<x[0]):
            YPDF = 0
            YCDF = 0
        zpdf.append(cdfx[i]*YPDF+YCDF*px[i])

    for i in range (size2-1):
        temp = y[i]
        if(temp<[x[0]]):
            i = i
        else:
            z.append(y[i])
            for j in range (size1-1):
                if(temp>=x[j]):
                    XCDF = cdfx[j]
                    XPDF = px[j]
            if(temp>x[size1-1]):
                XPDF = 0
                XCDF = 1
            zpdf.append(XCDF*py[i]+cdfy[i]*XPDF)
    #g = sns.lineplot(x=z, y=zpdf, color = "red")
    #print("The mean of maximum between A and B is: ", np.mean(z))


max(x,y)
#sns.lineplot(x=z, y=zpdf, color = "blue")
plt.show()

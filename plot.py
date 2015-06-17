from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from string import maketrans
f = open('vector.txt')
myDict = {} #define a dictionary
index=0
x=[]
y=[]
z=[]
intab = "()"
outtab = "  "
trantab = maketrans(intab, outtab)
for lines in f:
    myDict[index] = lines.translate(trantab).strip().split(", ") #
    index+=1
for i in myDict:
    x.append(float(myDict[i][0])) # append every point into list
    y.append(float(myDict[i][1]))
    z.append(float(myDict[i][2]))
fig = plt.figure() #set a default Panel
ax = fig.gca(projection='3d') # set the Panel default 3D
ax.plot(x, y, z) # draw lines point by point
plt.show() # show all we draw
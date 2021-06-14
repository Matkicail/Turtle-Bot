import numpy as np
from skimage import io 
from skimage import morphology
from skimage.morphology import disk
from matplotlib import pyplot as plt
import csv

map = io.imread("cleanImage.pgm",as_gray = True)
blankMap = np.zeros(map.shape)
setOfPoints = np.array([]).astype(np.int64)
maxDistance = 45
f = open('poi.txt', 'r+')
f.truncate(0)
f.close()
f = open("poi.txt","a")

for i in range(0,map.shape[0],maxDistance):
    for j in range(0,map.shape[1],maxDistance):
        xNoise = np.random.randint(-1,1,size=1)[0]
        yNoise = np.random.randint(-1,1,size=1)[0]
        if map[i+xNoise][j+yNoise] == 255:
            blankMap[i+xNoise][j+yNoise] = 1
            text = "["+str(i+xNoise) + "," + str(j+yNoise) + "],\n"
            f.write(text)

blankMap = morphology.binary_dilation(blankMap, selem = disk(3))
plt.imshow(blankMap, cmap = plt.cm.gray)
plt.show()
visualMap = np.zeros((map.shape[0], map.shape[1], 3))
print(visualMap.shape)
for i in range(visualMap.shape[0]):
    for j in range(visualMap.shape[1]):
        for p in range(3):
            if map[i][j] != 0:
                visualMap[i][j][0] = 255
                visualMap[i][j][1] = 255
                visualMap[i][j][2] = 255
                if blankMap[i][j] != 0:
                    visualMap[i][j][1] = 0
                    visualMap[i][j][2] = 0

plt.imshow(visualMap)
plt.ylabel("Y-cord")
plt.xlabel("X-cord")
plt.axhline(y = 340, color = 'b', linestyle = '-')
plt.axvline(x = 260, color = 'b', linestyle = '-')
for i in range(0,map.shape[0],25):
    for j in range(0,map.shape[1],25):
        plt.axhline(y = i, color = 'g', linestyle = 'dotted')
        plt.axvline(x = j, color = 'g', linestyle = 'dotted')
plt.show()
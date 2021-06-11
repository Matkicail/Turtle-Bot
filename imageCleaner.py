import numpy as np
from skimage import io 
from skimage import morphology
from skimage.morphology import disk
from matplotlib import pyplot as plt



image = io.imread("map.png",as_gray=True)
#Get all places where we are certain we can move
indicesWhite = np.where(image == image.max())
#Make a zero map
binaryImage = np.zeros(image.shape)
#colour places that we can move to in the map
binaryImage[indicesWhite] = 1

#just shows the binary map even though quite messy
# plt.imshow(binaryImage, cmap=plt.cm.gray)
# plt.show()

#labels the image
labeled = morphology.label(binaryImage, connectivity=1)

# Find the label that you would like to keep in this plot and set that to be the value for the next line
# plt.imshow(labeled, cmap=plt.cm.gray)
# plt.show()

indicesWhite = np.where(labeled == 1)

#turn the rest black basically
binaryImage = np.zeros(binaryImage.shape)
binaryImage[indicesWhite] = 1

#smooth the image heavily
binaryImage = morphology.binary_opening(binaryImage, selem=disk(13))
#increase object size
binaryImage = morphology.binary_erosion(binaryImage, selem=disk(13))
#Display
plt.imshow(binaryImage, cmap=plt.cm.gray)
plt.show()

#me just being pedantic to ensure that the floating white spot goes away
labeled = morphology.label(binaryImage, connectivity=1)
plt.imshow(labeled, cmap=plt.cm.gray)
plt.show()
indicesBlack = np.where(labeled == 2)
binaryImage[indicesBlack] = 0

#invert the image and now we will colour missing parts
indicesWhite = np.where(binaryImage == 0)
invertedImage = np.zeros(binaryImage.shape)
invertedImage[indicesWhite] = 1

#label again to find labels we want to make nonzero
labeled = morphology.label(invertedImage, connectivity=1)
plt.imshow(labeled, cmap=plt.cm.gray)
plt.show()
indicesBlack = np.where(labeled == 2)
labeled[indicesBlack] = 0
indicesBlack = np.where(labeled == 8)
labeled[indicesBlack] = 0
plt.imshow(labeled, cmap=plt.cm.gray)
plt.show()

#invert this back
indicesWhite = np.where(labeled ==0)
binaryImage = np.zeros(labeled.shape)
binaryImage[indicesWhite] = 1
labeled = morphology.label(binaryImage, connectivity=1)
plt.imshow(labeled, cmap=plt.cm.gray)
plt.show()
indicesWhite = np.where(labeled == 1)
binaryImage = np.zeros(binaryImage.shape)
binaryImage[indicesWhite] = 1

io.imsave("cleanImage.pgm",binaryImage)
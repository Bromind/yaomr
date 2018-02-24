# Standard imports
import cv2
import numpy as np;
from sys import argv
import os
import sys

def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts

name_file="full_page"
myargs = getopts(argv)
if '-i' in myargs:  # Example usage.
    print(myargs['-i'])
    name_file=myargs['-i']

script_dir=os.path.dirname(__file__)
if(script_dir == ""):
    script_dir="."
file_path= script_dir + "/../assets/" + name_file + ".png"
print(file_path)
# Read image
im_orig = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
cv2.imshow("smoothed", im_orig)

# Gaussian blur 
kernel = np.ones((15,15),np.float32)/225
smoothed = cv2.filter2D(im_orig,-1,kernel)

#Blob detection 

im = smoothed
_, im = cv2.threshold(im, 230, 255, cv2.THRESH_BINARY)

im = 255 - im; 
im = 255 - cv2.erode(im, np.ones((3,3)), iterations=6)
im = (255-im)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Filter by Area.
# Change thresholds
params.minThreshold = 200;
params.maxThreshold = 50000;
 
# Filter by Area.
params.filterByArea = True
params.minArea = 10
 
# Filter by Circularity
params.filterByCircularity = False
params.minCircularity = 0.1
 
# Filter by Convexity
params.filterByConvexity = False
 
# Filter by Inertia
params.filterByInertia =False
params.minInertiaRatio = 0.5

# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
    detector = cv2.SimpleBlobDetector(params)
else : 
    detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs.
im = 255 - im; 

height = np.size(im, 0)
width = np.size(im, 1)

keypoints = detector.detect(im)
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Draw blobs
sorted_point_x=[]
tmp=list(keypoints)
for i in range(len(keypoints)):
    smallest = tmp[0]
    for j in range(len(tmp)):
        if(tmp[j].pt[1] < smallest.pt[1]):
            smallest = tmp[j]
    sorted_point_x.append(smallest)
    if tmp:
        tmp.remove(smallest)

for keyPoint in sorted_point_x:
    x1 = keyPoint.pt[0]
    y1 = keyPoint.pt[1]
    s = keyPoint.size
    print(" x " + str(x1) + " y " + str(y1) + " s " + str(s))


#cv2.imwrite("treble_staff2.jpg", crop_img)
cv2.imwrite("treble_staff.jpg", im_with_keypoints)

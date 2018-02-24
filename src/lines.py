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

# Gaussian blur 
kernel = np.ones((15,15),np.float32)/225
smoothed = cv2.filter2D(im_orig,-1,kernel)

#Blob detection 

im = smoothed
_, im = cv2.threshold(im, 230, 255, cv2.THRESH_BINARY)
cv2.imshow("smoothed", im)

im = 255 - im; 
im = 255 - cv2.erode(im, np.ones((3,3)), iterations=6)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Filter by Area.
params.filterByArea = False
params.filterByInertia = False
params.filterByConvexity = False
params.filterByCircularity = False

# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
    detector = cv2.SimpleBlobDetector(params)
else : 
    detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs.
im = 255 - im; 
cv2.imshow("im", im)
keypoints = detector.detect(im)

# Draw blobs
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

for keyPoint in keypoints:
    x = keyPoint.pt[0]
    y = keyPoint.pt[1]
    s = keyPoint.size
    print(" x " + str(x) + " y " + str(y))


# Show blobs
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey();


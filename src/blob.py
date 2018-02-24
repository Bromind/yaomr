# Standard imports
import cv2
import numpy as np;
from sys import argv
import os
import sys
from operator import itemgetter
from create_part import create_part

def sec_elem(s):
    return s[1]

def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts

window_width = 20
immune = 10

name_file="blob_notes"
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
im = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

im_orig = im

_, im = cv2.threshold(im, 128, 255, cv2.THRESH_BINARY)

im = 255 - im; 
im = 255 - cv2.erode(im, np.ones((3,3)), iterations=2)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Filter by Area.
params.filterByArea = True
params.minArea = 10

params.filterByConvexity = False

# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
    detector = cv2.SimpleBlobDetector(params)
else : 
    detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs.
keypoints = detector.detect(im)

# Draw blobs
im_with_keypoints = cv2.drawKeypoints(im_orig, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

sorted_point_x=[]
tmp=list(keypoints)
for i in range(len(keypoints)):
    smallest = tmp[0]
    for j in range(len(tmp)):
        if(tmp[j].pt[0] < smallest.pt[0]):
            smallest = tmp[j]
    sorted_point_x.append(smallest)
    if tmp:
        tmp.remove(smallest)

print("d")

im2 = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
k = 0
list_filename = []
for keyPoint in sorted_point_x:
    k = k + 1 
    x1 = keyPoint.pt[0]
    y1 = keyPoint.pt[1]
    s = keyPoint.size
    crop_y = 140
    crop_x = 5
    crop_img = im2[int(y1)-crop_y:int(y1)+crop_y, int(x1)-crop_x:int(x1)+crop_x + 4]
    filename = script_dir + "/../assets/" + name_file + str(k) + ".png"
    cv2.imwrite(filename, crop_img);
    list_filename.append(filename)
    print(" x " + str(x1) + " y " + str(y1) + " s " + str(s) + " at " + filename)

create_part(list_filename)

# Process the blobs in order

#Write image
#cv2.imwrite("treble_staff.jpg", im_with_keypoints)

# Show blobs
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey();


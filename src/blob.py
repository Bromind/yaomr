# Standard imports
import cv2
import numpy as np;

# Read image
im = cv2.imread("blob.png", cv2.IMREAD_GRAYSCALE) 
im_orig = im

_, im = cv2.threshold(im, 128, 255, cv2.THRESH_BINARY)

im = 255 - im; 
im = 255 - cv2.erode(im, np.ones((3,3)), iterations=2)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Filter by Area.
params.filterByArea = True
params.minArea = 20

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

#Write image
cv2.imwrite("treble_staff.jpg", im_with_keypoints)

# Show blobs
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)

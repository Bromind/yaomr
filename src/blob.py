# Standard imports
import cv2
import numpy as np;
from sys import argv
import os
import sys
import note
from operator import itemgetter

def sec_elem(s):
    return s[1]

def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts

def blob_detection(im2, name_file):

    script_dir=os.path.dirname(__file__)
    if(script_dir == ""):
        script_dir="."

    myargs = getopts(argv)
    if '-i' in myargs:  # Example usage.
        print(myargs['-i'])
        name_file=myargs['-i']

    # Read image from given argument: im
    im = im2

    # First Threshold
    threshold_1 = 128
    #Second Threshold after erode
    threshold_2 = 64
    # Number of time we erode:
    # the more we erode the more it diffuse
    erode_iteration=1
    # Number of pixel the round should be to be detected
    min_blob_area=1
    #Matrix to erode
    erode_np = 3
    # If the image is too small; increase this
    # Height
    crop_y = 140
    # Width
    crop_x = 5
    
    # Keep the old image to print the detected blobs
    im_orig = im

    _, im = cv2.threshold(im, threshold_1 , 255, cv2.THRESH_BINARY)

    # Invert the image
    im = 255 - im; 
    im = 255 - cv2.erode(im, np.ones((erode_np,erode_np)), iterations=erode_iteration)

    _, im = cv2.threshold(im, threshold_2, 255, cv2.THRESH_BINARY)

    # Setup SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()

    # Filter by Area.
    params.filterByArea = True
    params.minArea = min_blob_area

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
    im_with_keypoints = cv2.drawKeypoints(im_orig,
                                          keypoints, 
                                          np.array([]), 
                                          (0,0,255), 
                                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

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

    k = 0
    list_path=[]
    for keyPoint in sorted_point_x:
        k = k + 1 
        x1 = keyPoint.pt[0]
        y1 = keyPoint.pt[1]
        s = keyPoint.size
        print(" x " + str(x1) + " y " + str(y1) + " s " + str(s))
        crop_img = im2[int(y1)-crop_y:int(y1)+crop_y, int(x1)-crop_x:int(x1)+crop_x + 4]
        file_name_note=script_dir + "/../assets/" + name_file + "_note_" + str(k).zfill(2) + ".png"
        cv2.imwrite(file_name_note, crop_img);
        list_path.append(file_name_note)

    return list_path
    # Process the blobs in order
    # Show blobs
    #cv2.imshow("Keypoints", im_with_keypoints)
    #cv2.imshow("Keypointsf", im)
    #cv2.waitKey();


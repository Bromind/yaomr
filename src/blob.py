# Standard imports
import cv2
import numpy as np;
from sys import argv
import os
import sys
import note
from param import *
from operator import itemgetter

windows_name='debugKeypoints'

def nothing(x):
    pass

def sec_elem(s):
	return s[1]

def getopts(argv):
	opts = {}  # Empty dictionary to store key-value pairs.
	while argv:  # While there are arguments left to parse...
		if argv[0][0] == '-':  # Found a "-name value" pair.
			opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
		argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
	return opts

def blob_detection(im2, name_file, path_folder_out):

	# Read image from given argument: im
	# First Threshold
	threshold_1 = 145
	#Second Threshold after erode
	threshold_2 = 0
	# Number of pixel the round should be to be detected
	# a small number will make the blob detector find more blobs
	min_blob_area=10
	max_blob_area=100
	# Number of time we erode:
	# the more we erode the more it diffuse
	erode_iteration=2
	#Matrix to erode
	erode_np = 3

	dilate_iteration=1
	#Matrix to erode
	dilate_np = 1
	# If the image is too small; increase this
	# Height
	crop_y = 100
	# Width
	crop_x = 15
	# Window: number of pixels before accepting a new blob
	window=10
	# invert image
	invert=1
	# Black circles will be taken into account for blob

	# Keep the old image to print the detected blobs
	im_orig = im2


	# Show blobs
	#cv2.imshow("debugKeypointsf", im)
	if blobgui :
		cv2.namedWindow(windows_name)
		cv2.createTrackbar('threshold_1',windows_name,threshold_1,255,nothing)
		cv2.createTrackbar('threshold_2',windows_name,0,255,nothing)
		cv2.createTrackbar('min_blob_area',windows_name,min_blob_area,255,nothing)
		cv2.createTrackbar('max_blob_area',windows_name,max_blob_area,255,nothing)
		cv2.createTrackbar('erode_iteration',windows_name,erode_iteration,10,nothing)
		cv2.createTrackbar('window',windows_name,window,100,nothing)
		cv2.createTrackbar('crop_y',windows_name,crop_y,200,nothing)
		cv2.createTrackbar('crop_x',windows_name,crop_x,200,nothing)
		cv2.createTrackbar('invert',windows_name,invert,1,nothing)
		cv2.createTrackbar('switch',windows_name,0,1,nothing)
		cv2.createTrackbar('erode_np',windows_name,2,8,nothing)

		cv2.createTrackbar('dilate_np',windows_name,2,8,nothing)
		cv2.createTrackbar('dilate_iteration',windows_name,1,8,nothing)

	switch_image = 0

	_, im = cv2.threshold(im2, threshold_1 , 255, cv2.THRESH_BINARY)
	# Invert the image
	if invert:
		im = 255 - im;
	if erode_iteration > 0:
		im = 255 - cv2.erode(im, np.ones((erode_np,erode_np)), iterations=erode_iteration)
	if threshold_2 > 0:
		_, im = cv2.threshold(im, threshold_2, 255, cv2.THRESH_BINARY)
	if dilate_iteration > 0:
		im = cv2.dilate(im,np.ones((dilate_np,dilate_np),np.uint8),iterations = dilate_iteration)

	# Setup SimpleBlobDetector parameters.
	params = cv2.SimpleBlobDetector_Params()

	# Filter by Area.
	params.filterByArea = True
	params.minArea = min_blob_area
	params.maxArea = max_blob_area

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


	while(blobgui):

		_, im = cv2.threshold(im2, threshold_1 , 255, cv2.THRESH_BINARY)

		#im = cv2.GaussianBlur(im,(1,1),0)

		# Invert the image
		if invert:
			im = 255 - im;
		if erode_iteration > 0:
			im = 255 - cv2.erode(im, np.ones((erode_np,erode_np)), iterations=erode_iteration)
		if threshold_2 > 0:
			_, im = cv2.threshold(im, threshold_2, 255, cv2.THRESH_BINARY)
		if dilate_iteration > 0:
			im = cv2.dilate(im,np.ones((dilate_np,dilate_np),np.uint8),iterations = dilate_iteration)


		# Setup SimpleBlobDetector parameters.
		params = cv2.SimpleBlobDetector_Params()

		# Filter by Area.
		params.filterByArea = True
		params.minArea = min_blob_area
		params.maxArea = max_blob_area
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

		im2_with_keypoints = cv2.drawKeypoints(im,
											  keypoints,
											  np.array([]),
											  (0,0,255),
											  cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

		threshold_1 = cv2.getTrackbarPos('threshold_1', windows_name)
	   	threshold_2 = cv2.getTrackbarPos('threshold_2', windows_name)
		min_blob_area = cv2.getTrackbarPos('min_blob_area', windows_name)
		max_blob_area = cv2.getTrackbarPos('max_blob_area', windows_name)
		erode_iteration = cv2.getTrackbarPos('erode_iteration', windows_name)
		crop_y = cv2.getTrackbarPos('crop_y', windows_name)
		crop_x = cv2.getTrackbarPos('crop_x', windows_name)
		window = cv2.getTrackbarPos('window', windows_name)
		invert = cv2.getTrackbarPos('invert', windows_name)
		erode_np = cv2.getTrackbarPos('erode_np', windows_name)

		dilate_np = cv2.getTrackbarPos('dilate_np', windows_name)
		dilate_iteration = cv2.getTrackbarPos('dilate_iteration', windows_name)

		switch_image = cv2.getTrackbarPos('switch_image', windows_name)

		#im_out = im_with_keypoints
		im_out = im2_with_keypoints
		#if switch_image:
		#	im_out = im_with_keypoints
		#else:
		#	im_out = im
		#im_out = im

		old_x1 = -window
		#height, width, channels = im_out.shape
		for keyPoint in keypoints:
			x1 = keyPoint.pt[0]
			y1 = keyPoint.pt[1]
			s = keyPoint.size
			#print(" " + str(int(x1)) + " " + str(old_x1) + " " + str(window))
			#if (int(x1) - old_x1) > window:
			cv2.rectangle(im_out,	(int(x1) - crop_x/2, int(y1) - crop_y/2),
									(int(x1) + crop_x/2, int(y1) + crop_y/2),
									(0,255,0), 1)
			old_x1 = int(x1)

		cv2.imshow(windows_name, im_out)

		k = cv2.waitKey(1) & 0xFF
		# Escape character
		if k == 27:
			# Exit windows when it is done
			cv2.destroyWindow(windows_name)
			break

	#cv2.destroyAllWindows()

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

	old_x1 = -window
	height, width = im2.shape[:2]

	for keyPoint in sorted_point_x:
		k = k + 1
		x1 = keyPoint.pt[0]
		y1 = keyPoint.pt[1]
		s = keyPoint.size
		print(" " + str(int(x1)) + " " + str(old_x1) + " " + str(window))
		if (int(x1) - old_x1) > window:
			x_min=int(x1-crop_x/2)
			if(x_min < 0):
				x_min = 0

			x_max=int(x1+crop_x/2)

			print(" x " + str(x1) + " " + str(x_min) + " " + str(x_max) + " y " + str(y1) + " s " + str(s))
			crop_img = im2[0:height, x_min:x_max]
			file_name_note=path_folder_out + "/" + name_file + "_note_" + str(k).zfill(2) + ".png"
			cv2.imwrite(file_name_note, crop_img);
			list_path.append(file_name_note)
			print file_name_note
		old_x1 = int(x1)

	# Process the blobs in order
	return list_path


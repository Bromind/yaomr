# Standard imports
import param
import cv2
import numpy as np;
from sys import argv
import os
import sys
from create_part import create_part
from blob import blob_detection
from create_part import create_part
from os.path import basename

def getopts(argv):
	opts = {}  # Empty dictionary to store key-value pairs.
	while argv:  # While there are arguments left to parse...
		if argv[0][0] == '-':  # Found a "-name value" pair.
			opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
		argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
	return opts

def separate_lines():

	print param.outdir
	print param.infile
	path_folder_out=param.outdir
	if not os.path.exists(path_folder_out):
		os.makedirs(path_folder_out)
	else:
		for f in os.listdir(path_folder_out):
			file_path = os.path.join(path_folder_out, f)
			try:
				if os.path.isfile(file_path):
					os.unlink(file_path)
			except Exception as e:
				print(e)

	print("Folder out: " + path_folder_out)

	file_path= param.infile
	print("Input file: " + file_path)
	name_file=basename(file_path)
	print(name_file)

	# Read image
	im_orig = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
	im_modified = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
	black_sum_thresh = 100

	# Gaussian blur
	kernel = np.ones((15,15),np.float32)/225
	smoothed = cv2.filter2D(im_modified,-1,kernel)

	#Line detection
	im = smoothed
	_, im = cv2.threshold(im, 240, 255, cv2.THRESH_BINARY)



	rows, cols = im.shape
	print str(rows) + " " + str(cols)
	sums = {}
	for i in range(rows):
		black_sum = 0
		for j in range(cols):
			if im[i, j] == 255:
				black_sum = black_sum + 1
		sums[i] = black_sum

	prev_line = sums[0]
	splits = []
	end_low = 0
	for i in sums:
		if sums[i] < black_sum_thresh and prev_line >= black_sum_thresh:
			split = ((i - end_low) / 2) +end_low
			splits.append(split)
		if sums[i] >= black_sum_thresh and prev_line < black_sum_thresh:
			end_low = i
		prev_line = sums[i]

	prev_split = rows

	if len(splits) == 0:
		notes = blob_detection(im_orig, name_file[:-4] + "_line_00", path_folder_out)
		create_part(notes, name_file)
	else:
		r = range(len(splits), 0, -1)
		k = len(r)
		notes = []
		for i in r:
			k = k - 1
			end_y = prev_split
			begin_y = splits[i-1]
			begin_x = 0
			end_x = cols
			splitted = im_orig[begin_y:end_y, begin_x:end_x]
			begining = blob_detection(splitted, name_file[:-4] + "_line_" + str(i-1).zfill(2), path_folder_out)
			begining.extend(notes)
			notes = begining
			#cv2.imwrite("../assets/" + name_file + "_line_" + str(i-1) + ".png", splitted)
			prev_split = splits[i-1]

		create_part(notes, name_file)

		#cv2.imwrite("treble_staff2.jpg", crop_img)
		#cv2.waitKey();

### USAGE
### run in default
# python main.py
### To run with configs, enter the command below
# python main.py --type "type of input file: 0 for image, 1 for video" --input "path to input folder" --template "path to template image" --threshold "threshold value"
# E.g. python main.py --type 0 --input images --template templates/logo_template.jpg --threshold 0.7

import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse
import os

ap = argparse.ArgumentParser()
ap.add_argument("-t", "--type", type=int, default=0,
	help="type of input file: 0 for image, 1 for video")
ap.add_argument("-i", "--input", type=str, default="images",
	help="path to input folder")
ap.add_argument("-temp", "--template", type=str, default="templates/logo_template.jpg",
	help="path to template image")
ap.add_argument("-th", "--threshold", type=float, default=0.82,
	help="threshold value")
args = vars(ap.parse_args())

threshold = args["threshold"]
template = cv2.imread(args["template"], 0)
source = args["input"]

if args["type"] == 0:
	print("Press Q Key to quit")
	for file in os.listdir(source):
		imgDir = source + "/" + file
		img = cv2.imread(imgDir)
		img_cpy = img.copy()
		img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		height, width= template.shape

		# Applying template matching; Minimum value is the point where the image matches best
		res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

		min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
		# print(min_val, max_val, min_loc, max_loc)

		top_left = max_loc
		bottom_right = (top_left[0] + width, top_left[1] + height)
		if max_val >= threshold:
			print("No defects detected.")
			cv2.rectangle(img, top_left, bottom_right, (0, 0, 255), 2)
		else:
			print("Defects detected.")
		# print(top_left[0], bottom_right[0], top_left[1], bottom_right[1])
		cropped_img = img[top_left[1]: bottom_right[1], top_left[0]: bottom_right[0], 0]
		masked_img = cropped_img - template

		# cv2.imshow("Template image", template)
		cv2.imshow("Gray image", img)
		# cv2.imshow("Cropped image", cropped_img)
		cv2.imshow("Masked image", masked_img)
		# cv2.imshow("Contour image", img_cpy)
		key = cv2.waitKey()
		# if the `q` key was pressed, break from the loop
		if key == ord("q"):
			print("Quitting...")
			break
	cv2.destroyAllWindows()

elif args["type"] == 1:
	defect_detected = True
	print("Press Q Key to quit")
	cap = cv2.VideoCapture(source)
	while(cap.isOpened()):
		ret, img = cap.read()
		if ret == True:
			img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			height, width= template.shape

			# Applying template matching; Minimum value is the point where the image matches best
			res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

			min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
			# print(min_val, max_val, min_loc, max_loc)

			top_left = max_loc
			bottom_right = (top_left[0] + width, top_left[1] + height)
			if max_val >= threshold:
				if defect_detected == True:
					print("No defects detected.")
					defect_detected = False
				cv2.rectangle(img, top_left, bottom_right, (0, 0, 255), 2)
			else:
				if defect_detected == False:
					print("Defects detected.")
					defect_detected = True
			cv2.imshow("Gray image", img)
			key = cv2.waitKey(10) 
			if key == ord('q'):
				break
	cap.release()
	cv2.destroyAllWindows()


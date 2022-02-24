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
import glob
import API_call
import time

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

url = "http://127.0.0.1:8000/detections/"
detection_result = "0"

# serial_no = 0
serial_no = API_call.get_last_serial_no(url)

def process_image(imgDir, serial_no):
	img = cv2.imread(imgDir)
	img_h, img_w, _ = img.shape
	img_cpy = img.copy()
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	height, width = template.shape

	# Applying template matching; Minimum value is the point where the image matches best
	res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
	# print(min_val, max_val, min_loc, max_loc)

	top_left = max_loc
	bottom_right = (top_left[0] + width, top_left[1] + height)
	if max_val >= threshold:
		print("No defects detected.")
		detection_result = "OK"
		cv2.rectangle(img, top_left, bottom_right, (0, 0, 255), 2)
	else:
		print("Defects detected.")
		detection_result = "Defective"
	# print(top_left[0], bottom_right[0], top_left[1], bottom_right[1])
	cropped_img = img[top_left[1]: bottom_right[1], top_left[0]: bottom_right[0], 0]
	masked_img = cropped_img - template
	masked_img_cpy = cv2.resize(masked_img, (img_w, img_h), interpolation = cv2.INTER_AREA)

	serial_no += 1
	response = API_call.upload_to_server(img_cpy, img, serial_no, detection_result, url)
	print(response)

	# cv2.imshow("Template image", template)
	# cv2.imshow("Output image", img)
	# cv2.imshow("Cropped image", cropped_img)
	# cv2.imshow("Masked image", masked_img)
	# cv2.imshow("Original image", img_cpy)
	# key = cv2.waitKey()
	return serial_no

first_loop_done = False
last_img_dir = "0"
last_img_time = 0

if args["type"] == 0:
	while True:
		# print("Press Q Key to quit")
		if first_loop_done == True:
			files = glob.glob(source + "/*")
			latest_img_dir = max(files, key=os.path.getctime)
			if last_img_dir == latest_img_dir:
				time.sleep(4)
				continue
			else:
				print("Processing new image ...", latest_img_dir)
				serial_no = process_image(latest_img_dir, serial_no)
				last_img_dir = latest_img_dir
		else:
			for file in os.listdir(source):
				imgDir = source + "/" + file
				latest_img_time = os.path.getctime(imgDir)
				if last_img_time < latest_img_time:
					last_img_time = latest_img_time
					last_img_dir = imgDir
				serial_no = process_image(imgDir, serial_no)
		first_loop_done = True
		# break
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


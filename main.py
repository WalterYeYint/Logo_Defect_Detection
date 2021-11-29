import cv2
import numpy as np
from matplotlib import pyplot as plt


# img = cv2.imread('images/vlcsnap-2021-11-29-19h51m36s119.jpg')


# img = cv2.imread('images/zoomed.jpg')
# img = cv2.imread('images/gaussian-blurred.jpg')
# img = cv2.imread('images/oil_paint.jpg')
# img = cv2.imread('images/broken.jpg')
# img = cv2.imread('images/rotated.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread('images/logo_template.jpg', 0)
height, width= template.shape
threshold = 0.82

# res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
# loc = np.where(res >= threshold)


# for pt in zip(*loc[::-1]):
# 	cv2.rectangle(img, pt, (pt[0] + width, pt[1] + height), (0,0,255), 2)


# Applying template matching; Minimum value is the point where the image matches best
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
print(min_val, max_val, min_loc, max_loc)

top_left = max_loc
bottom_right = (top_left[0] + width, top_left[1] + height)
if max_val >= threshold:
	cv2.rectangle(img, top_left, bottom_right, (0, 0, 255), 2)

cv2.imshow("Gray image", img)
cv2.waitKey()
cv2.destroyAllWindows()
import os
import time
import glob
from xml.etree.ElementPath import xpath_tokenizer_re

latest_img_time = 0

# files = []
# for file in os.listdir("img warehouse"):
# 	imgDir = "img warehouse" + "/" + file
# 	files.append(imgDir)

# files = glob.glob("img warehouse/*")
# x = max(files, key=os.path.getctime)
# print(x)

# for file in os.listdir("img warehouse"):
	
# 	imgDir = "img warehouse" + "/" + file
# 	img_time.append(os.path.getctime(imgDir))
# print("Before sorting = ", img_time)
# img_time = sorted(img_time)
# print("After sorting = ", img_time)
# 	print(file, img_time)
# 	if img_time > latest_img_time:
# 		latest_img_time = img_time
# time.sleep(5)


from datetime import datetime

x = datetime.now()
date = x.strftime("%Y")+'-'+x.strftime("%m")+'-'+x.strftime("%d")+' '+x.strftime("%H")+':'+x.strftime("%M")+':'+x.strftime("%S")
date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

print(x)



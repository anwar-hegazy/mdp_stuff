#!/usr/bin/env python2.7

import cv
from threading import Thread
import time
import datetime
import os

#checks date and time
x = datetime.datetime.now()
x = str(x)
x = x.replace(' ', '_')
folder_name = '/Users/cta/test/' + str(x) +'/'

#makes a new folder, named by datetime, in the directory
os.makedirs( str(folder_name))

#sets up isight
cv.NamedWindow("w1", cv.CV_WINDOW_AUTOSIZE)
camera_index = 0

#take a photo every n seconds object
def take_photo(n):
	num = 0
	while True:
		#take photo here
#		print('Hello world...')
		capture = cv.CaptureFromCAM(camera_index)
		frame = cv.QueryFrame(capture)
		num = num + 1
		cv.SaveImage(str(folder_name) + 'pic_'+ str(num) + '.jpg', frame)
		print('just took photo number ' + str(num) +'!')
		time.sleep(n)

#take the photo, set n seconds
t = Thread(target = take_photo, args =(15,))
t.run()
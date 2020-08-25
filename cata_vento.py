import os
import time
import pyfirmata
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

direction = 0
val = 0.0
oldval = 0.0
board = pyfirmata.Arduino('/dev/cu.usbmodem14201')
it = pyfirmata.util.Iterator(board)
it.start()
potentiometer = board.analog[2]
potentiometer.enable_reporting()
driver = webdriver.Chrome("")
time.sleep(3)
while True:
	try:
		val = round(potentiometer.read(), 2)
		# maybe round it up or down
		time.sleep(0.1)
		if val != oldval:
			if val <= 1.0 and val >= 0.783:
				direction = 0
			if val <= 0.783 and val >= 0.420:
				direction = 1
			if val <= 0.420 and val >= 0.079:
				direction = 2
			if val <= 0.079 and val >= 0:
				direction = 3
		if direction != old_direction:
			if direction == 0:
				print("moving north toward dublin")
				driver.get("https://www.earthcam.com/world/ireland/dublin/?cam=templebar")
			if direction == 1:
				print("moving west toward aruba")
				driver.get("https://www.earthcam.com/world/aruba/druifbeach/?cam=casadelmar")
			if direction == 2:
				print("moving south toward jerusalem")
				driver.get("https://www.earthcam.com/world/israel/jerusalem/?cam=jerusalem")
			if direction == 3:
				print("moving east toward madrid")
				driver.get("https://www.youtube.com/watch?v=JN1ZpDra91s&feature=emb_title")
		oldval = val
		old_direction = direction
	except:
		print("didn't work")

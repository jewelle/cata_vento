import os
import time
import pyfirmata
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("")
board = pyfirmata.Arduino('/dev/ttyACM0')

it = pyfirmata.util.Iterator(board)
it.start()

analog_input = board.get_pin('a:2:i')

while True:
	val = analog_input.read() # read the value from the sensor
    if val <= 1023 && val >= 938:
        cout << "moving north toward dublin"
        driver.get("https://www.earthcam.com/world/ireland/dublin/?cam=templebar")
    if val <= 937 && val >= 605:
    	cout << "moving west toward aruba"  
    	driver.get("https://www.earthcam.com/world/aruba/druifbeach/?cam=casadelmar")
  	if val <= 604 && val >= 215:
    	cout << "moving south toward jerusalem"
    	driver.get("https://www.earthcam.com/world/israel/jerusalem/?cam=jerusalem")
  	if val <= 214 && val >= 0:
    	cout << "moving east toward madrid"
    	driver.get("https://www.youtube.com/watch?v=JN1ZpDra91s&feature=emb_title")

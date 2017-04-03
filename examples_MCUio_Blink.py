#!/usr/bin/python

# Codeing By IOXhop : www.ioxhop.com
# Sonthaya Nongnuch : www.fb.me/maxthai


import time
import IOXhop_MUCio as mcu

def main():
	mcu.begin(0x08)
	
	mcu.mode(13, mcu.OUTPUT)
	while True:
		mcu.set(13, mcu.HIGH) # Set pin 13 to logic 1 (HIGH)
		time.sleep(0.5)
		mcu.set(13, mcu.LOW) # Set pin 13 to logic 0 (LOW)
		time.sleep(0.5)

if __name__ == '__main__':
	main()
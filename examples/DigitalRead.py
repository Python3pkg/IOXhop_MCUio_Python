#!/usr/bin/python

# Codeing By IOXhop : www.ioxhop.com
# Sonthaya Nongnuch : www.fb.me/maxthai


import time
import IOXhop_MCUio as mcu

def main():
	mcu.begin(0x08)
	
	mcu.mode(2, mcu.INPUT)
	while True:
		value = mcu.get(2) # Read digital value from pin 2
		print(value) # Send value to Console
		time.sleep(0.5)

if __name__ == '__main__':
	main()
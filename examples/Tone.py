#!/usr/bin/python

# Codeing By IOXhop : www.ioxhop.com
# Sonthaya Nongnuch : www.fb.me/maxthai


import time
import IOXhop_MCUio as mcu

def main():
	mcu.begin(0x08)
	
	mcu.mode(9, mcu.OUTPUT)
	while True:
		mcu.tone(9, 2000) # Send sound 2KHz to pin 2
		time.sleep(1)
		mcu.Dtone(9) # Cancel send sound to pin 2
		time.sleep(1)

if __name__ == '__main__':
	main()
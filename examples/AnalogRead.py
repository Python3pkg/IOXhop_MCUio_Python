#!/usr/bin/python

# Codeing By IOXhop : www.ioxhop.com
# Sonthaya Nongnuch : www.fb.me/maxthai


import time
import IOXhop_MCUio as mcu

def main():
	mcu.begin(0x08)
	
	while True:
		value = mcu.Aget(mcu.A0)
		print value
		time.sleep(0.5)

if __name__ == '__main__':
	main()
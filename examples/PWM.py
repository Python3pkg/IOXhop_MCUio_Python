#!/usr/bin/python

# Codeing By IOXhop : www.ioxhop.com
# Sonthaya Nongnuch : www.fb.me/maxthai


import time
import IOXhop_MCUio as mcu

def main():
	mcu.begin(0x08)
	
	mcu.mode(9, mcu.OUTPUT)
	while True:
		value = mcu.Aget(mcu.A0) # Read analog value from A0
		pulse_width = value * 255 / 1023 # Resolution resize
		mcu.pwm(9, pulse_width) # Use pin 9 in PWM mode
		time.sleep(0.01)

if __name__ == '__main__':
	main()
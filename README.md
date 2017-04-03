# IOXhop_MCUio Library for Python
## English

### Install
you can install via pip

    pip install IOXhop_MCUio

 
### Last test
 * Raspberry Pi zero
 
### License
This library open source. Copied, distributed for free
 * http://www.ioxhop.com/

## ภาษาไทย
ไลบารี่นี้ใช้สำหรับทำให้บอร์ด Arduino หรือไมโครคอนโทรลเลอร์เป็นอุปกรณ์ขยายพอร์ต เหมาะสำหรับใช้กับไมโครคอมพิวเตอร์ที่มีพอร์ตการเชื่อมต่อน้อย

### การ Setup บอร์ด

ให้อัพโหลด Sketch ลงบอร์ดให้ตรงชิป เช่น Arduino Uno R3 ใช้ชิป ATmega328 ก็ให้อัพโหลด Sketch ของ ATmega328 โดยใช้โปรแกรม Arduino ในการคอมไพล์และอัพโหลด

### การต่อวงจร

ให้ต่อขา SCL และ SDA ให้ตรงกัน ระหว่างบอร์ด Arduino ที่นำมาใช้เป็นตัวขยายพอร์ต กับบอร์ดที่นำมาใช้เป็นตัวสั่งงาน

### การติดตั้งไลบารี่
สามารถติดตั้งได้โดยใช้ pip

    pip install IOXhop_MCUio

### อุปกรณ์ที่ทดสอบแล้ว
 * Raspberry Pi zero

### ตัวอย่าง

Blink.py

```python
#!/usr/bin/python

# Codeing By IOXhop : www.ioxhop.com
# Sonthaya Nongnuch : www.fb.me/maxthai


import time
import IOXhop_MCUio as mcu

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
```

DigitalRead.py

```python
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
		print value # Send value to Console
		time.sleep(0.5)

if __name__ == '__main__':
	main()
```

AnalogRead.py

```python
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
```

PWM.py

```python
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
```

Tone.py

```python
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
```

### รายละเอียดฟังก์ชั่น

#### begin(devAddr, ch = 0) ;

**ค่าพารามิเตอร์**

*(int) devAddr* - ตำแหน่งของอุปกรณ์บนบัส I2C หากไม่แก้โค้ดใน Sketch จะมีค่าเป็น 0x08

*(int) ch* - หมายเลขช่องของ I2C


**ค่าส่งกลับ**

ไม่มี

####mode(pin, mode)

ใช้ตั้งโหมดของขา GPIO ให้เป็นอินพุต หรือเอาต์พุต

**ค่าพารามิเตอร์**

*pin* - หมายเลขขา เช่น ขา 13 สามารถใส่ตัวเลขได้เลย แต่หากเป็นชื่อขา ให้ใส่ชื่อออปเจคที่สร้างไว้ข้างหน้า เช่น ขา A0 จะต้องใส่ mcu.A0

*mode* - โหมดของขา สามารถเป็นไปได้ดังนี้

 * INPUT - ตั้งให้ขามีสถานะเป็นอินพุต
 * OUTPUT - ตั้งให้ขามีสถานะเป็นเอาต์พุต

**ค่าส่งกลับ**

ไม่มี

#### set(pin, lavel)

ใช้เขียนค่าแบบดิจิตอลออกขา GPIO (ต้องเรียกคำสั่งตั้งโหมดให้ขาที่ต้องการเป็น OUTPUT ก่อนด้วย)

**ค่าพารามิเตอร์**

*pin* - หมายเลขขา

*lavel* - สถานะทางลอจิกที่ต้องการ สามารถเป็นไปได้ดังนี้

 * HIGH - ตั้งให้ขามีสถานะทางดิจิตอลเป็นลอจิก 1 (HIGH)
 * LOW - ตั้งให้ขามีสถานะทางดิจิตอลเป็นลอจิก 0 (LOW)

**ค่าส่งกลับ**

ไม่มี


#### get(pin)

ใช้อ่านสถานะแบบดิจิตอลที่ขา GPIO (ต้องเรียกคำสั่งตั้งโหมดให้ขาที่ต้องการเป็น INPUT ก่อนด้วย)

**ค่าพารามิเตอร์**

*pin* - หมายเลขขา

**ค่าส่งกลับ**

เป็นไปได้ดังนี้

 * ให้ค่า 1 เมื่อสถานะที่อ่านได้คือ HIGH
  * ให้ค่า 0 เมื่อสถานะที่อ่านได้เป็น LOW

#### Aget(pin)

ใช้อ่านสถานะแบบอนาล็อกที่ขา GPIO โดยมีความละเอียด 10 บิต หรือ 0 - 1023 (รอรับเฉพาะขา A0 - A3)

**ค่าพารามิเตอร์**

*pin* - หมายเลขขา (รอรับเฉพาะขา A0 - A3)

**ค่าส่งกลับ**

ค่าที่ได้จะอยู่ในช่วง 0 - 1023 ที่แรงดันอ้างอิงเท่าแรงดัน VCC

#### pwm(pin, value)

เลือกใช้เอาต์พุตแบบ PWM ออกที่ขาดิจิตอล 3 5 6 10 และ 11

**ค่าพารามิเตอร์**

*pin* - หมายเลขขา (รอรับเฉพาะขา 3 5 6 10 และ 11)

*value* - ความกว้างพัลส์ที่ต้องการ ความละเอียด 8 บิต หรืออยู่ในช่วง 0 - 255 โดยที่ 255 คือ 100%

**ค่าส่งกลับ**

ไม่มี

#### tone(pin, frequency)

ส่งสัญญาณเสียงความถี่ที่กำหนดออกที่ขา GPIO

**ค่าพารามิเตอร์**

*pin* - หมายเลขขา

*frequency* - ความถี่เสียงที่ต้องการ (สำหรับบัสเซอร์ แนะนำ 2000 หรือ 2KHz จะใช้เสียงดังที่สุด)

**ค่าส่งกลับ**

ไม่มี

#### Dtone(pin)

ยกเลิกการส่งสัญญาณเสียงออกที่ขา GPIO

**ค่าพารามิเตอร์**

*pin* - หมายเลขขา

**ค่าส่งกลับ**

ไม่มี

### ลิขสิทธิ์การใช้งาน
ผู้จัดทำอนุญาตให้นำไปใช้งาน และแจกจ่ายได้โดยคงไว้ซึ่งที่มาของเนื้อหา ห้ามมีให้นำไปใช้งานในเชิงพาณีย์โดยตรง เช่น การนำไปจำหน่าย
 * http://www.ioxhop.com/
 

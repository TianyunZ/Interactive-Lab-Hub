import board
import busio
import adafruit_apds9960.apds9960
import time
import sys
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)

sensor.enable_proximity = True
flg = 0
while flg < 10:
	prox = sensor.proximity
	flg += 1
	print(prox)
	if prox >= 20:
		sys.exit(20)
	time.sleep(0.2)
sys.exit(0)
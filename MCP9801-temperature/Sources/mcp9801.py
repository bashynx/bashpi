#!/usr/bin/python

import smbus
import time
from subprocess import call

bus = smbus.SMBus(1)
address = 0x4f

def bearing():
	data = bus.read_i2c_block_data(address, 0, 2)
	temp = data[0] + ( data[1] / ( 256.0 ) )
	return temp

data = bus.write_byte_data(address, 1, 0x50)
data = bus.write_byte_data(address, 0, 0x0)

while True:
        bears = bearing()
        print bears
        time.sleep(1)

#!/usr/bin/python
import smbus
import time
from subprocess import call

bus = smbus.SMBus(1)
address = 0x6b

x = 0x28
y = 0x2a
z = 0x2c

def sig(x):
        if (x >> 15) == 1:
                x = x - 0xffff - 1
        return (x * ( ( ( 2**15 ) - 1 ) ** (-1) )* ( 2 ) )

def bearing(var):
        data = bus.read_i2c_block_data(address, var, 2)
        temp = ( data[1] << 8) + ( data[0] )
        return temp

data = bus.write_byte_data(address, 0x20, 0xc0)
data = bus.write_byte_data(address, 0x10, 0xc0)

print bus.read_byte_data(address, 0x10)

while True:
        nux = bearing(x)
        nuy = bearing(y)
        nuz = bearing(z)

        print 'x:', sig(nux), ' y:', sig(nuy), ' z:', sig(nuz)
        time.sleep(0.01)


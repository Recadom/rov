import smbus
import time
import pygame

bus = smbus.SMBus(1)

address = 0x04


def writeNumber(value):
	bus.write_byte(address, value)
	# bus.write_byte_data(address, 0, value)
	return -1

def readNumber():
	number = bus.read_byte(address)
	number = bus.read_byte_data(address, 1)
	return number

    
while True:
##    print(readNumber())
    k = input()
    writeNumber(int(k))
    
##time.sleep(1)

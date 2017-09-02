import smbus
import time
import pygame


# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x04

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

print (joystick.get_name)

def writeNumber(value):
	bus.write_byte(address, value)
	# bus.write_byte_data(address, 0, value)
	return -1

def readNumber():
	number = bus.read_byte(address)
	number = bus.read_byte_data(address, 1)
	return number

while True:
        try:
                pygame.event.pump()
                for x in range (0, 4):
                        var = int(joystick.get_axis(x) * 14 + 15 + x * 30)
                        #if var < 128 and var >= 0:
                        writeNumber(var)
        except:
                print('error!')
                


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

print joystick.get_name

def writeNumber(value):
	bus.write_byte(address, value)
	# bus.write_byte_data(address, 0, value)
	return -1

def readNumber():
	number = bus.read_byte(address)
	# number = bus.read_byte_data(address, 1)
	return number

while True:
	pygame.event.pump()
#	print joystick.get_axis(1)
	for x in range (0, 4):
		var = int(joystick.get_axis(x) * 14 + 15 + x * 30)
		#if var < 128 and var >= 0:
		writeNumber(var)
		time.sleep(0.03)
	var = int(joystick.get_hat(0)[0] + 120)
	writeNumber(var)
	time.sleep(0.03)
	
#		print "sent ", var
#		sleep one second
#		time.sleep(0.05)
#		
#		number = readNumber()
#		print "received  ", number
 #		print
#	var = int(joystick.get_axis(3))


import smbus
import time
import pygame
import sys


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
	bus.write_byte(address, int(value))
	# bus.write_byte_data(address, 0, value)
	return -1

def readNumber():
	number = bus.read_byte(address)
	number = bus.read_byte_data(address, 1)
	return number
##Setup
end = True
axis_forward_back = 1
axis_left_right = 0
axis_up_down = 2
axis_twist = 3
while True:
        try:
                pygame.event.pump()
                for x in range (0, 3):
                        var = int(joystick.get_axis(x) * 14 + 15 + x * 30)
                        writeNumber(var)
##                        print(var)
                        time.sleep(0.01)
                
                if end == True:
                        end = False
                        print('Working!')

        except IOError as err:
                end = True
                time.sleep(0.5)
                print (err)
        

        except KeyboardInterrupt: pass




                
		
"""
                forwLeft = joystick.get_axis(axis_forward_back) * 63 + 64

                writeNumber(forwLeft)
                time.sleep(0.01)
                
                writeNumber(0)
                time.sleep(0.01)

                forwRight = joystick.get_axis(axis_forward_back) * 63 + 64
                writeNumber(forwRight)
                time.sleep(0.01)

                vertLeft = joystick.get_axis(axis_up_down) * 63 + 64
                writeNumber(vertLeft)
                time.sleep(0.01)
		
                vertRight = joystick.get_axis(axis_up_down) * 63 + 64
                writeNumber(vertRight)
                time.sleep(0.01)

                writeNumber(0)
                time.sleep(0.01)
"""

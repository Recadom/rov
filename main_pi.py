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

def current_check(m_1, m_2, m_3, m_4):
        value = abs(m_1) + abs(m_2) + abs(m_3) + abs(m_4)
        if value > 2:
                e_1 = m_1 * 0.75 ** ((value-2)/2)
                e_2 = m_2 * 0.75 ** ((value-2)/2)
                e_3 = m_3 * 0.75 ** ((value-2)/2)
                e_4 = m_4 * 0.75 ** ((value-2)/2)
                return e_1,e_2,e_3,e_4
        else:
                return m_1, m_2, m_3, m_4

def writeNumber(value):
        value = int(value)
	bus.write_byte(address, value)
	# bus.write_byte_data(address, 0, value)
	return -1

def readNumber():
	number = bus.read_byte(address)
	number = bus.read_byte_data(address, 1)
	return number
##Setup
err_time = 0
end = True
axis_forward_back = 1
axis_left_right = 0
axis_up_down = 2
axis_twist = 3
t_wait = 0.01

while True:
        try:
                
                pygame.event.pump()
                m_1, m_2, m_3, m_4 = current_check(joystick.get_axis(axis_forward_back),joystick.get_axis(axis_left_right),joystick.get_axis(axis_up_down),joystick.get_axis(axis_up_down))

                forwLeft = (m_1 + m_2/2) * 63 + 64
                forwRight = (m_1 - m_2/2) * 63 + 64
                if (m_1 + m_2/2) > 1:
                        forwLeft = 1 * 63 + 64

                if (m_1 + m_2/2) < -1:
                        forwLeft = -1 * 63 + 64

                if (m_1 - m_2/2) > 1:
                        forwRight = 1 * 63 + 64
                        
                if (m_1 - m_2/2) < -1:
                        forwRight = -1 * 63 + 64
                
                vertLeft = m_3 * 63 + 64
                vertRight = m_4 * 63 + 64

                #print(forwLeft, forwRight, vertLeft, vertRight)
                
                writeNumber(forwLeft)
                time.sleep(t_wait)
                
                writeNumber(forwRight)
                time.sleep(t_wait)
                
                writeNumber(vertLeft)
                time.sleep(t_wait)
                
                writeNumber(vertRight)
                time.sleep(t_wait)
                
                writeNumber(0)
                time.sleep(t_wait)
                
        
                #print(str(int(forwLeft)) + "\t" + str(int(forwLeft)) + "\t" + str(int(vertLeft)) + "\t" + str(int(vertRight)))

                
                if end == True:
                        end = False
                        print('Working!')

        except IOError as err:
                end = True
                time.sleep(0.2)
                err_time +=1
                #subprocess.call(['i2cdetect', '-y', '1'])
                print (str(err) + ', ' + str(err_time))
        

        except KeyboardInterrupt: break



print ('')
                
		
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

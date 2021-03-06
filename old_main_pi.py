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

print(joystick.get_name)

'''def claw_conv(claw_state, count):
        time = count * 0.1 #.06 S
        value = 0.4 / (10 * time + 1) + 0.4 # .33 MIN * .66
        count += 1
        
        if (claw_state > 0):
                value = 1 * value
                
        elif (claw_state < 0):
                value = -1 * value
                
        elif claw_state == 0:
                count = 0
                value = 0
        
        return int(value * 63 + 64), count
'''

def current_check(m_1, m_2, m_3, m_4):
        value = abs(m_1) + abs(m_2) + abs(m_3) * 2
        if value > 2000:
                e_1 = m_1 * 0.75 ** ((value-2)/2)
                e_2 = m_2 * 0.75 ** ((value-2)/2)
                e_3 = m_3 * 0.75 ** ((value-2)/2)
                e_4 = m_4 #* 0.75 ** ((value-2)/2)
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
count = 0

while True:
        try: # m_4 is claw
                
                pygame.event.pump()
                m_1, m_2, m_3, m_4 = current_check(joystick.get_axis(axis_forward_back),joystick.get_axis(axis_left_right),joystick.get_axis(axis_up_down),joystick.get_axis(axis_twist))
                m_5 = joystick.get_hat(0)

                forwLeft = (m_1 + m_2/2) * 50 + 64
                forwRight = (m_1 - m_2/2) * 50 + 64
                if (m_1 + m_2/2) > 1:
                        forwLeft = 1 * 50 + 64

                if (m_1 + m_2/2) < -1:
                        forwLeft = -1 * 50 + 64

                if (m_1 - m_2/2) > 1:
                        forwRight = 1 * 50 + 64
                        
                if (m_1 - m_2/2) < -1:
                        forwRight = -1 * 63 + 64
                
                vertLeft = m_3 * 50 + 64
                vertRight = m_3 * 50 + 64

                #print(count)
               # claw, count = claw_conv(m_4,count)
                #print(claw)
                
                
		#claw = int(round(m_4,0))* 63 + 64

                #print(forwLeft, forwRight, vertLeft, vertRight)
                for nonie in range(0,2):
                        writeNumber(int(forwLeft))#fr
                        time.sleep(t_wait)
                
                        writeNumber(int(vertRight))#vr
                        time.sleep(t_wait)

                        writeNumber(int(forwRight))#frl
                        time.sleep(t_wait)

                        writeNumber(int(vertLeft))#vl
                        time.sleep(t_wait)
                        cl = int(m_4*63+64)
    #			        print(cl)
                        writeNumber(cl)
                        time.sleep(t_wait)

    #			        print(cl, int(forwLeft), int(forwRight), int(vertRight), int(vertLeft))

                        writeNumber(0)
                        time.sleep(t_wait)

                        print(int(forwLeft),int(vertRight),int(forwRight),int(vertLeft),cl,0)
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
                
		
'''
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
'''


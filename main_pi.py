import smbus
import time
import pygame
import sys


bus = smbus.SMBus(1)
address = 0x04

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
print(joystick.get_name)


def writeNumber(value):
    value = int(value)
    bus.write_byte(address, value)
    # bus.write_byte_data(address, 0, value)
    return -1

def readNumber():
    number = bus.read_byte(address)
    number = bus.read_byte_data(address, 1)
    return number

def send(sgs):
    pr = ""
    for signal in sgs:
        writeNumber(int(signal))
        time.sleep(0.01)
        pr += int(signal) + ", "
    print(pr)


#Setup
err_time = 0
end = True
axis_forward_back = 1
axis_left_right = 0
axis_up_down = 2
axis_twist = 3
count = 0
mult = 63

while True:
        try:
                
                pygame.event.pump()
                fb = joystick.get_axis(axis_forward_back)
                lr = joystick.get_axis(axis_left_right)
                ud = joystick.get_axis(axis_up_down)
                tw = joystick.get_axis(axis_twist)
                hat = joystick.get_hat(0)
                #trig = joystick.get_

                forwLeft = (fb + lr/2) * mult + 64
                forwRight = (fb - lr/2) * mult + 64
                if (fb + lr/2) > 1:
                        forwLeft = 1 * mult + 64

                if (fb + lr/2) < -1:
                        forwLeft = -1 * mult + 64

                if (fb - lr/2) > 1:
                        forwRight = 1 * mult + 64
                        
                if (fb - lr/2) < -1:
                        forwRight = -1 * 63 + 64
                
                vertLeft = ud * mult + 64
                vertRight = ud * mult + 64
                cl = abs(hat*63+64)
                
                Signals = [
                    forwLeft,
                    vertRight,
                    forwRight,
                    vertLeft,
                    cl,
                    0
                ]

                send(Signals)
                send(Signals)
                
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
                



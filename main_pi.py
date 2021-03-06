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



def readNumber():
    number = bus.read_byte(address)
    number = bus.read_byte_data(address, 1)
    return number

def send(sgs):
    pr = ""
    for signal in sgs:
        writeNumber(signal)
        time.sleep(0.01)
        pr += str(signal) + ", "
    writeNumber(0)
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
                ud = joystick.get_axis(axis_up_down) / 2
		fast1 = joystick.get_button(3)
                tw = joystick.get_axis(axis_twist) * 2 / 3
                trig = joystick.get_button(0)
		sp = joystick.get_hat(0)[0] + 3
		enable = joystick.get_button(1)
		fast2 = joystick.get_button(4)
		
		if(fast2):
			ud = ud * 2

		if(fast1):
			tw = tw * 3 / 2 
                forwLeft = int((fb + tw) * mult + 64)
                forwRight = int((fb - tw) * mult + 64)
                if (fb + tw) > 1:
                        forwLeft = int(1 * mult + 64)

                if (fb + tw) < -1:
                        forwLeft = int(-1 * mult + 64)

                if (fb - tw) > 1:
                        forwRight = int(1 * mult + 64)
                        
                if (fb - tw) < -1:
                        forwRight = int(-1 * 63 + 64)
                
                vertLeft = int(ud * mult + 64)
                vertRight = int(ud * mult + 64)
                cl = int(abs(((trig) * (enable-0.3))*90+64))
                
                Signals = [
			forwLeft,
			vertRight,
			forwRight,
			vertLeft,
			cl,
			sp,
                ]
                #print("= " + str(Signals))
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



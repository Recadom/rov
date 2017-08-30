import time
import pygame

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

print joystick.get_name

while True:
        try:
            pygame.event.pump()
            for x in range (0, 1):
                    var = float(round(joystick.get_axis(x),2))
                    print(var)
                    time.sleep(0.1)
                    
        except:
            print ('Error')
            time.sleep(.1)

pygame.close()


'''
while True:
	pygame.event.pump()
	for x in range (0, 4):
		var = int(joystick.get_axis(x) * 14 + 15 + x * 30)
		print(var)
		time.sleep(0.13)
	var = int(joystick.get_hat(0)[0] + 120)
	print(var)
	time.sleep(0.13)
'''

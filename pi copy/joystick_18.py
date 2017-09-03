import pygame, sys, time
from pygame.locals import *

 # Program starts
class joy_stick(object):

	def __intit__(self): #To make anything global to all functions
		self.joystick = pygame.joystick.Joystick(0)
		
	def start(self): # Initializes everything!
		pygame.init()
		pygame.joystick.init()
		self.joystick.init()
		
    def get(self,trial = None): #pass true if trial version
        if trial == True:
            for event in pygame.event.wait(): # Waiting for a response
                if event.type == pygame.JOYBUTTONDOWN:
                    print("Joystick button pressed.",event)
                    return event
                elif event.type == pygame.JOYBUTTONUP:
                    print("Joystick button released.",event)
                    return event
                elif event.type == pygame.JOYHATMOTION:
                    print("Joystick hat motion detected",event)
                    return event
                elif event.type == pygame.JOYBALLMOTION:
                    print("Joystick ball in motion",event)
                    return event
                elif event.type == pygame.JOYAXISMOTION:
                    print("Joystick axes detected",event)
                    return event
        else:
            for event in pygame.event.wait(): # Waiting for a response
                return event
    
    def close(self): # Close the program
		self.joystick.quit()
		pygame.quit()
			
#						***Code below runs only if file run***
							
if __name__ == "__main__": 
	i = joy_stick()
	i.start()
    print (pygame.joystick.get_count(),  'Number of joysticks')
	print (joystick.get_init(), 'If True, joystick has been initialized!',)
	print (joystick.get_id(), 'Name of id',)
	print (joystick.get_name(), 'Name of device',)
	print (joystick.get_numaxes(), 'Number of axis!',)
	print (joystick.get_numballs(), 'Number of track ball devices',)
	print (joystick.get_numbuttons(),'Number of buttons',)
	print (joystick.get_numhats(), 'Number of joystick hats',)
	print (' ')
    input('Enter to continue: ')
	while True: #Runs
        time.sleep(.03)
		try: i.get(True)
		except KeyboardInterrupt: pass
		finally:
			i.close()
			print ('Successful shutdown!')

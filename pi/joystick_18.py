import pygame, sys, time
from pygame.locals import *

 # Program starts
class joy_stick(object):

	def __intit__(self): #To make anything global to all functions
##		self.joystick = pygame.joystick.Joystick(0)
	def start(self): # Initializes everything!
                self.joystick = pygame.joystick.Joystick(0)
		pygame.init()
		pygame.joystick.init()
		self.joystick.init()
		
	def get(self):
		for event in pygame.event.wait(): # Waiting for a response
			return event.type
	
	def close(self): # Close the program
		self.joystick.quit()
		pygame.quit()
			
#						***Code below runs only if file run***
							
if __name__ == "__main__": 
	i = joy_stick()
	i.start()
	print (joystick.get_init(), 'If True, joystick has been initialized!',)
	print (joystick.get_id(), 'Name of id',)
	print (joystick.get_name(), 'Name of device',)
	print (joystick.get_numaxes(), 'Number of axis!',)
	print (joystick.get_numballs(), 'Number of track ball devices',)
	print (joystick.get_numbuttons(),'Number of buttons',)
	print (joystick.get_numhats(), 'Number of joystick hats',)
	print (' ')
	while True: #Runs 
		try: print (i.get())
		except KeyboardInterrupt: pass
		finally:
			i.close()
			print ('Successful shutdown!')

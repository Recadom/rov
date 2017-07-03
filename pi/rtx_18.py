import time
import serial

# Program starts!
class seri(object):

	def __init__(self): # To make anything global to all functions
		self.ser = serial.Serial('/dev/ttyAMA0', baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )

	def read(self): # Reads the data
#       if ser.inWaiting() > 0:
#	        data = ser.read()
#			return data
		return self.ser.read()
    
	def write(self,data): # Writes the data
		self.ser.write(str(data))
    
	def close(self): # To close program    
		self.ser.close()  
                    
        
#						***Code below runs only if file run***


if __name__ == "__main__":
	i = seri()
	while True:
		try:
			user = input('What would you like to send?')
			i.write(user)
			i.read()
			
		except KeyboardInterrupt: print ("Exiting Program")
		
		except: print ("Error Occurs, Exiting Program")	
		
		finally:
			print ('Close successful!')
			i.close()
			break

		
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
	
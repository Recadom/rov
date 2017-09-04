import time
import serial

# Program starts!
class seri(object):

	def __init__(self): # To make anything global to all functions / Also, for usb connection, use '/dev/ttyUSB1' instead of /dev/ttyAMA0 which is for rx and tx pins! Try:  /dev/ttyS1 or  /dev/ttyS2
		self.ser = serial.Serial('/dev/ttyAMA0', baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1
                    )
		self.ser.close()
		self.ser.open()

	def read(self): # Reads the data
#       if ser.inWaiting() > 0:
#	        data = ser.read()
#			return data
		return self.ser.read()
    
	def write(self,data): # Writes the data
##                self.ser.open()
##                self.ser.is_open()
		self.ser.write(b'hello')
    
	def close(self): # To close program    
		self.ser.close()
                    
        
#						***Code below runs only if file run***


if __name__ == "__main__":
        i = seri()
        try:
            while True:
                user = input('What would you like to send? ')
                i.write(user)
                print('d')
                time.sleep(1)
                #print(i.read())
                
        except KeyboardInterrupt: print ("Exiting Program")
        
        except: print ("Error Occurs, Exiting Program")	
        
        finally:
                print ('Close successful!')
                i.close()

'''
if __name__ == "__main__":
            i = seri()
##        try:
            while True:
                user = input('What would you like to send? ')
                i.write(user)
                
                print(i.read())
                
##        except KeyboardInterrupt: print ("Exiting Program")
        
##        except: print ("Error Occurs, Exiting Program")	
        
##        finally:
##                print ('Close successful!')
##                i.close()


'''
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
	

import serial

ser = serial.Serial('/dev/ttyACM1',9600)
s = [0,1]

while True:
		print(str(int (ser.readline(),16)))
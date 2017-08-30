import serial
#ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
ser = serial.Serial('/dev/ttyACM0', 9600)
ser.close()
ser.open()

ser.write("testing")
try:
    while 1:
        response = ser.readline()
        print response
except KeyboardInterrupt:
    ser.close()

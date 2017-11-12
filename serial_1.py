import serial


port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.2)

while True:
    rcv = port.readline()
    if len(rcv) > 0:
        print(rcv)


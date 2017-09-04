#!/usr/bin/env python

import serial
import string


test=serial.Serial("/dev/ttyAMA0",9600)
test.close()
test.open()

try:
    while True:
                test.write('8')
                print(test.readline())
                
except KeyboardInterrupt:
    pass # do cleanup here

test.close()

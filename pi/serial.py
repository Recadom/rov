import smbus

#bus = smbus.SMBus(1) # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)

#address = 0x04

class _bus(bus_num, addr):

    def __self__(self,bus_num,addr):
        self.bus = bus_num
        self.address = addr

    def writeNumber(self,value):
        self.bus.write_byte(self.address, value)

    def readNumber(self):
        number = self.bus.read_byte(self.address)
        number = self.bus.read_byte_data(self.address, 1)
        return number



if __name__ == "__main__":
    import time
    while 1:
        try:
            dev_1 = _bus(1,0x04) #first device
            try:
                dev_1.writeNumber(2) # sends the value "two"
                try:
                    print(dev_1.readNumber()+': value read!')
                except:
                    print('reading data failed')
                    time.sleep(0.25)
            except:
                print('sending data failed')
                time.sleep(0.25)
        except KeyboardInterrupt:
            print('Leaving program')
            quit()
        except:
            print('Connection failing')
            time.sleep(0.25)

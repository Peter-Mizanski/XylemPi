import time as t
import smbus
import sys

DEVICE_BUS = 1
DEVICE_ADDR = 0x10
bus = smbus.SMBus(DEVICE_BUS)

i = 4

while True:
    try:
        bus.write_byte_data(DEVICE_ADDR, i, 0xFF)
        t.sleep(1)
        bus.write_byte_data(DEVICE_ADDR, i, 0x00)
        t.sleep(1) 
    except KeyboardInterrupt as e:
        print("Quit the Loop")
        sys.exit()
"""
Continuously read the serial port and process IO data received from a remote XBee.
"""

from xbee import XBee
import serial

# to find xbee port in terminal: ls /dev/tty.*
ser = serial.Serial('/dev/ttyUSB0', 9600)

xbee = XBee(ser)

# Continuously read and print packets
while True:
    try:
        response = xbee.wait_read_frame()
        print response
    except KeyboardInterrupt:
        break
        
ser.close()
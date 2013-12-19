#osc test

import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO
import time
import OSC

ADC.setup()
lastadc= -1
GPIO.setup("P9_41", GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
lastdig= -1
sc= OSC.OSCClient()
sc.connect(('192.168.1.52', 57120)) #edit to match your laptop ip

while True:
        val= int(ADC.read_raw("P9_39")) #0-1799
        if val!=lastadc:
                lastadc= val
                msg= OSC.OSCMessage()
                msg.setAddress("/adc")
                msg.append(val)
                sc.send(msg)
                print val
                #time.sleep(0.1)
        val= GPIO.input("P9_41")
        if val!=lastdig:
                lastdig= val
                msg= OSC.OSCMessage()
                msg.setAddress("/dig")
                msg.append(val)
                sc.send(msg)
                print val
        time.sleep(0.05)
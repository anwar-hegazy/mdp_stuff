#digital test with BBIO

import Adafruit_BBIO.GPIO as GPIO
import time
GPIO.setup("P9_41", GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
while True:
        val= GPIO.input("P9_41")
        print val
        time.sleep(0.25)
#simple analog input test

import Adafruit_BBIO.ADC as ADC
import time
ADC.setup()
while True:
        val= int(ADC.read_raw("P9_39")) #0-1799
        print val
        time.sleep(0.125)
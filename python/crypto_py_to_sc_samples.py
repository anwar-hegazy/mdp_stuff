#send a number
import OSC
import time, random

client = OSC.OSCClient()
client.connect( ( '127.0.0.1', 57120 ) )
msg = OSC.OSCMessage()
msg.setAddress("/print")
msg.append(1000)
client.send(msg)

#########
#####ALL SAMPLES MUST BE WAVS
import wave
import contextlib
import glob
import time
import os
import OSC

os.chdir('/Users/cta/Desktop/samples/')
path = '/Users/cta/Desktop/samples/'
samples = []
sampdur = []
paths = []

samples = os.listdir(path)
samples.pop(0)                  #for some reason im getting .DS_Store in this list, so im popping it out

for i in samples:
    fname = i
    with contextlib.closing(wave.open(fname, 'r')) as f:
        frames=f.getnframes()
        rate = f.getframerate()
        duration = frames/float(rate)
        cleandur = round(duration)
        print cleandur
        sampdur.append(cleandur)

paths = os.listdir(path)
paths.pop(0)                    #same as above

masterlist = zip(paths, sampdur)
#cool, we have now automatically made our master array

#okay, now lets establish our connection with sc
client = OSC.OSCClient()
client.connect( ( '127.0.0.1', 57120 ) )
msg = OSC.OSCMessage()
msg.setAddress("/sample")


#and here is an example of how you would send all of the files from your folder sequentially (without overlap)
counter = range(len(masterlist))

for ind, itm, in enumerate(counter):
    label = masterlist[ind][0]
    print label
    dur = masterlist[ind][1]
    msg.insert(0, ind)
    client.send(msg)
    time.sleep(dur + 1.0)

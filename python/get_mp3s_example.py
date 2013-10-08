import urllib2

#set mp3 destination here
location = raw_input("Enter the mp3 location: ")
location = str(location)
print "you entered ", location

#do the rest
mp3file = urllib2.urlopen( location ) )
output = open('test.mp3', 'wb')
output.write(mp3file.read())
print "DONE!"
output.close()
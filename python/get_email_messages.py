

import email

fp = open('20080217-dude-971038.eml')

msg = email.message_from_file(fp)
#check one: how many parts is the message?
#issue 1: if multipart, need to walk through message and print get_payload() for each part
#issue 2: if message is single part, only need to get_payload()
for part in msg.walk():
    print part.get_payload()
""""
this loads all .eml files from a directory (exported there via thunderbird), opens them, reads them into a variable,
and stores each instance into a list called mailz

decode the message with the get_decoded_email_body() object, filter it with regex, then write to a big long text file
"""

import email
import os
import glob
import re
import itertools

mailz = []
archive = []
clean_mails = ""
msg =""
log = ""

os.chdir('/Users/cta/Desktop/email_test')
for f in glob.glob('*.eml'):
    fp = open( f )
    msg = email.message_from_file(fp)
    mailz.append(msg)

""" Decode email body.
"""

#for this in mailz:
#for this in mailz:
for this in itertools.islice(mailz, 50, 100):
    text = ""

    msg = email.message_from_string(str(this))
    
    if msg.is_multipart():
        html = None
        for part in msg.get_payload():
            if part.get_content_type() is not 'application/pdf' or part.get_content_type() is not 'image/jpeg': 
                print "%s, %s" % (part.get_content_type(), part.get_content_charset())

                if part.get_content_charset() is None:
                # We cannot know the character set, so return decoded "something"
                    text = part.get_payload(decode=True)
                    continue

                charset = part.get_content_charset()
                
                if part.get_content_type() == 'text/plain':
                    text = unicode(part.get_payload(decode=True), str(charset), "ignore").encode('utf8', 'replace')
                    output1 = text.strip()
                    clean_mails = re.sub('(\\nOn(.*?)wrote:\\n)|(\>(.*?)\\n)|(\>(.*?)$)', '', output1)
                    cleaner_mails = re.sub('([^\<]+)\<','', clean_mails)
                    archive.append(cleaner_mails)

for i in archive:
    fp2 = open('/Users/cta/Desktop/email_test/OUTPUT.txt', 'a')
    fp2.write( ' ' + str(i) )
    fp2.close()
    print 'added another message!'

                # elif part.get_content_type() == 'text/html':
                #     html = unicode(part.get_payload(decode=True), str(charset), "ignore").encode('utf8', 'replace')
                #     output1 = text.strip()
                #     clean_mails = re.sub('(\\nOn(.*?)wrote:\\n)|(\>(.*?)\\n)|(\>(.*?)$)', '', output1)
                #     archive.append(clean_mails)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests 
import datetime

# Create date time stamp
now = datetime.datetime.now() ; d = now.date() ; t = now.time()

# Storing the mailgun API key outside the file.
# The -1 is to remove the \n it is reading from the file
apifilename = "api.key.secret"
apikey = str(open(apifilename).read())[:-1]

class Sendmail(object):
    
    def send_simple_message(self):
        try:
            return requests.post(
                "https://api.mailgun.net/v2/MyDomain.com/messages",
                auth=("api", apikey),
                files=[("attachment", open("report.txt"))],
                data={"from": "Some one <some@one.com>",
                "to": ["some@body.com", "somebody@else.com"],
                "subject": "Subject line",
                "text": "Email body" })
        except Exception, e:
            print e
            print "Could not connect to Mailgun API"
            
email = Sendmail()
email.send_simple_message()

print "message sent"

#!/usr/bin/env python

import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from Parser9GAG import Parser9GAG

# me == my email address
# you == recipient's email address
me = "guillem.hernandez.sola@gmail.com"
you = "guillem.hernandez@softonic.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Your " + (time.strftime("%d/%m/%Y")) + " daily 9GAG digest"
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!<p>This a daily digest from 9gag<p>"
header = """<html><head></head><body>"""
center = Parser9GAG().FindLinksNoImage()
footer ="""Brought to you by Guillem<p></p></body></html>"""
html = header + text + center + footer

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)

# Send the message via local SMTP server.
s = smtplib.SMTP('localhost')
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
s.sendmail(me, you, msg.as_string())
s.quit()

#!/usr/bin/python3

# https://realpython.com/python-send-email/

import smtplib
import socket
import subprocess
import ssl
import time
from credentials import *


def is_online():
    # https://stackoverflow.com/a/40283805
    try:
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False


while not is_online():
    time.sleep(3)

ip_string = subprocess.run(['hostname', '-I'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
time_string = subprocess.run(['date', '+%m-%d %r'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()

message_raw = \
"""From: Nvidia Jetson Startup Script <{}>
Subject: Automated Jetson IP Message

IP addresses: {}
Time: {}

This is an automated message.
"""
message = message_raw.format(EMAIL, ip_string, time_string)
# print(message)



receivers = ["eph3rrp@virginia.edu"]
smtp_server = "smtp.gmail.com"
port = 587

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context = context)
    server.login(EMAIL, PASSWORD)
    server.sendmail(EMAIL, receivers, message)


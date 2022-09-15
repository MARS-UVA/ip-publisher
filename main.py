#!/usr/bin/python3

import requests
import smtplib
import socket
import subprocess
import ssl
import time
from credentials_groupme import *


def send_email(ip_string, time_string):
    # https://realpython.com/python-send-email/

    message_raw = \
    """From: Nvidia Jetson Startup Script <{}>
    Subject: Automated Jetson IP Message

    Time: {}
    IP addresses: {}

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

def send_groupme_message(ip_string, time_string):
    message_raw = "Time: {}\nIP addresses: {}"
    message = message_raw.format(time_string, ip_string)

    # https://dev.groupme.com/tutorials/bots
    response = requests.post("https://api.groupme.com/v3/bots/post", json={"bot_id": BOT_ID, "text": message})
    # print(response.text)

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
time_string = subprocess.run(['date', '+%m-%d-%Y %r'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()

# print(ip_string, time_string)
# send_email(ip_string, time_string)
send_groupme_message(ip_string, time_string)

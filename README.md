# IP emailer script

This script runs on startup to send an email containing the Jetson's local IP address to recipients in the script. If the Jetson isn't connected to the internet, it will wait until it is before emailing and terminating. 

Register this script in a cron job so it runs on startup: https://www.baeldung.com/linux/run-command-start-up


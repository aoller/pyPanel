#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import socket

GPIO.setmode(GPIO.BOARD)

GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#remote_ip = '192.168.1.135'
remote_ip = '192.168.4.1'
port = 1234

button1 = GPIO.input(8)
button2 = GPIO.input(10)

#f = open('/tmp/pyPanel.log', 'w')
#f.write('Start\n')  # python will convert \n to os.linesep
#f.close() 

while True:
	newButton1 = GPIO.input(8)
	newButton2 = GPIO.input(10)

	if(button1 == 1 and newButton1 == 0):
		print("Button 1 pressed")
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((remote_ip , port))
			s.sendall('\t?P1017Pulsador 1 ACTIVO\r\n')
			s.recv(2)
			time.sleep(4)
			s.close()
		except socket.error:
			print("Network error")

	if(button2 == 1 and newButton2 == 0):
		print("Button 2 pressed")
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((remote_ip , port))
			s.sendall('\t?Q1017Pulsador 2 ACTIVO\r\n')
			s.recv(2)
			time.sleep(4)
			s.close()
		except socket.error:
			print("Network error")


	button1 = newButton1
	button2 = newButton2
	
	time.sleep(0.1)

GPIO.cleanup()

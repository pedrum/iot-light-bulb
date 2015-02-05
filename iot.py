#IoT Light Bulb Concept - Web Server
from bottle import route, run, static_file, error, redirect, abort
from time import sleep
import serial

comPort = '/dev/tty.usbmodem1421'  #replace with your COM port
status = 0
ser = serial.Serial(comPort, 9600)
ser.write('0')	#start with bulb off

#Define Routes
@route('/images/<filename>')
def images(filename):
	return static_file(filename, root='images')

@route('/css/<filename>')
def css(filename):
	return static_file(filename, root='css')

@route('/')
def index():
	return static_file('index.html', root='')

@route('/api')
def get():
    return str(status)

@route('/api/<value:int>', method='POST')
def post(value='1'):
	global status

	if value == 1:
		status = 1
		sendOnToArduino()
	elif value == 0:
		status = 0
		sendOffToArduino()
	else:
		return str(-1)
	
	return str(status)

def sendOnToArduino():
	global ser
	ser.write('1')

def sendOffToArduino():
	global ser
	ser.write('0')

run(host='localhost', port=80, debug=True)

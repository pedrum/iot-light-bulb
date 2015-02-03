from bottle import route, run, static_file, error, redirect, abort
from time import sleep
import serial

#turn bulb off when first starting
status = 0
ser = serial.Serial('/dev/tty.usbmodem1421', 9600)
ser.write('0')

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

	#write value to serial port
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
#! /usr/bin/env python
import points
import serial
import time
import struct
import math
from pyquaternion import Quaternion


EV3 = serial.Serial('/dev/tty.SHOURJOSEV3-SerialPort')
print ("Listening for EV3 Bluetooth messages, press CTRL C to quit.")
vertices = []
outs = []
sortedouts = []
count = 0

def listen():
	string = []
	n = EV3.inWaiting()
	if n != 0: 
		s = EV3.read(n)
		for n in s:
			string.append("%02X" % ord(n))
		#print
		return string
	else:
		return None
		# No data is ready to be processed
		time.sleep(0.5)

def decode():
	msg = listen() 
	if msg is not None:
		msgbits = int(msg[0],16)
		mailbox = [msg[7].decode("hex"), msg[8].decode("hex"), msg[9].decode("hex"), msg[10].decode("hex")]
		mailbox = "".join(mailbox)
		msg = struct.unpack("!f", str(msg[-1]+msg[-2]+msg[-3]+msg[-4]).decode("hex"))[0]
		return [mailbox,msg]

def pointcoords(dist, sdeg, bdeg):
	'''
	x = dist*math.sin(math.radians(sdeg))
	y = dist*math.cos(math.radians(sdeg))
	'''
	vert = [0, dist, 0]
	theta = math.radians(bdeg)
	phi = math.radians(sdeg)
	axis = [18*math.cos(theta), 0, 18*math.sin(theta)]
	print axis
	print Quaternion(axis=axis,angle=phi)
	rotated_vert = Quaternion(axis=axis,angle=phi).rotate(vert)
	final_vert = [x + y for x, y in zip(axis, rotated_vert)]
	return final_vert

print pointcoords(1, 10, 0)


try:
	while True:
		d = 0
		s = 0
		b = 0
		val = decode()
		if val is not None:
			#print val #sortedouts
			if val[0] == "END":
				break
			count += 1
			outs.append(val)
			if count%3 == 0:
				#print count
				sortedouts.append([outs[count-1],outs[count-2],outs[count-3]])
				vertices.append(pointcoords(outs[-3][1],outs[-2][1],outs[-1][1]))
				print vertices[-1]
				#print vertices[-1] 
				#print outs[-3][1],outs[-2][1],outs[-1][1]


except KeyboardInterrupt:
	pass

print vertices
points.create()
points.finish(vertices)

EV3.close()

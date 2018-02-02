#Python 2.7
import cv2
import os
import sys 
from math import floor
def ascii(img):
	ratio = img.shape[0]/float(img.shape[1])
	rows, columns = os.popen('stty size', 'r').read().split()
	columns = int(columns)/2
	img = cv2.cvtColor(cv2.resize(img,(columns,int(floor(columns*ratio)))), cv2.COLOR_BGR2GRAY)
	gap = (int(rows)-img.shape[0])/2
	def asciiMapping(val):		
		shades = '  .:-=+*#%@'#[::-1]
		segments = 255/(len(shades)-1)
		return shades[(val/segments)]
	transformedAscii = []
	for i in img:
		temp = []
		for j in i:
			temp.append(asciiMapping(j))
		transformedAscii.append(temp)
	ascii = ''
	for i in transformedAscii:
		ascii += ' '.join(i)
		ascii += '\n'
	return '\n'*gap+ascii
cap = cv2.VideoCapture(0)
while True:
	ret, frame = cap.read()
	print ascii(frame)
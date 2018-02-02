#Python 2.7
from Tkinter import *
import re
root=Tk()
display=''
root.title('Roman Converter')
pattern='^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

def convert(roman):
	table=[('M',1000),('CM',900),('D',500),('CD',400),('C',100),('XC',90),('L',50),('XL',40),('X',10),('IX',9),('V',5),('IV',4),('I',1)]
	result=0
	flag=True
	if roman=='':
		return ''
	while flag:
		for letter, value in table:
			if letter==roman[:len(letter)]:
				result+=value
				roman=roman[len(letter):]
				if len(roman)==0:
					flag=False
	return str(result)

def valid(disp,value):
	global display,pattern
	if value=='R':
		disp=''
	if value=='B':
		disp=disp[:-1]
	if re.search(pattern,disp+value):
		disp+=value
	display=disp
	return disp

def isvalid(number):
	global pattern
	if re.search(pattern,number):
		return True
	else:
		return False
	
def choice(value):
	global display
	romandisp=valid(display,value)
	LCD.config(text=romandisp)
	LCD2.config(text=convert(romandisp))

LCD=Label(root, width=15)
LCD.grid(row=0,column=0,columnspan=1)
LCD2=Label(root, width=15)
LCD2.grid(row=0,column=1,columnspan=1)

R=Button(root,text='Reset',command=lambda: choice('R'),width=15,pady=5)
R.grid(row=1,column=0)

B=Button(root,text='<-',command=lambda: choice('B'),width=15,pady=5)
B.grid(row=1,column=1)

I=Button(root,text='I',command=lambda: choice('I'),width=15,pady=5)
I.grid(row=2,column=0)

V=Button(root,text='V',command=lambda: choice('V'),width=15,pady=5)
V.grid(row=2,column=1)

X=Button(root,text='X',command=lambda: choice('X'),width=15,pady=5)
X.grid(row=3,column=0)

L=Button(root,text='L',command=lambda: choice('L'),width=15,pady=5)
L.grid(row=3,column=1)

C=Button(root,text='C',command=lambda: choice('C'),width=15,pady=5)
C.grid(row=4,column=0)

D=Button(root,text='D',command=lambda: choice('D'),width=15,pady=5)
D.grid(row=4,column=1)

M=Button(root,text='M',command=lambda: choice('M'),width=30,pady=5)
M.grid(row=5,column=0,columnspan=2)

root.mainloop()

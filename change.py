import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import subprocess
from tkinter import *
import sys

def both():
	sample()
	write()
#def printtext():
def sample():
		
	global e
	sys.stdout = open("output.txt","w")
	email = e.get()
	x=Label(root, text="Enter the email")
	with open('comcast1.csv', 'r') as f:
	    
	    wines = list(csv.reader(f))

	frame = pd.DataFrame(wines)
	frame = frame[[0,1,2,]]
	frame.columns = ['Email','Name','Address']

	#print(frame)

	#print("enter email of the person")

	#email = input()

	#rint(email)
	
	for index,row in frame.iterrows():
		if row['Email']==email:
			print(row)
			name=row[1]
			#email=row[2]
			#print("inside",name)
		else:
			pass
		f.close()
	with open('new.csv', 'r') as f:
	    wines1 = list(csv.reader(f ,  delimiter=':'))

	data = pd.DataFrame(wines1)
	data = data[[0,1]]
	data.columns = ['Email','Password']


	for index,row in data.iterrows():
		if row['Email']==email:
			print('Password'+"--"+row[1])
			#passw=row[1]
		else:
			pass

		f.close()
	with open('3.csv', 'r') as f:
	    wines2 = list(csv.reader(f ,  delimiter=':'))

	data2 = pd.DataFrame(wines2)
	data2 = data2[[0,1]]
	data2.columns = ['Email','Phone']


	for index,row in data2.iterrows():
		if row['Email']==email:
			print('Phone'+"--"+row[1])
			#phone=row[1]
		else:
			pass
		f.close()
	
	return
	
def write():
	with open("output.txt","w") as f:
		if(f):
			output=sample()
			f.write(str(output))
		
		f.close()

	
def opens():
	
	with open('output.txt', 'r') as f:
	    

		if(f):
			if(textBox.get("1.0",END))=="\n":
				
					content=f.readlines()
					print(str(content))
					for line in content:
						textBox.insert(END,line)
						
					
			else:
					textBox.delete('1.0', END)
					content=f.readlines()
					print(str(content))
					for line in content:
						textBox.insert(END,line)
			
			return			
			
		
'''
wines = list(csv.reader(f))
	v=StringVar()
	print(wines[0])
	print(v)
	w1 = Label(root, textvariable=wines[0])
	w1.pack()dteehan@comcast.net
	v.set(wines[0])
'''


root = Tk()
#window=Tk()
root.resizable(height=False,width=False)
root.minsize(700,500)


root.title('OSINT')
display= Label(root, text="Enter Your Email")
e=Entry(root,width=20)
e.pack()
e.focus_set()


b = Button(root,text='okay',command=both)
c= Button(root,text="Show details of the breach",command=opens)
textBox=Text()
textBox.place(x=30,y=80,height=200)
display.pack()
c.pack()	

b.pack(side='bottom')

root.mainloop()

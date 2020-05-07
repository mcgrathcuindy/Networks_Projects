# Names: Tanner Wilhelm & Chris McGrath
# Emails: wilhelmt@uindy.edu & mcgrathc@uindy.edu
# Class: CSCI 420
# Date: 02/19/2020
# Filename: reactionTimeGui.py
# Desc: Make a program with gui that plays a reaction time game between two computers

import socket
from tkinter import *
import random, time
from random import randint

master = Tk()
master.title('reactionTime.py')
colors = ['orange','red','blue','green']
clock1 =0
clock2 =0
count =0
name = ''

#variable to hold the ip address of the server
server_ip = '192.168.1.65' #EDIT THIS LINE HERE, put the ipv4 address of the computer hosting the server
port_number = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def sendTime(event = None):
	global clock2
	global name
	message = str(clock2)
	s.sendto(message.encode('ascii'), (server_ip, port_number))
	print("Time sent!")



def reset(event = None):
	global master
	label = Label(master, text= "\t\t")	
	label.grid(column = 0, row = 2)
	global count
	count = 0
	master.after(1000,changeColors)

def changeColors(event = None):
	global colors
	global master
	global count
	master.configure(bg = colors[count])
	box.configure(bg = colors[count])
	spaceLabel1.configure(bg=colors[count])
	spaceLabel2.configure(bg=colors[count])
	count = count + 1
	if count == 4:
		global clock1
		clock1 = time.time()
		return
	master.after(randint(1000,3000),changeColors)
	
def stopClock(event = None):
	global clock1
	global clock2
	clock2 = time.time() - clock1
	label = Label(master, text= "{}".format(clock2))	
	label.grid(column = 0, row = 2)
	sendTime()
	return

master.after(1000,changeColors)

spaceLabel1 = Label(master, text = "\t\t")
spaceLabel1.grid(column = 0, row = 0)

spaceLabel2 = Label(master, text = "\t\t")
spaceLabel2.grid(column = 0, row = 1)


box = Label(master,text = "When the background turns green \nclick 'Stop Clock!'\n",bg='white')
box.grid(column = 0, row = 2)
button = Button(master,text="Stop Clock!",fg='red')
button.grid(column = 0, row = 3)
button.bind('<Button>', stopClock)
button2 = Button(master,text="Reset")
button2.grid(column = 0, row = 4)
button2.bind('<Button>',reset)
mainloop()


"""
NAME: Christopher McGrath
DATE: 2/4/2020
DESC: Python Program that 
	  1. Accepts a list of people through "Entry"
	  2. picks one at random, outputs to GUI
	  3. Will not output the same person twice
	  4. if a person's name is only four letters
	  	 such as "Paul" they will be added to 
	  	 the pool twice, thus increasing their 
	  	 chance of being chosen
	  5. Displays all of this with a GUI
"""
	  
from tkinter import *
import random

master = Tk()
master.title('gameRandomizer.py')
count = 0
lastChoice = None

def pickPlayer(event = None):
	global count
	count = count + 1
	if not w.get():
		label = Label(master, text= "\tNo data!\t\t")
		label.grid(column = 0, row = 2)
	else :
		l = w.get().split(",")
		randWord = random.choice(l)
		num = len(l)							#if num is less than 2 then the while
		if num < 2 : 							#loop below will run forever
			label = Label(master, text= "\t>2!!\t\t")	
			label.grid(column = 0, row = 2)
			return
		for a in range(num):
			if(len(l[a])==4):					#if a name in the list is 4
				l.append(l[a])					#letters, we add it in again
		if count == 1:							
			label = Label(master, text=	"\t{}\t\t".format(randWord))
			label.grid(column = 0, row = 2)		#the first time this function is called
			global lastChoice					#we print the random choice and set
			lastChoice = randWord				#last choice equal to it for the next iteration
			return
		while randWord == lastChoice :			#more than one name must be entered or
			randWord = random.choice(l)			#this while loop will never stop
		label = Label(master, text=	"\t{}\t\t".format(randWord))
		label.grid(column = 0, row = 2)
		lastChoice = randWord

box = Label(master,text = "Enter a list of at least 2 names separated only by a comma \ni.e. 'Joe,Bob,Chris'\n")
box.grid(column = 0, row = 0)
w = Entry(master)
w.grid(column = 0, row = 1)
button = Button(master,text="Pick Player!")
button.grid(column = 0, row = 3)
button.bind('<Button>', pickPlayer)
mainloop()
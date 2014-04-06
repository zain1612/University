# Group 11 Developing Quality Software Prototype
# Filename: DisplayResults.py
# Team member name: Zain Tahir
# Team member student number: 1308094

from Tkinter import *
import tkMessageBox
import csv
import MainPage
from ttk import Style

class Questionnaire(Frame):
	#GUI Setup

	def __init__(self,master):
		#Initialise Questionnaire class 
		Frame.__init__(self,master)
		self.grid()
		self.createWelcomeTitle()
		self.createInterestedIn()
		self.enterName()
		self.createButtons()
		self.clearResponse()
		self.centre_window()
		master.protocol( 'WM_DELETE_WINDOW', self.check_quit ) # Iain's code

	def createWelcomeTitle(self):
		lblProg = Label(self, text = 'This Questionnaire is designed to suggest a degree program based on your aptitude and skills.', font = ('MS',10,'bold'))
		lblProg.grid(row = 1, column = 1, columnspan = 6,)


	def createInterestedIn(self):
		#Create widgets to ask and store response to the 10 questions.
		
		lblProg = Label(self, text = 'I am interested in:', font = ('MS',8,'bold'))
		lblProg.grid(row = 3, column = 0, columnspan = 2, sticky = W)
		
		lblStrArg = Label(self, text = 'Stongly \n Disagree', font = ('MS', 8, 'bold'))
		lblStrArg.grid(row = 3, column = 4, rowspan = 2)
			
		lblStrArg = Label(self, text = 'Partly \n Disagree', font = ('MS', 8, 'bold'))
		lblStrArg.grid(row = 3, column = 5, rowspan = 2)
		
		lblStrArg = Label(self, text = 'Neither \n Agree \n or \n Disagree', font = ('MS', 8, 'bold'))
		lblStrArg.grid(row = 3, column = 6, rowspan = 2)

		lblStrArg = Label(self, text = 'Partly \n Agree', font = ('MS', 8, 'bold'))
		lblStrArg.grid(row = 3, column = 7, rowspan = 2)
		
		lblStrArg = Label(self, text = 'Stongly \n Agree', font = ('MS', 8, 'bold'))
		lblStrArg.grid(row = 3, column = 8, rowspan = 2)

		#Mathematics

		lblProg = Label(self, text = 'Mathematics:', font = ('MS',8,'bold'))
		lblProg.grid(row = 5, column = 0, columnspan = 2, sticky = W)

		self.varQ1 = IntVar()
		R1Q1 = Radiobutton(self, variable=self.varQ1, value=1)
		R1Q1.grid(row=5, column= 4)
		R2Q1 = Radiobutton(self, variable= self.varQ1, value=2)
		R2Q1.grid(row=5, column= 5)
		R3Q1 = Radiobutton(self, variable= self.varQ1, value=3)
		R3Q1.grid(row=5, column= 6)
		R4Q1 = Radiobutton(self, variable= self.varQ1, value=4)
		R4Q1.grid(row=5, column= 7)
		R5Q1 = Radiobutton(self, variable= self.varQ1, value=5)
		R5Q1.grid(row=5, column= 8)	

		#Problem Solving

		lblProg = Label(self, text = 'Problem Solving:', font = ('MS',8,'bold'))
		lblProg.grid(row = 6, column = 0, columnspan = 2, sticky = W)

		self.varQ2 = IntVar()
		R1Q2 = Radiobutton(self, variable=self.varQ2, value=1)
		R1Q2.grid(row=6, column= 4)
		R2Q2 = Radiobutton(self, variable=self.varQ2, value=2)
		R2Q2.grid(row=6, column= 5)
		R3Q2 = Radiobutton(self, variable=self.varQ2, value=3)
		R3Q2.grid(row=6, column= 6)
		R4Q2 = Radiobutton(self, variable=self.varQ2, value=4)
		R4Q2.grid(row=6, column= 7)
		R5Q2 = Radiobutton(self, variable=self.varQ2, value=5)
		R5Q2.grid(row=6, column= 8)

		#Large Scale Application Efficiency.

		lblProg = Label(self, text = 'Large scale application efficiency:', font = ('MS',8,'bold'))
		lblProg.grid(row = 7, column = 0, columnspan = 2, sticky = W)

		self.varQ3 = IntVar()
		R1Q3 = Radiobutton(self, variable=self.varQ3, value=1)
		R1Q3.grid(row=7, column= 4)
		R2Q3 = Radiobutton(self, variable=self.varQ3, value=2)
		R2Q3.grid(row=7, column= 5)
		R3Q3 = Radiobutton(self, variable= self.varQ3, value=3)
		R3Q3.grid(row=7, column= 6)
		R4Q3 = Radiobutton(self, variable= self.varQ3, value=4)
		R4Q3.grid(row=7, column= 7)
		R5Q3 = Radiobutton(self, variable= self.varQ3, value=5)
		R5Q3.grid(row=7, column= 8)

		#The implementation of computer systems in a business environment.

		lblProg = Label(self, text = 'The implementation of computer systems in a business environment:', font = ('MS',8,'bold'))
		lblProg.grid(row = 8, column = 0, columnspan = 2, sticky = W)

		self.varQ4 = IntVar()
		R1Q4 = Radiobutton(self, variable=self.varQ4, value=1)
		R1Q4.grid(row=8, column= 4)
		R2Q4 = Radiobutton(self, variable= self.varQ4, value=2)
		R2Q4.grid(row=8, column= 5)
		R3Q4 = Radiobutton(self, variable= self.varQ4, value=3)
		R3Q4.grid(row=8, column= 6)
		R4Q4 = Radiobutton(self, variable= self.varQ4, value=4)
		R4Q4.grid(row=8, column= 7)
		R5Q4 = Radiobutton(self, variable= self.varQ4, value=5)
		R5Q4.grid(row=8, column= 8)

		#Programming.

		lblProg = Label(self, text = 'Programming:', font = ('MS',8,'bold'))
		lblProg.grid(row = 9, column = 0, columnspan = 2, sticky = W)

		self.varQ5 = IntVar()
		R1Q5 = Radiobutton(self, variable=self.varQ5, value=1)
		R1Q5.grid(row=9, column= 4)
		R2Q5 = Radiobutton(self, variable= self.varQ5, value=2)
		R2Q5.grid(row=9, column= 5)
		R3Q5 = Radiobutton(self, variable= self.varQ5, value=3)
		R3Q5.grid(row=9, column= 6)
		R4Q5 = Radiobutton(self, variable= self.varQ5, value=4)
		R4Q5.grid(row=9, column= 7)
		R5Q5 = Radiobutton(self, variable= self.varQ5, value=5)
		R5Q5.grid(row=9, column= 8)

		#Security 

		lblProg = Label(self, text = 'Security:', font = ('MS',8,'bold'))
		lblProg.grid(row = 10, column = 0, columnspan = 2, sticky = W)

		self.varQ6 = IntVar()
		R1Q6 = Radiobutton(self, variable=self.varQ6, value=1)
		R1Q6.grid(row=10, column= 4)
		R2Q6 = Radiobutton(self, variable= self.varQ6, value=2)
		R2Q6.grid(row=10, column= 5)
		R3Q6 = Radiobutton(self, variable= self.varQ6, value=3)
		R3Q6.grid(row=10, column= 6)
		R4Q6 = Radiobutton(self, variable= self.varQ6, value=4)
		R4Q6.grid(row=10, column= 7)
		R5Q6 = Radiobutton(self, variable= self.varQ6, value=5)
		R5Q6.grid(row=10, column= 8)			

		#Forensics

		lblProg = Label(self, text = 'Forensics:', font = ('MS',8,'bold'))
		lblProg.grid(row = 11, column = 0, columnspan = 2, sticky = W)

		self.varQ7 = IntVar()
		R1Q7 = Radiobutton(self, variable=self.varQ7, value=1)
		R1Q7.grid(row=11, column= 4)
		R2Q7 = Radiobutton(self, variable= self.varQ7, value=2)
		R2Q7.grid(row=11, column= 5)
		R3Q7 = Radiobutton(self, variable= self.varQ7, value=3)
		R3Q7.grid(row=11, column= 6)
		R4Q7 = Radiobutton(self, variable= self.varQ7, value=4)
		R4Q7.grid(row=11, column= 7)
		R5Q7 = Radiobutton(self, variable= self.varQ7, value=5)
		R5Q7.grid(row=11, column= 8)

		#Games
		
		lblProg = Label(self, text = 'Games:', font = ('MS',8,'bold'))
		lblProg.grid(row = 12, column = 0, columnspan = 2, sticky = W)

		self.varQ8 = IntVar()
		R1Q8 = Radiobutton(self, variable=self.varQ8, value=1)
		R1Q8.grid(row=12, column= 4)
		R2Q8 = Radiobutton(self, variable= self.varQ8, value=2)
		R2Q8.grid(row=12, column= 5)
		R3Q8 = Radiobutton(self, variable= self.varQ8, value=3)
		R3Q8.grid(row=12, column= 6)
		R4Q8 = Radiobutton(self, variable= self.varQ8, value=4)
		R4Q8.grid(row=12, column= 7)
		R5Q8 = Radiobutton(self, variable= self.varQ8, value=5)
		R5Q8.grid(row=12, column= 8)

		#Visual Representation

		lblProg = Label(self, text = 'Visual Representation:', font = ('MS',8,'bold'))
		lblProg.grid(row = 13, column = 0, columnspan = 2, sticky = W)

		self.varQ9 = IntVar()
		R1Q9 = Radiobutton(self, variable=self.varQ9, value=1)
		R1Q9.grid(row=13, column= 4)
		R2Q9 = Radiobutton(self, variable= self.varQ9, value=2)
		R2Q9.grid(row=13, column= 5)
		R3Q9 = Radiobutton(self, variable= self.varQ9, value=3)
		R3Q9.grid(row=13, column= 6)
		R4Q9 = Radiobutton(self, variable= self.varQ9, value=4)
		R4Q9.grid(row=13, column= 7)
		R5Q9 = Radiobutton(self, variable= self.varQ9, value=5)
		R5Q9.grid(row=13, column= 8)

		#Producing Software

		lblProg = Label(self, text = 'Producing Software:', font = ('MS',8,'bold'))
		lblProg.grid(row = 14, column = 0, columnspan = 2, sticky = W)

		self.varQ10 = IntVar()
		R1Q10 = Radiobutton(self, variable=self.varQ10, value=1)
		R1Q10.grid(row=14, column= 4)
		R2Q10 = Radiobutton(self, variable= self.varQ10, value=2)
		R2Q10.grid(row=14, column= 5)
		R3Q10= Radiobutton(self, variable= self.varQ10, value=3)
		R3Q10.grid(row=14, column= 6)
		R4Q10 = Radiobutton(self, variable= self.varQ10, value=4)
		R4Q10.grid(row=14, column= 7)
		R5Q10 = Radiobutton(self, variable= self.varQ10, value=5)
		R5Q10.grid(row=14, column= 8)

		# #Ask the questions in part 2

		# lblProg = Label(self, text = '', font = ('MS',8,'bold'))
		# lblProg.grid(row = 15, column = 0, columnspan = 2, sticky = W)
		
		# lblStrArg = Label(self, text = 'Yes', font = ('MS', 8, 'bold'))
		# lblStrArg.grid(row = 15, column = 4, rowspan = 2)
			
		# lblStrArg = Label(self, text = 'No', font = ('MS', 8, 'bold'))
		# lblStrArg.grid(row = 15, column = 5, rowspan = 2)

		#Do you plan on getting a job in Computing? (Select one)

		# lblProg = Label(self, text = 'Do you plan on getting a job in Computing?', font = ('MS',8,'bold'))
		# lblProg.grid(row = 17, column = 0, columnspan = 2, sticky = W)

		# self.varQ11 = IntVar()
		# R1Q11 = Radiobutton(self, variable=self.varQ11, value=1)
		# R1Q11.grid(row=17, column= 4)
		# R2Q11 = Radiobutton(self, variable= self.varQ11, value=2)
		# R2Q11.grid(row=17, column= 5)

		# #'(If Q1: Yes) Do you have any routes into a Computing job?'

		# lblProg = Label(self, text = '(If Q1: Yes) Do you have any routes into a Computing job?', font = ('MS',8,'bold'))
		# lblProg.grid(row = 18, column = 0, columnspan = 2, sticky = W)

		# self.varQ12 = IntVar()
		# R1Q12 = Radiobutton(self, variable=self.varQ12, value=1)
		# R1Q12.grid(row=18, column= 4)
		# R2Q12 = Radiobutton(self, variable= self.varQ12, value=2)
		# R2Q12.grid(row=18, column= 5)

	def enterName(self):
		#Enter single line of text from a user (Name in this case) and the label 
 		self.entForename = Entry(self) 
 		self.entForename.grid(row=19, column=4, columnspan=2, sticky=W) 
		
		lblProb1 = Label(self, text='Forename:', font=('MS', 8,'bold'))
		lblProb1.grid(row=19, column = 0, sticky=W)

		self.entSurname = Entry(self) 
 		self.entSurname.grid(row=20, column=4, columnspan=2, sticky=W) 
		
		lblProb1 = Label(self, text='Surname:', font=('MS', 8,'bold'))
		lblProb1.grid(row=20, column = 0, sticky=W)
	
	def createButtons(self):
		#set up the Submit and Clear buttons.

		#button to submit

		butSubmit = Button(self, text='Submit',font=('MS', 8,'bold')) 
 		butSubmit['command']=self.storeResponse #Note: no () after the method 
 		butSubmit.grid(row=22, column=4, columnspan=2,sticky=W)

 		#button to clear
		
		butClear = Button(self, text='Clear',font=('MS', 8,'bold')) 
 		butClear['command']=self.clearResponse #Note: no () after the method 
 		butClear.grid(row=22, column=5, columnspan=2,sticky= W)

 		butMain = Button(self, text='Return To Main',font=('MS', 8,'bold')) 
 		butMain['command']=self.to_main #Note: no () after the method 
 		butMain.grid(row=22, column=6, columnspan=2,sticky= W)  

 	def clearResponse(self):
 		#clear the questionnaire 

		#Clear the radiobuttons
		self.varQ1.set(0)
		self.varQ2.set(0)
		self.varQ3.set(0)
		self.varQ4.set(0)
		self.varQ5.set(0)
		self.varQ6.set(0)
		self.varQ7.set(0)
		self.varQ8.set(0)
		self.varQ9.set(0)
		self.varQ10.set(0)
		# self.varQ11.set(0)
		# self.varQ12.set(0)
		#Clear the name field
		self.entForename.delete(0, END)
		self.entSurname.delete(0, END)

	def storeResponse(self):
		#Class store the name and the degree option in the database. 

	#Check for unanswered questions.
		if (self.varQ1.get()== 0) or (self.varQ2.get() == 0) or (self.varQ3.get() == 0) or (self.varQ4.get() == 0) or (self.varQ5.get() == 0) or (self.varQ6.get() == 0) or (self.varQ7.get() == 0) or (self.varQ8.get() == 0) or (self.varQ9.get() == 0) or (self.varQ10.get() == 0):
			tkMessageBox.showinfo("Error", "Please answer all questions")
		else:
			

	#Method of working out the degree programme:

		#answer = sum of all the radiobuttons (upto q10) divided by 10 
			answer = (self.varQ1.get()+self.varQ2.get()+self.varQ3.get()+self.varQ4.get()+self.varQ5.get()+self.varQ6.get()+self.varQ7.get()+self.varQ8.get()+self.varQ9.get()+self.varQ10.get())/10.0

			#if answer lies in a certain range , indicates the degree.		

			if 1 <= answer < 2.525:
				degree = "Business Information Systems"

			elif 2.525 <= answer < 2.975:
				degree = "Computer Science"

			elif 2.975 <= answer < 3.2:
				degree = "Computer Science with \nHigh Performance Computing"

			elif 3.2 <= answer < 3.275:
				degree = "Computer Science with \nSecurity & Forensics"

			elif 3.275 <= answer < 3.525:
				degree = "Computer Science with \nVisual Computing"
			
			elif answer >= 3.525:
				degree = "Software Engineering"	

			else:
				degree = ""

			if self.entForename.get() == "":
				tkMessageBox.showinfo("Error", "Please enter your Forename")
			elif self.entSurname.get() == "":
				tkMessageBox.showinfo("Error", "Please enter your Surname")
			else:


	#----------------------CSV-------------------------#

				response = [self.get_forename(),self.get_surname(),degree]
				questionnaire  = open("questionnaire.csv","a")
				writer = csv.writer(questionnaire,delimiter=',')
				writer.writerow(response)
				questionnaire.flush()
				questionnaire.close()

			#tkMessagebox to inform user their response is stored
				tkMessageBox.showinfo("Questionnaire", str(self.get_forename()) + " " + str(self.get_surname()) + " you should do " + degree)
				self.clearResponse()

	#function to return forename 
	def get_forename(self):
		return self.entForename.get()
	#function to return surname
	def get_surname(self):
		return self.entSurname.get()
	#function to return degree
	def get_degree(self):
		return degree

	def to_main(self):
		self.master.destroy()
		MainPage.main()
	
	def centre_window(self):
      
		width = 775
		height = 425

		swidth = self.master.winfo_screenwidth()
		sheight = self.master.winfo_screenheight()

		x = (swidth - width)/2
		y = (sheight - height)/2
		self.master.geometry('%dx%d+%d+%d' % (width, height, x, y))

	def check_quit(self):
		cancel = tkMessageBox.askokcancel("Quit", " Are you sure you want to quit? \n Press OK to quit \n Press Cancel to return")
		if cancel:
			self.master.destroy()
		else:
			pass

def main():
	# Main
	root = Tk()
	root.title("Questionnaire")
	root.minsize(775,425)	# To not allow resizing of the window
	root.maxsize(775,425) 	# ''
	app = Questionnaire(root)
	root.mainloop()
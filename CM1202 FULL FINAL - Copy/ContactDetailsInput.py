# Group 11 Developing Quality Software Prototype
# Filename: ContactDetailsOutput.py
# Team member name: Iain Johnston
# Team member student number: 1312579

### Import modules ###
from Tkinter import *
from ttk import Style
import tkMessageBox
import csv
from re import *

import MainPage
######################

class ContactDetailsInput(Frame):
	# GUI Setup

	def __init__(self, master):
		''' Initialise ContactDetailsInput Class '''
		Frame.__init__(self, master)

		self.grid()

		self.create_input_boxes()
		self.create_buttons()
		self.clear_response()
		self.centre_window()
		self.focus_force()
		master.protocol( 'WM_DELETE_WINDOW', self.check_quit )
		
		self.store_response

	def create_input_boxes(self):
		''' Create the input boxes and a title. '''
		self.style = Style()
		self.style.theme_use("clam")
		
		lbl_info = Label(self, text='Please enter your name and email address' 
								  + ' if you would like to be contacted about' 
								  + ' Cardiff Computer Science in the future.', pady=15, padx=10)
		lbl_info.grid(row=1, columnspan=10, rowspan=4)

		self.ent_forename = Entry(self)
		self.ent_forename.grid(row=6, column=4, columnspan=2)

		lbl_forename = Label(self, text='Forename:', font=('MS', 10, 'bold'), pady=5)
		lbl_forename.grid(row=6, column=2)

		self.ent_surname = Entry(self)
		self.ent_surname.grid(row=10, column=4, columnspan=2, sticky=W)
		lbl_forename = Label(self, text='Surname:', font=('MS', 10, 'bold'), pady=5)
		lbl_forename.grid(row=10, column=2)

		self.ent_email = Entry(self)
		self.ent_email.grid(row=12, column=4, columnspan=2, sticky=W)
		lbl_forename = Label(self, text='Email:', font=('MS', 10, 'bold'), pady=5)
		lbl_forename.grid(row=12, column=2)

	
	def create_buttons(self):
		''' Create the buttons for submitting the details and clearing them
		'''
		submit_but = Button(self, text='Submit', font=('MS', 10, 'bold'))
		submit_but['command'] = self.store_response
		submit_but.grid(row=16, column=2, columnspan=2)

		clear_but = Button(self, text='Clear', font=('MS', 10, 'bold'))
		clear_but['command'] = self.clear_response
		clear_but.grid(row=16, column=5, columnspan=2)

		back_but = Button(self, text= 'Return to Main', font=('MS', 10, 'bold'))
		back_but['command'] = self.to_main
		back_but.grid(row=16, column=8, columnspan=2)


	
	def clear_response(self):
		''' Clear the entries '''
		self.ent_forename.delete(0, END)
		self.ent_surname.delete(0, END)
		self.ent_email.delete(0, END)

	
	def store_response(self):
		''' Initialise a csv file,
		get the entries, add them to the file.
		'''
		filename = 'Details.csv'

		if self.get_forename() == "" and self.get_surname() == "" and self.get_email() == "":
			tkMessageBox.showwarning(title="Entry Error", message="Please complete all fields")
			self.focus_force()
		else:
			if not self.validEmail():	# Check the entered email against a simple regular expression for emails
				tkMessageBox.showwarning(title='Email error', message='Please enter a valid email address')
				self.focus_force()
			elif self.validEmail() and not self.details_in_file():	# if the entered email is valid, add that and the other details to the csv file 
				details_list = [self.get_forename(), self.get_surname(), self.get_email()]
				input_file = open(filename, 'a')	# Open the csv file
				writer = csv.writer(input_file, delimiter=",", quotechar='"')	# Create a writer object.
				writer.writerow(details_list)	# Write the data to the file.
				input_file.flush()	# flush the data to the disk
				input_file.close()	# Close the file
				tkMessageBox.showinfo(title='Details Submitted', message='Your details have been saved.')
				self.focus_force()
				self.quit()				# Call the quit method to close the window


	def details_in_file(self): 
		''' Check if the details are already in the file.
		'''
		details_list = [self.get_forename(), self.get_surname(), self.get_email()]
		print details_list
		with open('Details.csv', 'rb') as details_file:
			file_reader = csv.reader(details_file) 
			for row in file_reader:
				if row[0] in details_list and row[1] in details_list and row[2] in details_list:
					return True
				else:
					return False
	

	def centre_window(self):
		''' Center the window in the middle of the screen
      	'''
		width = 760
		height = 175

		swidth = self.master.winfo_screenwidth()
		sheight = self.master.winfo_screenheight()

		x = (swidth - width)/2
		y = (sheight - height)/2
		self.master.geometry('%dx%d+%d+%d' % (width, height, x, y))			

	
	def get_forename(self):
		''' Accessor for forename
		'''
		return self.ent_forename.get()

	
	def get_surname(self):
		''' Accessor for surname
		'''
		return self.ent_surname.get()


	def get_email(self):
		''' Accessor for email
		'''
		return self.ent_email.get()

	
	def __str__(self):
		''' To string method
		'''
		return ("Forename: " + self.Forename + "\n"
			  + "Surname: " + self.Surname + "\n" 
			  + "Email: " + self.Email)

	
	def validEmail(self):
		'''Method which takes the inputted email and checks it's validity against a basic email regular expression
	 	If email is valid return it, otherwise ask for a different email.
		'''
		my_regex = compile("^([A-Za-z0-9_\.-]+)@([\dA-Za-z\.-]+)\.([a-z\.]{2,6})$")
		match_email  = my_regex.search(self.get_email())

		if match_email:
			return True
		else:
			return False

	def quit_window(self):
		''' Cleanly close the window when finished
		'''
		self.master.destroy()

	def check_quit(self):
		cancel = tkMessageBox.askokcancel("Quit", " Are you sure you want to quit? \n Press OK to quit \n Press Cancel to return")
		if cancel:
			self.master.destroy()
		else:
			pass

	def to_main(self):
		self.quit_window()
		MainPage.main()


def main():
	''' Main loop '''
	root = Tk() 
	root.minsize(760, 175)
	root.maxsize(760, 175)
	root.title("Contact Details")
	app = ContactDetailsInput(root)
	root.mainloop()

if __name__ == '__main__':
	main()

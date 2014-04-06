# Group 11 Developing Quality Software Prototype
# Filename: ContactDetailsOutput.py
# Team member name: Iain Johnston
# Team member student number: 1312579


from Tkinter import *
from ttk import *
import csv
import tkMessageBox

class ContactDetailsOutput(Frame):
	# GUI Setup

	def __init__(self, master):
		''' Initialise the ContactDetailsOutput class '''
		Frame.__init__(self, master)
		scrollbar = Scrollbar(master)
		scrollbar.pack(side=RIGHT, fill=Y)

		self.pack()
		self.output_details(scrollbar)
		self.centre_window()
		self.focus_force()

	def output_details(self, scrollbar):
		''' Configure display for output '''

		self.style = Style()
		self.style.theme_use("clam")

		self.txtDisplay = Text(self, height=14, width=100, bg='#CDD1CD', yscrollcommand=scrollbar.set)		# Initialise text box
		scrollbar.config(command=self.txtDisplay.yview)
		self.txtDisplay.tag_configure('title', font=('MS', 14, 'bold'), underline=1)	# Initialise the title text style
		self.txtDisplay.tag_configure('data', font=('MS', 12))		# initialise the details text style
		
		tab_results = ("\t" + "\t" + "\t")			# Initialise a variable for style tabulation 

		self.txtDisplay.insert(END,"\t" + "Forename" + tab_results + "Surname"
								+ tab_results + "Email" + "\n", 'title')		# Insert the title text

		filename = 'Details.csv'

		with open(filename, 'rb') as details_file:		# open the csv file
			file_reader = csv.reader(details_file) 			# create a csv reader object
			try:
				for row in file_reader:
					file_forename = row[0]	# Take first element of csv file list
					file_surname = row[1]
					file_email = row[2]

					self.txtDisplay.insert(END,"\t" + file_forename + tab_results + file_surname
										+ tab_results + file_email + "\n", 'data')	# Insert the details into the text box
			except csv.Error as e:
				sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
				
		self.txtDisplay['state'] = DISABLED
		self.txtDisplay.pack()

	def centre_window(self):
      
		width = 750
		height = 225

		swidth = self.master.winfo_screenwidth()
		sheight = self.master.winfo_screenheight()

		x = (swidth - width)/2
		y = (sheight - height)/2
		self.master.geometry('%dx%d+%d+%d' % (width, height, x, y))

def main():
	# Main
	root = Toplevel()
	root.minsize(750, 225)
	root.maxsize(750, 225)
	root.title("Contact Details")
	app = ContactDetailsOutput(root)
	root.mainloop()


if __name__ == '__main__':
	main()


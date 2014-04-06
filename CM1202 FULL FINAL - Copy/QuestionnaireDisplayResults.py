from Tkinter import *
from ttk import *
import csv

class DisplayResults(Frame):
# GUI Setup
	def __init__(self, master):
	# Initialise Questionnaire Class
		
		Frame.__init__(self, master)
		scrollbar = Scrollbar(master)
		scrollbar.pack(side=RIGHT, fill=Y)		

		self.pack()
		self.retrieveResponse(scrollbar)
		self.centre_window()
		self.focus_force()
	
	def retrieveResponse(self,scrollbar):

		self.style = Style()
		self.style.theme_use("clam")

		self.txtDisplay = Text(self, height=14, width=400, bg='#CDD1CD', yscrollcommand=scrollbar.set)		# Initialise text box
		scrollbar.config(command=self.txtDisplay.yview)
		self.txtDisplay.tag_configure('title', font=('MS', 14, 'bold'), underline=1)	# Initialise the title text style
		self.txtDisplay.tag_configure('data', font=('MS', 12))		# initialise the details text style
		
		tab_results = ("\t" + "\t" + "\t")			# Initialise a variable for style tabulation 

		self.txtDisplay.insert(END,"\t" + "Forename" + tab_results + "Surname"
								+ tab_results + "Suggested Degree" + "\n", 'title')		# Insert the title text	
								
		with open('questionnaire.csv', 'rb') as f:
			reader = csv.reader(f)
			for row in reader:
				firstName = row[0]
				lastName = row[1]
				degree = row[2]

				self.txtDisplay.insert(END,"\t" + firstName + tab_results + lastName
										+ tab_results + degree + "\n", 'data')	# Insert the details into the text box

		self.txtDisplay['state'] = DISABLED
		self.txtDisplay.pack()


	def centre_window(self):
      
		width = 800
		height = 225

		swidth = self.master.winfo_screenwidth()
		sheight = self.master.winfo_screenheight()

		x = (swidth - width)/2
		y = (sheight - height)/2
		self.master.geometry('%dx%d+%d+%d' % (width, height, x, y))

def main():
	# Main
	root = Toplevel()
	root.minsize(800, 225)
	root.maxsize(800, 225)
	root.title("Questionnaire Results")
	app = DisplayResults(root)
	root.mainloop()


if __name__ == '__main__':
	main()


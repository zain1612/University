# Group 11 Developing Quality Software Prototype
# Filename: MainPage.py

############# Import modules ####################
from PIL import Image, ImageTk
from Tkinter import Tk, Label, BOTH, LEFT, RIGHT, BOTTOM, TOP, RAISED
from ttk import Frame, Style, Button
import tkMessageBox

###### Import Modules from other members ######
import LogicTest 				# Bert
import Questionnaire 			# Zain
import PractiseQuestions		# Jonny
import ExtendedTest 			# Daniel
import StaffAreaValidate 		# Iain
import ContactDetailsInput 		# Iain
###############################################

class MainPage(Frame):

	def __init__(self, master):
		''' Initialise the MainPage class '''
		Frame.__init__(self, master)

		self.master = master

		self.init_page()
		
		self.centre_window()
		
		self.focus_force()
		self.update()
		self.logo_image()
		master.protocol( 'WM_DELETE_WINDOW', self.check_quit )

	def init_page(self):
		''' Place the widgets into the screen '''
		self.master.title("Cardiff University")
		
		self.style = Style()
		self.style.theme_use("clam")

		frame = Frame(self, relief=RAISED, borderwidth=1.5)
		frame.pack(fill=BOTH, expand=1)

		self.pack(fill=BOTH, expand=1)

		self.frame1 = Frame(self, borderwidth=1.5)
		self.frame1.grid()

		self.frame1.pack()
		self.pack(fill=BOTH, expand=1)

		### Add command to open the corresponding classes ###
		### TODO 1) practice test
		practice_but = Button(self, text="Practice Questions", width=25)
		practice_but['command'] = self.to_practice
		practice_but.grid(in_=self.frame1, row=0, column=0, padx=10, pady=10)

		details_but = Button(self, text="Add Details", width=25)
		details_but['command'] = self.to_details 	# No parenthesis so only runs when called
		details_but.grid(in_=self.frame1, row=2, column=0, padx=10, pady=10)

		questionnaire_but = Button(self, text="Questionnaire", width=25)
		questionnaire_but['command'] = self.to_questionnaire 
		questionnaire_but.grid(in_=self.frame1, row=1, column=1, padx=10, pady=10)

		logic_but = Button(self, text="Logic Test", width=25)
		logic_but['command'] = self.to_logic
		logic_but.grid(in_=self.frame1, row=0, column=1, padx=10, pady=10)

		staff_but = Button(self, text="Staff Login", width=25)
		staff_but['command'] = self.to_staff
		staff_but.grid(in_=self.frame1, row=2, column=1, padx=10, pady=10)

		extended_but = Button(self, text="Extension Test", width=25)
		extended_but['command'] = self.to_extension
		extended_but.grid(in_=self.frame1, row=1, column=0, padx=10, pady=10)


	def centre_window(self):
		''' centre the window in the centre of the screen on opening '''
		win_width = 720
		win_height = 700

		swidth = self.master.winfo_screenwidth()
		sheight = self.master.winfo_screenheight()

		x = (swidth - win_width)/2
		y = (sheight - win_height)/2
		self.master.geometry('%dx%d+%d+%d' % (win_width, win_height, x, y))

	def logo_image(self):
		''' Get the logo image and place it in the window '''
		logo = Image.open("CardiffLogo.png")
		cardiff_logo = ImageTk.PhotoImage(logo)
		
		logo_label = Label(self, image= cardiff_logo)
		logo_label.image = cardiff_logo # keep a reference
		
		x, y = self.centre_image(logo)
		logo_label.place(x = x, y = y)

	def centre_image(self, img):
		''' Return the x and y for the image to be in the centre of the window '''
		
		win_width = 720
		win_height = 465

		image_width, image_height = img.size

		x = (win_width - image_width)/2
		y = (win_height - image_height)/2
		return (x,y)

	def to_staff(self):
		self.master.destroy()
		StaffAreaValidate.main()

	def to_details(self):
		self.master.destroy()
		ContactDetailsInput.main()

	def to_logic(self):
		self.master.destroy()
		LogicTest.main()

	def to_questionnaire(self):
		self.master.destroy()
		Questionnaire.main()

	def to_extension(self):
		self.master.destroy()
		ExtendedTest.main()

	def to_practice(self):
		self.master.destroy()
		PractiseQuestions.main()

	def check_quit(self):
		cancel = tkMessageBox.askokcancel("Quit", " Are you sure you want to quit? \n Press OK to quit \n Press Cancel to return")
		if cancel:
			self.master.destroy()
		else:
			pass
		

def main():
	''' Main loop '''
	root = Tk()
	root.minsize(720,640)	# To not allow resizing of the window
	root.maxsize(720,640) 	# ''
	app = MainPage(root)
	root.mainloop()

if __name__ == '__main__':
	main()
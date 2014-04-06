# Group 11 Developing Quality Software Prototype
# Filename: StaffArea.py

############# Import modules ####################
from PIL import Image, ImageTk
from Tkinter import Tk, Label, BOTH, TOP, RAISED, Toplevel
from ttk import Frame, Style, Button
import tkMessageBox

###### Import Modules from other members ###### 
import ContactDetailsOutput
import MainPage
import QuestionnaireDisplayResults
###############################################

class StaffArea(Frame):

	def __init__(self, master):
		''' Initialise the StaffArea class '''
		Frame.__init__(self, master)

		self.master = master

		self.init_page()
		self.centre_window()
		self.logo_image()
		self.focus_force()
		master.protocol( 'WM_DELETE_WINDOW', self.check_quit )

	def init_page(self):
		''' Place the widgets into the screen '''
		self.master.title("Cardiff University")
		self.style = Style()
		self.style.theme_use("clam")

		frame = Frame(self, relief=RAISED, borderwidth=1.5)
		frame.pack(fill=BOTH, expand=1)

		self.pack(fill=BOTH, expand=1)

		###### Add command to open the corresponding classes ######
		details_but = Button(self, text="View Contact Details", width=25)
		details_but['command'] = ContactDetailsOutput.main 
		details_but.pack(side=TOP, padx=10, pady=10)

		questionnaire_but = Button(self, text="View Questionnaire Results", width=25)
		questionnaire_but['command'] = QuestionnaireDisplayResults.main 
		questionnaire_but.pack(side=TOP, padx=10, pady=10)

		back_but = Button(self, text="<-- Back to Main Page --> ", width=25)
		back_but['command'] = self.to_main
		back_but.pack(side=TOP, padx=10, pady=10)

	def centre_window(self):
		''' Center the window in the center of the screen on opening '''
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
		''' Return the x and y for the image to be in the center of the window '''
		win_width = 720
		win_height = 500

		image_width, image_height = img.size

		x = (win_width - image_width)/2
		y = (win_height - image_height)/2
		return (x,y)

	def get_usernames():
		usernames = ['admin']
		return usernames 

	def get_passwords():
		passwords = ['abcd1234']
		return passwords

	def to_main(self):
		self.master.destroy()
		MainPage.main()

	def check_quit(self):
		cancel = tkMessageBox.askokcancel("Quit", " Are you sure you want to quit? \n Press cancel and click Main Page to return to main page")
		if cancel:
			self.master.destroy()
		else:
			pass

def main():
	''' Main loop '''
	w, h = 720, 640
	root = Tk()
	root.minsize(w, h)	# To not allow resizing of the window
	root.maxsize(w, h) 	# ''
	app = StaffArea(root)
	root.mainloop()

if __name__ == '__main__':
	main()
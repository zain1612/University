# Group 11 Developing Quality Software Prototype
# Filename: StaffAreaValidate.py
# Team member name: Iain Johnston 
# Team member student number: 1312579

from Tkinter import *
from ttk import *
from PIL import Image, ImageTk
import tkMessageBox
import StaffArea
import MainPage

class StaffAreaValidate(Frame):
    
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.grid()
        self.create_input_boxes()
        self.create_buttons()
        self.centre_window(w = 370, h = 143)
        self.focus_force()
        master.protocol( 'WM_DELETE_WINDOW', self.check_quit )

    def create_input_boxes(self):
        ''' Create the input boxes and a title. 
        '''

        self.style = Style()
        self.style.theme_use("clam")

        info_lbl = Label(self, text='Please enter the username and password')
        info_lbl.grid(row=1, columnspan=10, rowspan=4)

        self.ent_username = Entry(self)
        self.ent_username.grid(row=6, column=4, columnspan=2, pady=10)
        lbl_username = Label(self, text='Username:')
        lbl_username.grid(row=6, column=2)

        self.ent_password = Entry(self, show='*')
        self.ent_password.grid(row=10, column=4, columnspan=2, pady=10)
        lbl_password = Label(self, text='Password:')
        lbl_password.grid(row=10, column=2)

    def create_buttons(self):
        ''' Create the buttons for submitting the details and clearing them
        '''
        submit_but = Button(self, text='Submit')
        submit_but['command'] = self.validate_password
        submit_but.grid(row=16, column=2, columnspan=2, pady=5, padx=20)

        clear_but = Button(self, text='Clear')
        clear_but['command'] = self.clear_response
        clear_but.grid(row=16, column=5, columnspan=2, pady=5, padx=20)

        back_but = Button(self, text='Main Page')
        back_but['command'] = self.to_main
        back_but.grid(row=16, column=8, columnspan=2, pady=5, padx=20)

    
    def clear_response(self):
        ''' Clear the entries '''
        self.ent_username.delete(0, END)
        self.ent_password.delete(0, END)

    def centre_window(self, w, h):
        ''' Center the window in the middle of the screen '''
        swidth = self.master.winfo_screenwidth()
        sheight = self.master.winfo_screenheight()

        x = (swidth - w)/2
        y = (sheight - h)/2
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    def validate_password(self):
        ''' validate the entered username and password for entry to the staff area '''
        usernames = ['admin']
        passwords = ['pass']

        if self.get_username() in usernames and self.get_password() in passwords:
            self.quit_window()
            StaffArea.main()
        else:
            tkMessageBox.showwarning("Invalid Entry", "Username or Password incorrect")
            self.focus_force()
    
    def get_username(self):
        ''' Accessor for username '''
        return self.ent_username.get()

    def get_password(self):
        ''' Accessor for password '''
        return self.ent_password.get()

    def to_main(self):
        self.quit_window()
        MainPage.main()

    def quit_window(self):
        self.master.destroy()

    def check_quit(self):
        cancel = tkMessageBox.askokcancel("Quit", " Are you sure you want to quit? \n Press cancel and click Main Page to return to main page")
        if cancel:
            self.master.destroy()
        else:
            pass

def main():
    ''' Main loop '''
    w, h = 370, 143
    root = Tk()
    root.minsize(w, h)
    root.maxsize(w, h)
    root.title("Staff Area")
    app = StaffAreaValidate(root)
    root.mainloop()

if __name__ == '__main__':
    main()

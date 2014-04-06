# Author: Roberto Dyke
# Student Number: 1317850
from Tkinter import *
from ttk import *
from PIL import Image, ImageTk
from LoadCode import *
import MainPage
import tkMessageBox

class LogicTest(Frame):
    def __init__(self, master, questions): # Class:master, Class:questions
        Frame.__init__(self, master) # Initialises the master frame for LogicTest
        self.master = master # Type: Class
        self.questions = questions # Type: Class
        self.q_number = 1 # Stores current question number
        self.initUI() # Calls initUI method
        master.protocol('WM_DELETE_WINDOW', self.check_quit) # Checks if user selects the close button in the top right of the window, then quits appropriately
        self.centre_window()

    def initUI(self): # Creates initial widgets for window
        self.master.title("Logic Reasoning Test") # Writes window title to top of window
        self.style = Style()
        self.style.theme_use("clam") # Widget theme

        self.frame = Frame(self, relief=RAISED, borderwidth=1) # Creates a frame widget
        self.frame.pack(fill=BOTH, expand=1) # This tells the frame to take up as much space in the window as it can
        self.pack(fill=BOTH, expand=1) # Adds frame to master window
        # Frame panel widgets ----------
        # Introductory paragraph label
        intro_paragraph = self.questions.getCurrentQuestion().getIntroParagraph() # Gets the introductory paragraph for the inital question as type:string
        self.lbl_intro_paragraph = Label(self, text=intro_paragraph, justify=LEFT, wraplength=width, font=('MS', 8)) # Creates a label widget
        self.lbl_intro_paragraph.pack(side=TOP, in_=self.frame, pady=5)
        # Question label
        question = self.questions.getCurrentQuestion().getQuestion()
        self.lbl_question = Label(self, text=question, justify=LEFT, wraplength=width, font=('MS', 8, 'bold'))
        self.lbl_question.pack(side=TOP, in_=self.frame, pady=5)
        # Diagram label
        diagram = self.questions.getCurrentQuestion().getDiagram()
        self.lbl_diagram = Label(self, image=diagram)
        self.lbl_diagram.pack(side=TOP, in_=self.frame, pady=5)
        # Radio buttons
        self.initCheckboxes() # Calls initCheckboxes method
        # Master frame panel -----------
        # Quit button
        bttn_quit = Button(self, text="Quit Test", command=self.to_main)
        bttn_quit.pack(side=LEFT, padx=5, pady=5)
        # Submit button
        bttn_submit = Button(self, text="Submit Test", command=self.submitTest)
        bttn_submit.pack(side=LEFT, padx=5, pady=5)
        # Next button
        bttn_next = Button(self, text="Next", command=self.nextQuestion)
        bttn_next.pack(side=RIGHT, padx=5, pady=5)
        # Previous button
        bttn_prev = Button(self, text="Previous", command=self.previousQuestion)
        bttn_prev.pack(side=RIGHT)
        # Question number label
        self.lbl_q_number = Label(self, text=str(self.q_number), font=('MS', 8))
        self.lbl_q_number.pack(side=RIGHT, padx=5)
    
    def initCheckboxes(self): # Creates initial check boxes
        options = self.questions.getCurrentAnswer().getOptions() # Gets options for checkbuttons to refer to
        self.question_options = [] # List to hold information on checkbuttons current state (selected/not selected)
        self.cb_list = []
        for i in range(0,len(options)):
            self.question_options.append(IntVar())
            c = Checkbutton(self, text=options[i], variable=self.question_options[i])
            c.pack(side=LEFT,in_=self.frame, padx=5, pady=5)
            self.cb_list.append(c)

    def updateCheckboxes(self): # Updates information in check boxes
        options = self.questions.getCurrentAnswer().getOptions() # Gets options for checkbuttons to refer to
        self.question_options = [] # List to hold information on checkbuttons current state (selected/not selected)
        for i in range(0,len(options)):
            self.question_options.append(IntVar())
            if (i < len(self.cb_list)):
                option = options[i]
                self.cb_list[i]['text'] = option
                self.cb_list[i].visible = True
                value = self.questions.getCurrentQuestion().getAnswer().getSelected(i)
                self.question_options[i].set(value)
                self.cb_list[i]['variable'] = self.question_options[i]
            else:
                self.question_options[i].set(self.questions.getCurrentQuestion().getAnswer().getSelected(i))
                c = Checkbutton(self, text=options[i], variable=self.question_options[i])
                c.pack(side=LEFT,in_=self.frame, padx=5, pady=5)
                self.cb_list.append(c)
        for i in range(0, len(self.cb_list)):
            if (i >= len(options)):
                self.cb_list[i].pack_forget()
        for j in range(len(self.cb_list), 0, -1):
            i = j - 1
            if (i >= len(options)):
                value = self.cb_list[i]
                self.cb_list.remove(value)
    
    def nextQuestion(self): # Move the current question to the next question
        for i in range(0,len(self.question_options)):
            if (self.question_options[i].get() == 1):
                self.questions.getCurrentQuestion().getAnswer().selectAnswer(i)
            elif (self.question_options[i].get() == 0):
                self.questions.getCurrentQuestion().getAnswer().removeSelectedAnswer(i)
        if self.questions.nextQuestion():
            self.q_number += 1
        self.widgetQuestionUpdate()
    
    def previousQuestion(self): # Move the current question to the next question
        for i in range(0,len(self.question_options)):
            if (self.question_options[i].get() == 1):
                self.questions.getCurrentQuestion().getAnswer().selectAnswer(i)
            elif (self.question_options[i].get() == 0):
                self.questions.getCurrentQuestion().getAnswer().removeSelectedAnswer(i)
        if self.questions.previousQuestion():
            self.q_number -= 1
        self.widgetQuestionUpdate()
    
    def widgetQuestionUpdate(self): # Updates widgets so that information displayed matches current information in questions class
        self.lbl_q_number['text'] = str(self.q_number) # Change question number
        self.lbl_intro_paragraph['text'] = self.questions.getCurrentQuestion().getIntroParagraph() # Change introductory paragraph
        self.lbl_question['text'] = self.questions.getCurrentQuestion().getQuestion() # Change question
        self.lbl_diagram['image'] = self.questions.getCurrentQuestion().getDiagram() # Change diagram
        self.updateCheckboxes() # Change check boxes
    
    def submitTest(self): # Calculates user's final score for the test and calls method to display results
        # Saves data of final question to questions class
        for i in range(0,len(self.question_options)):
            if (self.question_options[i].get() == 1):
                self.questions.getCurrentQuestion().getAnswer().selectAnswer(i)
            elif (self.question_options[i].get() == 0):
                self.questions.getCurrentQuestion().getAnswer().removeSelectedAnswer(i)
        self.updateCheckboxes()
        # Calculates the total correct answers and total answers
        self.total_correct_answers = 0
        self.total_answers = 0
        while self.questions.previousQuestion(): # This resets the questions
            pass
        self.total_correct_answers += self.questions.getCurrentQuestion().getAnswer().countCorrect()
        self.total_answers += len(self.questions.getCurrentQuestion().getAnswer().getCorrectAnswers())
        while self.questions.nextQuestion():
            self.total_correct_answers += self.questions.getCurrentQuestion().getAnswer().countCorrect()
            self.total_answers += len(self.questions.getCurrentQuestion().getAnswer().getCorrectAnswers())
        self.pack_forget()
        self.frame.pack_forget()
        self.showResults()
    
    def showResults(self): # Presents the results of the test to the user
        Frame.__init__(self, self.master)
        self.frame = Frame(self, relief=RAISED, borderwidth=1)
        self.frame.pack(fill=BOTH, expand=1)
        # Title label
        self.title = Label(self, text="Result", justify=LEFT, font=('MS', 32, 'bold'))
        self.title.pack(side=TOP, in_=self.frame, pady=5)
        # Score label
        results = "Total correct answers: " + str(self.total_correct_answers) + "\n\tout of\nTotal answers: " + str(self.total_answers)
        self.test = Label(self, text=results, justify=LEFT, font=('MS', 16, 'bold'))
        self.test.pack(side=TOP, in_=self.frame, pady=5)
        self.pack(fill=BOTH, expand=1)
        # Return button
        bttn_next = Button(self, text="Return to main", command=self.to_main) # Creates button widget to return to the main menu
        bttn_next.pack(side=TOP, padx=5, pady=5)
    
    def quitWindow(self): # Gracefully quits the LogicTest window
        self.master.destroy()

    def to_main(self): # Returns the user to the main menu
        self.quitWindow()
        MainPage.main()

    def check_quit(self): # Checks to see if user has selected the quit(X) button in the top right of the screen
        cancel = tkMessageBox.askokcancel("Quit", " Are you sure you want to quit? \n Press OK to quit \n Press Cancel to return")
        if cancel:
            self.quitWindow()
        else:
            pass

    def centre_window(self):
        ''' centre the window in the centre of the screen on opening from Iain'''
        win_width = 720
        win_height = 700

        swidth = self.master.winfo_screenwidth()
        sheight = self.master.winfo_screenheight()

        x = (swidth - win_width)/2
        y = (sheight - win_height)/2
        self.master.geometry('%dx%d+%d+%d' % (win_width, win_height, x, y))

width, height = 600, 550

def main():
    root = Tk()
    root.geometry(str(width) + "x" + str(height))
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    app = LogicTest(root,loadCode())
    root.mainloop()
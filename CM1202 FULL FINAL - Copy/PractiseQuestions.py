# Author: Jonathan Ellis
# Student Number: 1106512

from Tkinter import *
from ttk import *
import tkMessageBox
from os import path
import MainPage

### Read SubQuestions from text files #####################################################################
subDirectory = "PractiseQuestionsData"
Questions = [path.join(subDirectory,"question1.gif"), path.join("PractiseQuestionsData","question2.gif")]
Question1a = open(path.join(subDirectory, "question1a.txt")).read()
Question1b = open(path.join(subDirectory, "question1b.txt")).read()
Question1c = open(path.join(subDirectory, "question1c.txt")).read()
Question2a = open(path.join(subDirectory, "question2a.txt")).read()
Question2b = open(path.join(subDirectory, "question2b.txt")).read()
Question2c = open(path.join(subDirectory, "question2c.txt")).read()

### Read SubQuestion Answers for radio buttons ############################################################
QuestionAnswer1a = open(path.join(subDirectory, "questionAnswer1a.txt"))
QuestionAnswer1a_i = QuestionAnswer1a.readline()
QuestionAnswer1a_ii = QuestionAnswer1a.readline()
QuestionAnswer1a_iii = QuestionAnswer1a.readline()
QuestionAnswer1a_iv = QuestionAnswer1a.readline()
QuestionAnswer1a_v = QuestionAnswer1a.readline()

QuestionAnswer1b = open(path.join(subDirectory, "questionAnswer1b.txt"))
QuestionAnswer1b_i = QuestionAnswer1b.readline()
QuestionAnswer1b_ii = QuestionAnswer1b.readline()
QuestionAnswer1b_iii = QuestionAnswer1b.readline()
QuestionAnswer1b_iv = QuestionAnswer1b.readline()
QuestionAnswer1b_v = QuestionAnswer1b.readline()

QuestionAnswer1c = open(path.join(subDirectory, "questionAnswer1c.txt"))
QuestionAnswer1c_i = QuestionAnswer1c.readline()
QuestionAnswer1c_ii = QuestionAnswer1c.readline()
QuestionAnswer1c_iii = QuestionAnswer1c.readline()
QuestionAnswer1c_iv = QuestionAnswer1c.readline()
QuestionAnswer1c_v = QuestionAnswer1c.readline()

QuestionAnswer2a = open(path.join(subDirectory, "questionAnswer2a.txt"))
QuestionAnswer2a_i = QuestionAnswer2a.readline()
QuestionAnswer2a_ii = QuestionAnswer2a.readline()
QuestionAnswer2a_iii = QuestionAnswer2a.readline()
QuestionAnswer2a_iv = QuestionAnswer2a.readline()
QuestionAnswer2a_v = QuestionAnswer2a.readline()

QuestionAnswer2b = open(path.join(subDirectory, "questionAnswer2b.txt"))
QuestionAnswer2b_i = QuestionAnswer2b.readline()
QuestionAnswer2b_ii = QuestionAnswer2b.readline()
QuestionAnswer2b_iii = QuestionAnswer2b.readline()
QuestionAnswer2b_iv = QuestionAnswer2b.readline()
QuestionAnswer2b_v = QuestionAnswer2b.readline()

QuestionAnswer2c = open(path.join(subDirectory, "questionAnswer2c.txt"))
QuestionAnswer2c_i = QuestionAnswer2c.readline()
QuestionAnswer2c_ii = QuestionAnswer2c.readline()
QuestionAnswer2c_iii = QuestionAnswer2c.readline()
QuestionAnswer2c_iv = QuestionAnswer2c.readline()
QuestionAnswer2c_v = QuestionAnswer2c.readline()

#########################################################################################################

# Provides text for each subquestion
SubQuestions = [[Question1a, Question1b, Question1c], [Question2a, Question2b, Question2c]]
# Default value of student answers to questions
studentAnswers = [[0, 0, 0], [0, 0, 0]]
# Numeric value of correct answers to questions
answersToQuestions = [[3, 1, 2], [4, 5, 3]]

### List of all the radio button question answers ########################################################
SubQuestionAnswers = [[[QuestionAnswer1a_i, QuestionAnswer1a_ii, QuestionAnswer1a_iii, QuestionAnswer1a_iv, QuestionAnswer1a_v],
					 [QuestionAnswer1b_i, QuestionAnswer1b_ii, QuestionAnswer1b_iii, QuestionAnswer1b_iv, QuestionAnswer1b_v],
					 [QuestionAnswer1c_i, QuestionAnswer1c_ii, QuestionAnswer1c_iii, QuestionAnswer1c_iv, QuestionAnswer1c_v]],
					 [[QuestionAnswer2a_i, QuestionAnswer2a_ii, QuestionAnswer2a_iii, QuestionAnswer2a_iv, QuestionAnswer2a_v],
					 [QuestionAnswer2b_i, QuestionAnswer2b_ii, QuestionAnswer2b_iii, QuestionAnswer2b_iv, QuestionAnswer2b_v],
					 [QuestionAnswer2c_i, QuestionAnswer2c_ii, QuestionAnswer2c_iii, QuestionAnswer2c_iv, QuestionAnswer2c_v]]]
##########################################################################################################



# initialises global variable question and sub-question value at zero (zero-indexing) 
global question_number, sub_question_number
question_number, sub_question_number = 0, 0

class PractiseLogicTest(Frame):
	
	def __init__(self, master):
		# Tkinter inheritance (AppUI)
		Frame.__init__(self, master)
		self.master = master

		# Loads instructions function
		self.instructions()
		master.protocol( 'WM_DELETE_WINDOW', self.check_quit )
		self.centre_window()
		
	# Defines the standard GUI
	def GUI(self):
		# Match the style of standard questions
		self.master.title("Practise Logic Reasoning Test")
		self.style = Style()
		self.style.theme_use("clam")
		self.frame = Frame(self, relief=RAISED, borderwidth=1)
		self.frame.pack(fill=BOTH, expand=1)
		self.pack(fill=BOTH, expand=1)

	def startTestButton(self):
		label_instructions_text.pack_forget()
		start_button.pack_forget()
		self.displayCurrentQuestion(question_number)
		self.displayCurrentSubQuestion(question_number, sub_question_number)
		self.displayRadioButtons(question_number, sub_question_number)
		self.displayTravelButtons()

	def instructions(self):
		self.GUI()
		# read the file containing the text for instructions for the practise test
		instructions_text = open(path.join(subDirectory, "instructions.txt")).read()
		# create a Tkinter label containing the text of the instructions text file
		global label_instructions_text
		label_instructions_text = Label(self, text=instructions_text, justify=LEFT, wraplength=width, background="white", font=('MS', 8))
		label_instructions_text.pack(in_=self.frame, pady=5)

		# create a Tkinter button that calls the function to start the practise test
		global start_button
		start_button = Button(self, text="Start Practise Questions", command=self.startTestButton)
		start_button.pack(in_=self.frame, pady=5)

	def displayCurrentQuestion(self, quest):
		current_question = PhotoImage(file=Questions[quest])
		global current_question_label
		current_question_label = Label(self, image=current_question)
		current_question_label.image = current_question
		current_question_label.pack(in_=self.frame, pady=5)

	def displayCurrentSubQuestion(self, quest, subquest):
		current_sub_question = SubQuestions[quest][subquest]
		global current_sub_question_label
		current_sub_question_label = Label(self, text=current_sub_question)
		current_sub_question_label.pack(in_=self.frame, pady=5, ipady=5)
	
	def displayTravelButtons(self):
		# Defines button to allow return to previous question
		global previous_question_button

		# Prevents negative indexing
		if (question_number <= 0) and (sub_question_number <= 0):
			previous_question_button = Button(self, text="Previous", command=DISABLED)

		# if on first sub-question of second question, return to previous question
		elif (question_number > 0) and (sub_question_number <= 0):
			previous_question_button = Button(self, text="Previous", command=self.getPreviousQuestion)
		# otherwise return to previous subquestion
		else:
			previous_question_button = Button(self, text="Previous", command=self.getPreviousSubQuestion)
		previous_question_button.pack(side=LEFT, pady=5)

		# Defines button to proceed to next question
		global next_question_button
		# If reached final question, give feedback
		if (question_number == 1) and (sub_question_number == 2):
			next_question_button = Button(self, text="Next", command=self.giveFeedback)

		# else if reached last sub question of question proceed to next question
		elif (sub_question_number == 2) and (question_number < 1):
			next_question_button = Button(self, text="Next", command=self.getNextQuestion)
		# Otherwise proveed to next subquestion
		else:
			next_question_button = Button(self, text="Next", command=self.getNextSubQuestion)
		next_question_button.pack(side=RIGHT, pady=5)

		# Defines exit button - ends script when clicked
		global exit_button
		exit_button = Button(self, text="Exit Test", command=self.to_main)
		exit_button.pack(side=BOTTOM, pady=5)

	# Displays the appropriate radio button choices for each particular subquestion
	def displayRadioButtons(self, currentQuestion, currentSubQuestion):
		global answer1, answer2, answer3, answer4, answer5
		global currentSubQuestionAnswer
		currentSubQuestionAnswer = IntVar()		
		answer1 = Radiobutton(self, text=SubQuestionAnswers[currentQuestion][currentSubQuestion][0], value=1, variable=currentSubQuestionAnswer)
		answer2 = Radiobutton(self, text=SubQuestionAnswers[currentQuestion][currentSubQuestion][1], value=2, variable=currentSubQuestionAnswer)
		answer3 = Radiobutton(self, text=SubQuestionAnswers[currentQuestion][currentSubQuestion][2], value=3, variable=currentSubQuestionAnswer)
		answer4 = Radiobutton(self, text=SubQuestionAnswers[currentQuestion][currentSubQuestion][3], value=4, variable=currentSubQuestionAnswer)
		answer5 = Radiobutton(self, text=SubQuestionAnswers[currentQuestion][currentSubQuestion][4], value=5, variable=currentSubQuestionAnswer)
		answer1.pack(in_=self.frame, pady=5, ipady =2)
		answer2.pack(in_=self.frame, pady=5, ipady =2)
		answer3.pack(in_=self.frame, pady=5, ipady =2)
		answer4.pack(in_=self.frame, pady=5, ipady =2)
		answer5.pack(in_=self.frame, pady=5, ipady =2)
	
	# Adds value of selected radio button to student answer list at appropriate index
	def addAnswer(self, currentQuestion, currentSubQuestion, answer):
		# Debug Method
		print answer.get()
		# Puts students chosen question answer in the studentAnwswers list
		studentAnswers[currentQuestion][currentSubQuestion] = answer.get()
		#clears the value of currentSubQuestionAnswer
		currentSubQuestionAnswer = 0
		

	def getNextQuestion(self):
		global sub_question_number, question_number
		self.addAnswer(question_number, sub_question_number, currentSubQuestionAnswer)
		if question_number < 1:
			question_number += 1
		sub_question_number = 0
		self.forgetQuestionPacking()
		self.resetQuestionPacking()

	def getNextSubQuestion(self):
		global sub_question_number, question_number
		self.addAnswer(question_number, sub_question_number, currentSubQuestionAnswer)
		if sub_question_number < 2:
			sub_question_number += 1
		else:
			if sub_question_number >= 2 and question_number >= 1:
				self.giveFeedback()
			else:
				self.getNextQuestion()
		self.forgetQuestionPacking()
		self.resetQuestionPacking()

	def getPreviousQuestion(self):
		#DebugPrint
		global sub_question_number, question_number
		if question_number > 0:
			question_number -= 1
		sub_question_number = 2
		self.forgetQuestionPacking()
		self.resetQuestionPacking()
	
	def getPreviousSubQuestion(self):
		#DebugPrint
		global sub_question_number, question_number
		if sub_question_number > 0:
			sub_question_number -= 1
		self.forgetQuestionPacking()
		self.resetQuestionPacking()

	def forgetQuestionPacking(self):
		current_question_label.pack_forget()
		current_sub_question_label.pack_forget()
		answer1.pack_forget()
		answer2.pack_forget()
		answer3.pack_forget()
		answer4.pack_forget()
		answer5.pack_forget()
		previous_question_button.pack_forget()
		next_question_button.pack_forget()
		exit_button.pack_forget()

	def resetQuestionPacking(self):
		self.displayCurrentQuestion(question_number)
		self.displayCurrentSubQuestion(question_number, sub_question_number)
		self.displayRadioButtons(question_number, sub_question_number)
		self.displayTravelButtons()

	def getScore(self):
		score = 0
		for m, n in zip(studentAnswers[0], answersToQuestions[0]):
			if m == n:
				score += 1
		for m, n in zip(studentAnswers[1], answersToQuestions[1]):
			if m == n:
				score += 1
		return score
		

	def giveFeedback(self):
		self.addAnswer(question_number, sub_question_number, currentSubQuestionAnswer)
		self.forgetQuestionPacking()

		
		feedbackText = "You scored " + str(self.getScore()) + " out of 6."
		feedback_label = Label(self, text=feedbackText)
		feedback_label.pack(pady=5)
		exit_button.pack(pady=5)

	def quitWindow(self):
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
		''' centre the window in the centre of the screen on opening '''
		win_width = 600
		win_height = 725

		swidth = self.master.winfo_screenwidth()
		sheight = self.master.winfo_screenheight()

		x = (swidth - win_width)/2
		y = (sheight - win_height)/2
		self.master.geometry('%dx%d+%d+%d' % (win_width, win_height, x, y))


width, height = 600, 725	
def main():
	root = Tk()
	width, height = 600, 725
	root.geometry(str(width) + "x" + str(height))
	root.update()
	root.minsize(root.winfo_width(), root.winfo_height())
	root.configure(background="gray")
	app = PractiseLogicTest(root)
	app.mainloop()
# Questions class
class Questions:
    def __init__(self, questions): # List:questions[Class:Question]
        self.questions = questions # Type: List[Class]
        self.current_question = 0 # Type: Int
    def nextQuestion(self): # Next Question Method
        if ((self.current_question + 1) < len(self.questions)): # If there is a next question then go to it
            self.current_question += 1 # Increment current_question count by 1
            return True # Tells program if operation was successful
        return False # Tells program if operation was unsuccessful
    def previousQuestion(self): # Previous Question Method
        if ((self.current_question - 1) >= 0): # If there is a previous question then go to it
            self.current_question -= 1 # Decrement current_question count by 1
            return True # Tells program if operation was successful
        return False # Tells program if operation was unsuccessful
    def getCurrentQuestion(self):
        return self.questions[self.current_question]
    def getCurrentAnswer(self):
        return self.questions[self.current_question].getAnswer()
    def __str__(self):
        string = ""
        for question in self.questions:
            string = string + str(self.question) + "\n"
        return string

if __name__ == '__main__':
    import sys
    # Import classes from respective files and other required modules
    modules = [['Questions','*'],['Question','*'],['Answer','*'],['Tkinter','*'], ['PIL','Image, ImageTk']]
    for module in modules:
        try:
            exec('from ' + module[0] + ' import ' + module[1])
        except ImportError:
            print "Error, \"" + module[0] + "\" module not found"
            sys.exit()
    
    root = Tk()
    
    # Load intro paragraph table
    intro_paragraph_file = open('DATA\IntroParagraph.csv')
    intro_paragraph_list = []
    for line in intro_paragraph_file:
        intro_paragraph_list.append(line.split('|'))
    intro_paragraph_list.remove(intro_paragraph_list[0])
    
    # Load question table
    question_table_file = open('DATA\Questions.csv')
    question_table_list = []
    for line in question_table_file:
        question_list = line.split('|')
        diagram_link = question_list[4].split('\n')[0]
        question_table_list.append([question_list[0],question_list[1],question_list[2].split('\\'),question_list[3].split('\\'),diagram_link])
    question_table_list.remove(question_table_list[0])
    
    question_list = []
    for question in question_table_list:
        ans = Answer(question[2], question[3]) # Create Answer class
        img = ImageTk.PhotoImage(Image.open('DATA\\' + question[4]),'r')
        #img = Image.open('DATA\\' + question[4])
        que = Question(question[1], ans, img, intro_paragraph_list[int(question[0])][1]) # Create Question class
        question_list.append(que) # Add Question to question_list
    # Create Questions class
    q_class = Questions(question_list)
    
    # Display questions and answers
    print q_class.getCurrentQuestion()
    print q_class.getCurrentAnswer()
    print q_class.getCurrentQuestion().getIntroParagraph()
    while q_class.nextQuestion() == True:
        print q_class.getCurrentQuestion()
        print q_class.getCurrentAnswer()

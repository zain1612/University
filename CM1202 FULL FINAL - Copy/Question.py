# Question class
class Question:
    def __init__(self, question, answer, diagram, intro_paragraph): # String:question, Class:answer, Image:diagram, String:introParagraph
        # Question Constructor
        self.question = question # Type: String
        self.answer = answer # Type: Class
        self.diagram = diagram # Type: Image
        self.intro_paragraph = intro_paragraph # Type: String
    def saveAnswer(self, answer):
        # Set User Answer Method
        print 'Empty'
    def getQuestion(self):
        return self.question
    def getAnswer(self):
        return self.answer
    def getDiagram(self):
        return self.diagram
    def getIntroParagraph(self):
        return self.intro_paragraph
    def __str__(self):
        answer = str(self.answer)
        return "Question: " + self.question # Returns the question and correct answers

if __name__ == '__main__':
    from Answer import *
    from Tkinter import *
    from PIL import Image, ImageTk
    root = Tk()
    answer = Answer(['10 miles','11 miles','15 miles','16 miles'],['11 miles'])
    img = ImageTk.PhotoImage(Image.open('DATA\\type 1 diagram 1.png','r'))
    question = Question('What is the shortest distance from A to C?',answer,img,'The diagram below is a map showing towns called A, B, C, etc. and the roads connecting them. The roads are all one-way and cars can only travel in the direction of the arrow. Each section of road links two towns, and the number marked on the road is the distance in miles between the two towns.')
    print "question: " + str(question)
    print "getQuestion(): " + str(question.getQuestion())
    print "getAnswer(): " + str(question.getAnswer())
    print "getIntroParagraph(): " + str(question.getIntroParagraph())

from PIL import Image, ImageTk
from Questions import *
from Question import *
from Answer import *

def loadCode():
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
    return Questions(question_list)

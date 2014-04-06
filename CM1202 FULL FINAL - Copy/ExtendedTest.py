from Tkinter import *
import MainPage
import tkMessageBox

#Daniel
result_label=""

class Logic (Frame):
  # GUI Setup
  
  def __init__(self, master):
    # Initiate Questionnaire Class
    Frame.__init__(self, master)

    self.questions()
    self.grid()
    self.centre_window()
    master.protocol('WM_DELETE_WINDOW', self.check_quit)


  def compare_lists(self,q_list, results_list):
    #To check if the radio buttons are in one of the results. If so, return the number of the matching list
    
    for ctr, sub_list in enumerate(results_list):
        if sub_list == q_list:
            print "Found", ctr, sub_list
            return ctr
    return -1

  def questions(self):
    self.q1 = IntVar()

    Label(self, text="If FRIEND is coded as HUMJTK, how can CANDLE be written in that code? ", padx = 20).pack(anchor=W)

    Radiobutton(self,text="A) ECPFNG", padx = 20, variable=self.q1, value=1).pack(anchor=W)

    Radiobutton(self, text="B) ESJFME", padx = 20, variable=self.q1, value=2).pack(anchor=W)


    self.q2 = IntVar()

    Label(self, text="In a certain code ADVENTURES is written as TRDESAUVEN. How is PRODUCED written in that code ? ", justify = LEFT, padx = 20).pack(anchor=W)

    Radiobutton(self,text = "A) IUIPGSSRNP", padx = 20, variable=self.q2, value = 1).pack(anchor=W)

    Radiobutton(self,text = "B) IUIPGSRSNR", padx = 20, variable=self.q2, value = 2).pack(anchor=W)



    self.q3 = IntVar()

    Label(self, text="If FRAGRANCE is written as SBHSBODFG, how can IMPOSING be written? ", justify = LEFT, padx = 20).pack(anchor=W)

    Radiobutton(self, text = "A) NQPTJHOJ", padx = 20, variable=self.q3, value = 1).pack(anchor=W)

    Radiobutton(self, text = "B) NQPTJOHJ", padx = 20, variable=self.q3, value = 2).pack(anchor=W)


    self.q4 = IntVar()

    Label(self, text="If ROBUST is coded as QNATRS in a certain language, which word would be coded as ZXCMP? ", justify = LEFT, padx = 20).pack(anchor=W)

    Radiobutton(self, text = "A) AWDLQ", padx = 20, variable=self.q4, value = 1).pack(anchor=W)

    Radiobutton(self, text = "B) AYDNQ", padx = 20, variable=self.q4, value = 2).pack(anchor =W)

    global result_label
  
    result_label = StringVar()
    result_label.set("Good Luck in the test!")
    Label(self, textvariable=result_label).pack()
    Button(self, text = "Submit", command=self.choose).pack(anchor=N)
    Button(self, text = "Clear All", command=self.clear).pack(anchor=N)
    Button(self, text = "EXIT", command=self.to_main).pack(anchor=N)



  def choose(self):
    q_list = []
    results_list = [[1, 1, 2, 2],
                    [2, 2, 1, 1],
                    [1, 1, 1, 1],
                    [2, 2, 2, 2],
                    [2, 1, 1, 1],
                    [1, 2, 1, 1],
                    [1, 1, 2, 1],
                    [1, 1, 1, 2],
                    [1, 2, 2, 1],
                    [1, 2, 1, 2],
                    [2, 1, 1, 2],
                    [2, 1, 2, 1],
                    [2, 2, 2, 1],
                    [2, 1, 2, 2]]
    print_list = ['Congratulations you have scored the test!',
                  'You have failed!',
                  'You have passed the test! (Q1 and Q2 was correct)',
                  'You have passed the test! (Q3 and Q4 was correct)',
                  'You have failed! (Q2 was correct)',
                  'You have failed! (Q1 was correct)',
                  'You have passed the test! (Q4 was wrong)',
                  'You have passed the test! (Q3 was wrong)',
                  'You have passed the test! (Q1 and Q3 was correct)',
                  'You have passed the test! (Q1 and Q4 was correct)',
                  'You have passed the test! (Q2 and Q4 was correct)',
                  'You have passed the test! (Q2 and Q3 was correct)',
                  'You have failed! (Q3 was correct)',
                  'You have passed the test! (Q1 was wrong)']
    for var in (self.q1, self.q2, self.q3, self.q4):
        q_list.append(var.get())
    print q_list

    global result_label
    #ctr is the number of matching list and will print the same number in the print list
    ctr = self.compare_lists(q_list, results_list)
    if ctr > -1:
        result_label.set(print_list[ctr])
      
    else: result_label.set('Please answer all questions before submitting!')
        #result_label.set('You have failed the test. :(')


  def clear(self):
    self.q1.set(0)
    self.q2.set(0)
    self.q3.set(0)
    self.q4.set(0)

    global result_label
    result_label.set("Good Luck in the test!")

  def to_main(self):
    self.master.destroy()
    MainPage.main()

  def check_quit(self):
    cancel = tkMessageBox.askokcancel("Quit", " Are you sure you want to quit? \n Press OK to quit \n Press Cancel to return")
    if cancel:
      self.master.destroy()
    else:
      pass
  
  def centre_window(self):
    ''' centre the window in the centre of the screen on opening '''
    win_width = 600
    win_height = 400

    swidth = self.master.winfo_screenwidth()
    sheight = self.master.winfo_screenheight()

    x = (swidth - win_width)/2
    y = (sheight - win_height)/2
    self.master.geometry('%dx%d+%d+%d' % (win_width, win_height, x, y))


def main():
  #main
  root = Tk()
  root.title("Simple Cryptography")
  root.minsize(600,400) # To not allow resizing of the window
  root.maxsize(640,400)   # ''
  app = Logic(root)
  root.mainloop()

if __name__ == '__main__':
  main()












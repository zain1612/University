# Answer class
class Answer:
    def __init__(self, options, correct_answers): # List:options, List:correct_answers
        # Answer Constructor
        self.options = options # Type: List
        self.correct_answers = correct_answers # Type: List
        self.selected_answers = [] # Type: List
    def selectAnswer(self, answer): # int:answer
        if not self.options[answer] in self.selected_answers:
            self.selected_answers.append(self.options[answer]) # Appends answer selected to selectedAnswers list
    def removeSelectedAnswer(self, answer): # int:answer
        if self.options[answer] in self.selected_answers:
            self.selected_answers.remove(self.options[answer])
    def getSelectedAnswers(self):
        return self.selected_answers # Returns selectedAnswers variable
    def getCorrectAnswers(self):
        return self.correct_answers
    def getSelected(self, i):
        if self.options[i] in self.selected_answers:
            return 1
        return 0
    def getOptions(self):
        return self.options # Returns options variable
    def countCorrect(self):
        count = 0
        for selected_answer in self.selected_answers:
            if selected_answer in self.correct_answers:
                count += 1
            else: count -= 1
        return count
    def __str__(self):
        return "Answer: " + str(self.correct_answers)

if __name__ == '__main__':
    answer = Answer(['A','B','C','D','E'],['A','C'])
    print "answer: " + str(answer)
    print "answer.getSelectedAnswers(): " + str(answer.getSelectedAnswers())
    print "answer.selectAnswer(0) # 0 = 'A'"
    answer.selectAnswer(0) # 0 = 'A'
    print "answer.getSelectedAnswers(): " + str(answer.getSelectedAnswers())
    print "answer.getOptions(): " + str(answer.getOptions())
    print "answer.countCorrect(): " + str(answer.countCorrect())
    print "answer.selectAnswer(2) # 2 = 'C'"
    answer.selectAnswer(2) # 2 = 'C'
    print "answer.countCorrect(): " + str(answer.countCorrect())
    print "answer.selectAnswer(3) # 3 = 'D'"
    answer.selectAnswer(3) # 3 = 'D'
    print "answer.countCorrect(): " + str(answer.countCorrect())
    print "answer.getSelectedAnswers(): " + str(answer.getSelectedAnswers())
    print "answer.getSelected(0) # 0 = 'A': " + str(answer.getSelected(0))
    print "answer.getSelected(1) # 1 = 'B': " + str(answer.getSelected(1))

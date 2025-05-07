from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox,QRadioButton, QPushButton,QLabel, QButtonGroup
from random import shuffle, randint # NEW








class Question():
  ''' contains the question, one correct answer and three incorrect answers'''
  def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
      # all the lines must be given when creating the object, and will be recorded as properties
      self.question = question
      self.right_answer = right_answer
      self.wrong1 = wrong1
      self.wrong2 = wrong2
      self.wrong3 = wrong3






questions_list = []
questions_list.append(Question('The state language of Brazil', 'Portuguese', 'English', 'Spanish', 'Brazilian'))
questions_list.append(Question('Which color does not appear on the American flag?', 'Green', 'Red', 'White', 'Blue'))
questions_list.append(Question('A traditional residence of the Yakut people', 'Urasa', 'Yurt', 'Igloo', 'Hut'))




app = QApplication([])




window = QWidget()
window.setWindowTitle("Memo Card")




btn_OK = QPushButton("Answer")
lb_Question = QLabel("The most difficult question in the world!")




#Radio Group Box ----------
RadioGroupBox = QGroupBox("Answer options")
rbtn_1 = QRadioButton("Option 1")
rbtn_2 = QRadioButton("Option 2")
rbtn_3 = QRadioButton("Option 3")
rbtn_4 = QRadioButton("Option 4")




layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()




layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)




layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)




RadioGroupBox.setLayout(layout_ans1)
#------------------------------




#AnsGroupBox ------------------
AnsGroupBox = QGroupBox("Test result")
lb_Result = QLabel ("you are correct or not")
lb_Correct = QLabel("the correct answer")




layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result)
layout_res.addWidget(lb_Correct)




AnsGroupBox.setLayout(layout_res)
#------------------------------




layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()




layout_line1.addWidget(lb_Question, alignment = Qt.AlignCenter )
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()




layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch = 1)
layout_line3.addStretch(1)




layout_card = QVBoxLayout()




layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)




window.setLayout(layout_card)








def show_result():
  ''' show answer panel '''
  RadioGroupBox.hide()
  AnsGroupBox.show()
  btn_OK.setText('Next question')




RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)








def show_question():
  ''' show question panel '''
  RadioGroupBox.show()
  AnsGroupBox.hide()
  btn_OK.setText('Answer')
  RadioGroup.setExclusive(False) # remove limits in order to reset radio button selection
  rbtn_1.setChecked(False)
  rbtn_2.setChecked(False)
  rbtn_3.setChecked(False)
  rbtn_4.setChecked(False)
  RadioGroup.setExclusive(True) # bring back the limits so only one radio button can be selected








answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]




def ask(q: Question):
  ''' This function writes the value of the question and answers in the corresponding widgets. The answer options are distributed randomly. '''
  shuffle(answers) # shuffle the list of buttons; now a random button is first in the list
  answers[0].setText(q.right_answer) # fill the first element of the list with the correct answer and the other elements with incorrect answers
  answers[1].setText(q.wrong1)
  answers[2].setText(q.wrong2)
  answers[3].setText(q.wrong3)
  lb_Question.setText(q.question) # question
  lb_Correct.setText(q.right_answer) # answer
  show_question() # show question panel








def show_correct(res):
  ''' show result - put the written text into "result" and show the corresponding panel '''
  lb_Result.setText(res)
  show_result()




def check_answer():
  ''' if an answer option was selected, check and show answer panel '''
  if answers[0].isChecked():
      show_correct('Correct!')
      #[4] NEW -----
      window.score += 1
      # ---------
  else:
      if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
          show_correct('Incorrect!')
   #[5] NEW ---------
  print('Statistics\n-Total questions: ', window.total, '\n-Right answers: ', window.score)
  print('Rating: ', (window.score/window.total*100), '%')
   # ------------




def next_question():
  ''' Asks the next question in the list. '''
  #[3] NEW ---------
  window.total += 1
  cur_question = randint(0, len(questions_list) - 1)
  # -----------


  #[2] DELETE  --------
  #window.cur_question = window.cur_question + 1 # move on to the next question
  #if window.cur_question >= len(questions_list):
      #window.cur_question = 0 # if the list of questions has ended, start over
  # ----------------


  q = questions_list[cur_question] # take a question
  ask(q) # ask it




def click_OK():
  ''' This determines whether to show another question or check the answer to this question. '''
  if btn_OK.text() == 'Answer':
      check_answer()
  else:
      next_question()




window.cur_question = -1
btn_OK.clicked.connect(click_OK)




#[1] NEW ------------
window.score = 0
window.total = 0
# ---------------


next_question()
window.show()
app.exec_()

import sys
import random
from util import *
from time import sleep
from pygame import mixer
from ques_and_ans import *
from endgame import Ui_endGame
from homescreen import Ui_HomeScreen
from mainscreen import Ui_MainWindow
from PyQt5 import QtWidgets,QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow

mixer.init()
sound = mixer.music

score = 0
high = 0
username = ""



class homescreen(QMainWindow):
	def __init__(self):
		super(homescreen, self).__init__()

		self.ui = Ui_HomeScreen()
		self.ui.setupUi(self)
		self.setWindowTitle('Questions')

		self.ui.playButton.clicked.connect(self.play)

	def play(self):
		if self.ui.usernameField.text().strip() == "":
			self.ui.userError.setText("Please enter a username")

		elif len(self.ui.usernameField.text().strip()) > 10:
			self.ui.userError.setText("Username less than 10 chars")

		else:
			global username
			username = self.ui.usernameField.text().strip()
			self.main = main()
			self.main.show()
			self.close()


class main(QMainWindow):
	def __init__(self):
		super(main, self).__init__()

		global high
		
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowTitle('Questions')
		
		self.tries = 2
		self.worth = 100
		self.ans = ""
		self.count = 0
		
		self.questions, self.answers, self.h_user, self.h_score = get_data()
		high = self.h_score
		
		self.question()

		self.ui.pushButtonA.clicked.connect(lambda:self.answer(self.ui.pushButtonA))
		self.ui.pushButtonB.clicked.connect(lambda:self.answer(self.ui.pushButtonB))
		self.ui.pushButtonC.clicked.connect(lambda:self.answer(self.ui.pushButtonC))
		self.ui.pushButtonD.clicked.connect(lambda:self.answer(self.ui.pushButtonD))


	def question(self):
		index = gen_random_number()
		global score
		
		if self.count == 20:
			self.end = endGame()
			self.end.show()
			self.close()

		self.ui.tries.setText("Tries: " + str(self.tries))
		self.ui.questionWorth.setText("Worth: " + str(self.worth))
		self.ui.score.setText(f"Score - {username}: " + str(score))
		self.ui.highScore.setText(f"Highscore - {self.h_user}: {self.h_score}")
		self.ui.questionField.setText(generate_question(self.questions,index))



		self.dic, self.ans = generate_answers(self.answers,index)
		self.ui.pushButtonA.setText('A.' + self.dic['a'])
		self.ui.pushButtonB.setText('B.' + self.dic['b'])
		self.ui.pushButtonC.setText('C.' + self.dic['c'])
		self.ui.pushButtonD.setText('D.' + self.dic['d'])
		self.count += 1
				


	def answer(self,button):
		global score
		global sound

		if button.text()[2:] == self.ans:
			sound.load('../files/correctSound.mp3')
			sound.play()
			score += self.worth
			self.worth += 100
			self.question()

		else:
			if self.tries == 0:
				self.end = endGame()
				self.end.show()
				self.close()
			else:
				sound.load('../files/wrongSound.mp3')
				sound.play()
				score -= self.worth
				self.tries -= 1
				self.question()



class endGame(QMainWindow):
	def __init__(self):
		super(endGame, self).__init__()

		self.ui = Ui_endGame()
		self.ui.setupUi(self)
		self.checkHighScore()

		self.ui.newGameButton.clicked.connect(self.new)
		self.ui.quitGameButton.clicked.connect(self.quit)

	def checkHighScore(self):
		global score
		global high
		global username

		if score > high:
			fob = open('../files/highscore.txt','w')
			fob.write(username+"\n")
			fob.write(str(score))
			fob.close
			self.ui.endLabel.setText("Congratulations New Highscore!!!")

	def new(self):
		global score
		score = 0
		self.main = main()
		self.main.show()
		self.close()

	def quit(self):
		sys.exit(app.exec_())

if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = homescreen()
	win.show()
	sys.exit(app.exec_())
import random


def get_data():
	try:
		qob = open('../files/questions.txt','r')
		questions = qob.readlines()
		qob.close()
	except:
		print("Question file missing")

	try:
		aob = open('../files/answers.txt','r')
		answers = aob.readlines()
		aob.close()
	except:
		print("Answer file missing")

	try:
		hob = open('../files/highscore.txt','r+')
		hs_data = hob.readlines()
		h_user = hs_data[0].strip("\n")
		h_score = int(hs_data[1])
	except:
		h_user = "None"
		h_score = 0

	return questions, answers, h_user, h_score


def gen_random_number():
	return random.randint(0,30)
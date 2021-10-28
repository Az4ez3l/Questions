import random


# generate and display question
def generate_question(questions,index):
	temp = questions[index]
	questions.pop(index)
	return temp

# generate and display possible answers, return correct answer
def generate_answers(answers,index):
	answer = answers[index].strip("\n").split(",")
	answers.pop(index)
	ans = answer[0]
	random.shuffle(answer)
	
	dic = {
		"a": answer[0],
		"b": answer[1],
		"c": answer[2],
		"d": answer[3]
		}
	
	return dic, ans
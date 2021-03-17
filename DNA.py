import string
import random
alphabets= list(string.ascii_lowercase)
white_space=list(string.whitespace)
alphabets.append(white_space[0])
def newChar():
	global alphabets
	letter=random.choice(alphabets)
	return letter
def newChar_nospace():
	alphabets= list(string.ascii_lowercase)
	letter=random.choice(alphabets)
	return letter	
class DNA:
	def __init__(self,num):
		self.genes = []
		self.fitness = 0 
		for i in range(num):
			self.genes.append(newChar())
	#cHECK IF SELF.GENES HAS TO BE CONVERTED TO A STRING
	def getPhrase(self):
		return "".join(self.genes)
		

	def calculateFitness(self,target):
		score = 0
		for i in range(len(self.genes)):
			if self.genes[i] == target[i]:
				score+=1

		self.fitness = score/len(target)

	def crossover(self,partner):
		child = DNA(len(self.genes))

		midpoint = random.randint(0,len(self.genes)-1)

		#CHECK HERE IF YOU HAVE TO USE THE REPLACE METHOD
		for i in range(len(self.genes)):
			if i > midpoint:
				# x = self.genes.replace(self.genes[i],newChar())
				child.genes[i] = self.genes[i]
			else:
				child.genes[i] = partner.genes[i]

		return child
		
	def mutate(self,mutation_rate,target):
		global white_space
		for i in range(len(self.genes)):
			if random.uniform(0,1)<mutation_rate:
				if self.genes[i]==target[i]:
					continue
				else:		
					if self.genes[i]== white_space[0]:
						self.genes[i] = newChar()
					else:
						self.genes[i]=newChar()
				



	
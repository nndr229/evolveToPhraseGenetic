import math
from DNA import DNA
import random

def map(n, start1, stop1, start2, stop2):
     return ((n-start1)/(stop1-start1))*(stop2-start2)+start2

class Population:
	def __init__(self,p,m,num):
		self.population = []
		self.matingPool = []
		self.generations = 0
		self.finished = False
		self.target = p
		self.mutationRate = m
		self.perfectScore = 1

		self.best = ""

		for i in range(num):
			self.population.append(DNA(len(self.target)))

		self.calcFitness()

	def calcFitness(self):
		for i in range(len(self.population)):
			self.population[i].calculateFitness(self.target)


	def naturalSelection(self):
		"""for (let i = 0; i < this.population.length; i++) {
      if (this.population[i].fitness > maxFitness) {
        maxFitness = this.population[i].fitness;
      }
    }"""
		self.matingPool = []

		maxFitness = 0

		for i in range(len(self.population)):
			if self.population[i].fitness >maxFitness:
				maxFitness=self.population[i].fitness

		for i in range(len(self.population)):
			fitness = map(self.population[i].fitness,0,maxFitness,0,1)
			n = math.floor(fitness*100)

			for j in range(0,n):
				self.matingPool.append(self.population[i])


	def generate(self):
		for i in range(len(self.population)):
			a = random.randint(0,len(self.matingPool)-1)
			b = random.randint(0,len(self.matingPool)-1)

			partnerA = self.matingPool[a]
			partnerB = self.matingPool[b]

			child = partnerA.crossover(partnerB)
			child.mutate(self.mutationRate,self.target)
			self.population[i] = child

		self.generations += 1
		

	def getBest(self):
		return self.best

	def evaluate(self):
		worldrecord = 0.0
		index = 0

		for i in range(len(self.population)):
			self.best = self.population[index].getPhrase()
			if self.best == self.target:
				print(self.best)
				self.finished = True
				break

	def isFinished(self):
		return self.finished

	def getGenerations(self):
		return self.generations

	def getAverageFitness(self):
		total = 0
		for i in range(len(self.population)):
			total += self.population[i].fitness

		return total/(len(self.population))
		
	def allPhrases(self):
		everything = ""
		displayLimit = min(len(self.population),50)

		for i in range(displayLimit):
			everything += self.population[i].getPhrase() + "\n"
		return everything	




	

























































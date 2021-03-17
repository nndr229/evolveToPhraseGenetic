from DNA import DNA
from population import Population

def runPhraseGenerator():
	target = "to be or not to be that is the question";
	popmax = 1000;
	mutationRate = 0.01;

	# // Create a population with a target phrase, mutation rate, and population max
	population = Population(target, mutationRate, popmax)

	while True:
		population.naturalSelection();
		# //Create next generation
		population.generate();
		# // Calculate fitness
		population.calcFitness();

		population.evaluate();
		if population.isFinished():
			print(population.isFinished())
			break

		print(population.getBest())





runPhraseGenerator()

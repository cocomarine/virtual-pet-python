HUNGER_INCREMENT = 5
HUNGER_DECREMENT = 3
FITNESS_INCREMENT = 4
FITNESS_DECREMENT = 3

MAXIMUM_HUNGER = 10
MAXIMUM_FITNESS = 10
MAXIMUM_AGE = 30


class Pet:
	def __init__(self, name):
		self.name = name
		self.age = 0
		self.hunger = 0
		self.fitness = MAXIMUM_FITNESS
		self.children = []

	def is_alive(self):
		return self.fitness > 0 and self.hunger < MAXIMUM_HUNGER and self.age < MAXIMUM_AGE

	def grow_up(self):
		if not self.is_alive():
			raise Exception('Your pet is no longer alive :(')
		self.age += 1
		self.age = min(self.age, MAXIMUM_AGE)
		self.hunger += HUNGER_INCREMENT
		self.hunger = min(self.hunger, MAXIMUM_HUNGER)
		self.fitness -= FITNESS_DECREMENT
		self.fitness = max(self.fitness, 0)




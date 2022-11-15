import unittest
from pet import Pet

HUNGER_INCREMENT = 5
HUNGER_DECREMENT = 3
FITNESS_INCREMENT = 4
FITNESS_DECREMENT = 3

MAXIMUM_HUNGER = 10
MAXIMUM_FITNESS = 10
MAXIMUM_AGE = 30

class TestPet(unittest.TestCase):
	def setUp(self):
		self.fido = Pet("Fido")

	def test_is_object(self):
		message = "given object is not instance of Pet"
		self.assertIsInstance(self.fido, Pet, message)

	def test_has_name(self):
		self.assertEqual(self.fido.name, "Fido")

	def test_initial_age_0(self):
		self.assertEqual(self.fido.age, 0)

	def test_initial_hunger_0(self):
		self.assertEqual(self.fido.hunger, 0)


class TestIsAlive(unittest.TestCase):
	def setUp(self):
		self.fido = Pet("Fido")

	def test_alive(self):
		self.assertTrue(self.fido.is_alive())

	def test_dead_due_to_unfitness(self):
		self.fido.fitness = -2
		self.fido.age = 10
		self.fido.hunger = 2
		self.assertFalse(self.fido.is_alive())

	def test_dead_due_to_hunger(self):
		self.fido.hunger = 12
		self.fido.age = 10
		self.fido.fitness = 8
		self.assertFalse(self.fido.is_alive())

	def test_dead_due_to_old_age(self):
		self.fido.hunger = 2
		self.fido.age = 32
		self.fido.fitness = 8
		self.assertFalse(self.fido.is_alive())


class TestGrowUp(unittest.TestCase):
	def setUp(self):
		self.fido = Pet("Fido")
		self.fido.grow_up()

	def test_age_by_1(self):
		self.assertEqual(self.fido.age, 1)

	def test_increase_hunger_by_5(self):
		self.assertEqual(self.fido.hunger, 5)

	def test_throw_error_when_dead(self):
		self.fido.age = MAXIMUM_AGE
		with self.assertRaises(Exception):
			self.fido.grow_up()



if __name__ == '__main__':
	unittest.main()

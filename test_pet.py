import unittest
from pet import Pet


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





# class TestGrowUp(unittest.TestCase):
# 	def setUp(self):
# 		self.fido = Pet("Fido")
#
# 	def test_increase_age(self):


if __name__ == '__main__':
	unittest.main()

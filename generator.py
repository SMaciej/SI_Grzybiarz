class Map:
	"""Klasa mapy."""

	def __init__(self, x_dimension, y_dimension):
		self.tiles = [[0 for x in range(x_dimension)] for y in range(y_dimension)]

	def generate(self):
		for rows in self.tiles:
			for tile in rows:
				print tile


class Tree:
	"""Podany gatunek drzewa."""

	def __init__(self, tree_species):
		self.species_name = tree_species

	def type(self):
		"""Zwraca typ obiektu."""
		return self.__class__.__name__

	def species(self):
		"""Zwraca gatunek obiektu."""
		return self.species_name


class Mushroom:
	"""Podany gatunek grzyba."""

	def __init__(self, mushroom_species):
		self.species_name = mushroom_species

	def type(self):
		"""Zwraca typ obiektu."""
		return self.__class__.__name__

	def species(self):
		"""Zwraca gatunek obiektu."""
		return self.species_name


class Ground:
	"""Podany rodzaj gruntu."""

	def __init__(self, ground_species):
		self.species_name = ground_species

	def type(self):
		"""Zwraca typ obiektu."""
		return self.__class__.__name__

	def species(self):
		"""Zwraca gatunek obiektu."""
		return self.species_name


mapa = Map(5, 5)
mapa.generate()
drzewo = Tree("brzoza")
print drzewo.type()
print drzewo.species()

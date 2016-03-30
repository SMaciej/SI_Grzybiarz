import random


class Map:
	"""Klasa mapy."""

	def __init__(self, x_dimension, y_dimension):
		self.tiles = [[Ground("trawa") for x in range(x_dimension)] for y in range(y_dimension)]

	def generate(self):
		"""Generuje mape."""

		# Przechodzimy po naszej macierzy, generując odpowiednie elementy.
		for rows_index, rows in enumerate(self.tiles):
   			for columns_index, tile in enumerate(rows):
   				self.insert_tree(rows_index, columns_index, 50)
   				# TUTAJ DODAC LOSOWANIE DODATKOWYCH ELEMENTOW


   	def insert_tree(self, rows, columns, probability):
   		"""Sprawdza, czy w danym miejscu mozna umiescic drzewo, jesli tak to umieszcza je tam z podanym prawdopodobienstwem."""
   		
   		if self.check_neighbors(rows, columns, 'Tree', 3):
   			if random.randint(0,100) <= probability:
   				# TUTAJ DODAC LOSOWANIE GATUNKU:
   				self.tiles[rows][columns] = Tree('brzoza')

   	def print_map(self):
   		"""Drukuje mape w czytelnej formie."""

   		for rows in self.tiles:
   			for i in range(0, len(rows)):
   				print rows[i].symbol(),
   			print "\n"

   	def check_neighbors(self, r, c, type, dist):
   		"""Funkcja pomocnicza sprawdzajaca sasiadow danego typu w podanej odleglosci."""

   		while dist > 0:
   			try:
		   		if  	self.tiles[r+dist][c].type() != type and \
		   				self.tiles[r-dist][c].type() != type and \
		   				self.tiles[r][c+dist].type() != type and \
		   				self.tiles[r][c-dist].type() != type and \
		   				self.tiles[r+dist][c+dist].type() != type and \
		   				self.tiles[r-dist][c+dist].type() != type and \
		   				self.tiles[r+dist][c-dist].type() != type and \
		   				self.tiles[r-dist][c-dist].type() != type:
	   				dist = dist - 1
	   			else:
	 				return False
	 			
	   		except:
	   			return False
	   	return True


class Tree:
	"""Podany gatunek drzewa."""

	def __init__(self, tree_species):
		acceptable_species = ['brzoza', 'dab', 'swierk']
		if tree_species in acceptable_species:
			self.species_name = tree_species
		else:
			raise NameError('Taki gatunek drzewa nie istnieje.')

	def type(self):
		"""Zwraca typ obiektu."""
		return self.__class__.__name__

	def species(self):
		"""Zwraca gatunek obiektu."""
		return self.species_name

	def symbol(self):
		"""Zwraca symbol obiektu na mapie"""
		if self.species_name == 'brzoza':
			return "B"


class Mushroom:
	"""Podany gatunek grzyba."""

	def __init__(self, mushroom_species):
		self.species_name = mushroom_species
		acceptable_species = ['maslak']
		if mushroom_species in acceptable_species:
			self.species_name = mushroom_species
		else:
			raise NameError('Taki gatunek grzyba nie istnieje.')

	def type(self):
		"""Zwraca typ obiektu."""
		return self.__class__.__name__

	def species(self):
		"""Zwraca gatunek obiektu."""
		return self.species_name

	def symbol(self):
		"""Zwraca symbol obiektu na mapie"""
		if self.species_name == 'maslak':
			return "M"


class Ground:
	"""Podany rodzaj gruntu."""

	def __init__(self, ground_species):
		acceptable_species = ['trawa', 'mech']
		if ground_species in acceptable_species:
			self.species_name = ground_species
		else:
			raise NameError('Taki rodzaj gruntu nie istnieje.')

	def type(self):
		"""Zwraca typ obiektu."""
		return self.__class__.__name__

	def species(self):
		"""Zwraca gatunek obiektu."""
		return self.species_name

	def symbol(self):
		"""Zwraca symbol obiektu na mapie"""
		if self.species_name == 'trawa':
				return "."


mapa = Map(30, 30)
mapa.generate()
mapa.print_map()
# drzewo = Tree("brzoza")
# print drzewo.type()
# print drzewo.species()
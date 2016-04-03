import random


class Map:
	"""Klasa mapy."""

	def __init__(self, x_dimension, y_dimension):
		self.tiles = [[Ground("trawa") for x in range(x_dimension)] for y in range(y_dimension)]

	def generate(self):
		"""Generuje mape."""

		# Przechodzimy po naszej macierzy, generujac odpowiednie elementy.
		for rows_index, rows in enumerate(self.tiles):
   			for columns_index, tile in enumerate(rows):
   				self.insert_tree(rows_index, columns_index, 'brzoza', 3, 30)
   				self.insert_tree(rows_index, columns_index, 'dab', 3, 20)
   				self.insert_tree(rows_index, columns_index, 'swierk', 3, 10)
   				self.insert_ground(rows_index, columns_index, 'mech', 1, 60)
   				self.insert_mushroom(rows_index, columns_index, 'maslak', 1, 15)
   				self.insert_mushroom(rows_index, columns_index, 'pieprznik', 1, 10)

   				# TUTAJ DODAC LOSOWANIE DODATKOWYCH ELEMENTOW


   	def insert_tree(self, rows, columns, species, gap, probability):
   		"""Sprawdza, czy w danym miejscu mozna umiescic drzewo (z podanym odstepem od innych drzew), jesli tak to umieszcza je tam z podanym prawdopodobienstwem."""
   		
   		if self.check_neighbors(rows, columns, 'Tree', gap) == True and self.check_neighbors(rows, columns, 'Tree', gap) != 'found':
   			if random.randint(0,100) <= probability:
   				self.tiles[rows][columns] = Tree(species)

   	def insert_ground(self, rows, columns, species, gap, probability):
   		"""Sprawdza, czy w danym miejscu mozna umiescic obiekt gruntu, jesli tak to umieszcza go tam z podanym prawdopodobienstwem."""
   		
   		if self.check_neighbors(rows, columns, 'Tree', gap) == 'found':
   			if random.randint(0,100) <= probability:
   				self.tiles[rows][columns] = Ground(species)

   	def insert_mushroom(self, rows, columns, species, gap, probability):
   		"""Sprawdza, czy w danym miejscu mozna umiescic obiekt gruntu, jesli tak to umieszcza go tam z podanym prawdopodobienstwem."""
   		
   		if self.check_neighbors(rows, columns, 'Tree', gap) == 'found':
   			if random.randint(0,100) <= probability:
   				self.tiles[rows][columns] = Mushroom(species)

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
	 				return 'found'
	 			
	   		except:
	   			return False
	   	return True


class Tree:
	"""Podany gatunek drzewa."""

	def __init__(self, tree_species):
		acceptable_species = {'brzoza':'B', 'dab':'D', 'swierk':'S'}
		if tree_species in acceptable_species:
			self.species_name = tree_species
			self.species_symbol = acceptable_species[tree_species]
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
		return self.species_symbol


class Mushroom:
	"""Podany gatunek grzyba."""

	def __init__(self, mushroom_species):
		acceptable_species = {'maslak':'m', 'pieprznik':'p'}
		if mushroom_species in acceptable_species:
			self.species_name = mushroom_species
			self.species_symbol = acceptable_species[mushroom_species]
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
		return self.species_symbol


class Ground:
	"""Podany rodzaj gruntu."""

	def __init__(self, ground_species):
		acceptable_species = {'trawa':'.', 'mech':'+'}
		if ground_species in acceptable_species:
			self.species_name = ground_species
			self.species_symbol = acceptable_species[ground_species]
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
		return self.species_symbol


mapa = Map(30, 30)
mapa.generate()
mapa.print_map()
# drzewo = Tree("brzoza")
# print drzewo.type()
# print drzewo.species()
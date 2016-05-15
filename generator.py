import random
from objects import Tree, Mushroom, Ground
from config import trees, mushrooms, ground

class Map:
    """Klasa mapy."""

    def __init__(self, x_dimension, y_dimension):
        # Umieszcza trawe w pustych miejscach.
        self.tiles = [[Ground('trawa') for x in range(x_dimension)] for y in range(y_dimension)]

    def generate(self):
        """Generuje mape tworzac poszczegolne obiekty."""

        for rows_index, rows in enumerate(self.tiles):
            for columns_index, tile in enumerate(rows):
                for species in trees:
                    self.insert_tree(rows_index, columns_index, species, 3, trees[species]['probability'])
                for species in ground:
                    if species == 'trawa':
                        pass
                    else:
                        self.insert_ground(rows_index, columns_index, species, 1, ground[species]['probability'])
                for species in mushrooms:
                    self.insert_mushroom(rows_index, columns_index, species, 1, mushrooms[species]['probability'])


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
                if      self.tiles[r+dist][c].type() != type and \
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



mapa = Map(30, 30)
mapa.generate()
mapa.print_map()
# drzewo = Tree("brzoza")
# print drzewo.type()
# print drzewo.species()
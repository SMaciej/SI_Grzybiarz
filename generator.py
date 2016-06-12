import random, pickle
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
        
        # Drzewa umieszczane sa w odpowiedniej (zaleznym od atrybutu 'gap') odleglosci od siebie
        check = self.check_neighbors(rows, columns, 'Tree', gap)
        if check == True and type(check) is not list:
            if random.randint(0,100) <= probability:
                self.tiles[rows][columns] = Tree(species)

    def insert_ground(self, rows, columns, species, gap, probability):
        """Sprawdza, czy w danym miejscu mozna umiescic obiekt gruntu, jesli tak to umieszcza go tam z podanym prawdopodobienstwem."""
        
        # Obiekt gruntu umieszczany jest w sasiedztwie (zaleznym od atrybutu 'gap') drzew.
        check = self.check_neighbors(rows, columns, 'Tree', gap)
        if type(check) is list:
            if random.randint(0,100) <= probability:
                self.tiles[rows][columns] = Ground(species)

    def insert_mushroom(self, rows, columns, species, gap, probability):
        """Sprawdza, czy w danym miejscu mozna umiescic obiekt grzyba, jesli tak to umieszcza go tam z podanym prawdopodobienstwem."""

        # Grzyby umieszczane sa w sasiedztwie (zaleznym od atrybutu 'gap') drzew.
        check = self.check_neighbors(rows, columns, 'Tree', gap)
        if type(check) is list:
            if self.check_favorite(check, species):  # Sprawdza, czy w poblizu miejsca wybranego na grzyba znajduje sie jego ulubione drzewo.
                probability += 20                       # Jesli tak, to zwieksza prawdopodobienstwo wystapienia grzyba.
            if random.randint(0,100) <= probability:        # Ostatecznie umieszcza grzyba z obliczonym prawdopodobienstwem.
                self.tiles[rows][columns] = Mushroom(species)

    def print_map(self):
        """Drukuje mape w czytelnej formie."""

        for rows in self.tiles:
            for i in range(0, len(rows)):
                print(rows[i].symbol())
            print("\n")

    def print_to_file(self, file_name):
        """Drukuje mape do pliku o podanej nazwie."""

        f = open('./' + file_name, 'w+')

        for rows in self.tiles:
            for i in range(0, len(rows)):
                f.write(rows[i].symbol())
            f.write("\n")

    def save_to_file(self, file_name):
        """Zapisuje mape do pliku o podanej nazwie."""

        f = open('./' + file_name, 'w+')

        pickle.dump(self, open('./' + file_name + '.p', 'wb'))

    def check_neighbors(self, r, c, type, dist):
        """Funkcja pomocnicza sprawdzajaca sasiadow danego typu w podanej odleglosci."""

        neighbors = []
        t = self.tiles
        while dist > 0:
            try:
                if t[r+dist][c].type() == type:
                    neighbors.append(t[r+dist][c])
                if t[r-dist][c].type() == type:
                    neighbors.append(t[r-dist][c])
                if t[r][c+dist].type() == type:
                    neighbors.append(t[r][c+dist])
                if t[r][c-dist].type() == type:
                    neighbors.append(t[r][c-dist])
                if t[r+dist][c+dist].type() == type:
                    neighbors.append(t[r+dist][c+dist])
                if t[r-dist][c+dist].type() == type:
                    neighbors.append(t[r-dist][c+dist])
                if t[r+dist][c-dist].type() == type:
                    neighbors.append(t[r+dist][c-dist])
                if t[r-dist][c-dist].type() == type:
                    neighbors.append(t[r-dist][c-dist])
                dist = dist -1
            except:
                return False

        if neighbors:
            return neighbors
        else:
            return True

    def check_favorite(self, neighbors, species):
        """Funkcja pomocnicza sprawdzajaca, czy w sasiedztwie grzyba znajduje sie jego ulubione drzewo."""

        for neighbor in neighbors:
            if neighbor == mushrooms[species]['favorite_tree']:
                return True
            else:
                return False



<<<<<<< HEAD
mapa = Map(25, 25)
mapa.generate()
#mapa.print_map()
<<<<<<< HEAD
mapa.print_to_file('map.txt')
=======
mapa.print_to_file('map')
=======
#mapa = Map(8, 8)
#mapa.generate()
#mapa.print_map()
#mapa.save_to_file('map')
>>>>>>> origin/master
>>>>>>> origin/master

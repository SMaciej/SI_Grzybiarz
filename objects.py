import json
from config import trees, mushrooms, ground


class Tree:
    """Podany gatunek drzewa."""

    def __init__(self, tree_species):
        acceptable_species = trees
        if tree_species in acceptable_species:
            self.species_name = tree_species
            self.species_data = acceptable_species[tree_species]
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
        return self.species_data['symbol']


class Mushroom:
    """Podany gatunek grzyba."""

    def __init__(self, mushroom_species):
        acceptable_species = mushrooms
        if mushroom_species in acceptable_species:
            self.species_name = mushroom_species
            self.species_data = acceptable_species[mushroom_species]
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
        return self.species_data['symbol']


class Ground:
    """Podany rodzaj gruntu."""

    def __init__(self, ground_species):
        acceptable_species = ground
        if ground_species in acceptable_species:
            self.species_name = ground_species
            self.species_data = acceptable_species[ground_species]
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
        return self.species_data['symbol']



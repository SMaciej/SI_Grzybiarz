import pygame, sys
from pygame.locals import *
from objects import Tree, Mushroom, Ground
from config import trees, mushrooms, ground
from Ekran2 import Ekran
from generator import Map

RES = 7
TILE = 24

mapa = Map(RES, RES)
mapa.generate()
#mapa.print_map()
mapa.print_to_file('map')

Ekran(RES*TILE, RES*TILE, RES)


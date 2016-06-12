import pygame
from pygame.locals import *
import sys

class Ekran(object):
    def __init__(self,Xres,Yres):
        pygame.init()
        flag = DOUBLEBUF

        # bufor grafiki
        self.surface = pygame.display.set_mode((Xres,Yres),flag)
        # zmienna stanu programu (1 -run, 0 - exit)
        self.state = 1
        self.loadGraphic()
        self.mapa = self.loadmap("map")
        self.mainloop()

    def progExit(self):
        exit()

    def mainloop(self):
        while self.state == 1:
            for event in pygame.event.get():
                if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                    self.state=0
            print(event)
            self.surface.fill((0,0,0))
            self.drawMap(self.mapa)
            pygame.display.flip()
        self.progExit()

    def loadGraphic(self):
        self.tiles = {}
        self.tiles['B'] = pygame.image.load('tree.brzoza.png')
        self.tiles['D'] = pygame.image.load('tree.dab.png')
        self.tiles['S'] = pygame.image.load('tree.swierk.png')
        self.tiles['u'] = pygame.image.load('mush.uszak.png')
        self.tiles['s'] = pygame.image.load('mush.sromotnik.png')
        self.tiles['p'] = pygame.image.load('mush.piepsznik.png')
        self.tiles['h'] = pygame.image.load('mush.muchomor.png')
        self.tiles['m'] = pygame.image.load('mush.maslak.png')
        self.tiles['l'] = pygame.image.load('mush.lysiczka.png')
        self.tiles['c'] = pygame.image.load('mush.czubajka.png')
        self.tiles['.'] = pygame.image.load('map.trawa.png')
        self.tiles['+'] = pygame.image.load('map.mech.png')

    def loadmap(self,mapa):
        mapa = open(mapa, 'r')
        tab1 = []
        for line in mapa:
            tab2 = []
            for i in range(len(line[:-1])):
                tab2.append(line[i])
            tab1.append(tab2)
        return tab1

    def drawMap(self,mapa):
        Ydam = 0
        for line in mapa:
            Xdam = 0
            for symbol in line:
                self.surface.blit(self.tiles[symbol], (Xdam,Ydam))
                Xdam += 24
            Ydam += 24
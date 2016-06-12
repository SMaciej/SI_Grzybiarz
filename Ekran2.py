import pygame
from pygame.locals import *
import sys
from getmap import *

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
        self.mapa2 = self.loadmap("map")
        self.loadDict()
        self.cursor = (0,0)

        self.mainloop()

    def progExit(self):
        exit()

    def mainloop(self):
        while self.state == 1:
            for event in pygame.event.get():
                if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                    self.state=0
            self.cursor = self.printPosition(event,self.mapa,self.cursor)
            self.surface.fill((0,0,0))
            self.drawMap(self.mapa)
            self.rysujPostac((19,19))
            self.drawTrees(self.mapa)			#wyswietlanie koron drzew
            pygame.display.flip()
            pygame.time.wait(2000)
		

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
        self.korona = {}
        self.korona['B'] = pygame.image.load('tree.brzoza.top.png')
        self.korona['D'] = pygame.image.load('tree.dab.top.png')
        self.korona['S'] = pygame.image.load('tree.swierk.top.png')
        self.grzybman = pygame.image.load('char.grzybiarz.png')

    def loadDict(self):
        self.dict = {}
        self.dict['B'] = ["Drzewo","Brzoza"]
        self.dict['D'] = ["Drzewo","Dab"]
        self.dict['S'] = ["Drzewo","Swierk"]
        self.dict['u'] = ["Grzyb","Uszak"]
        self.dict['s'] = ["Grzyb","Muchomor Sromotnikowy"]
        self.dict['p'] = ["Grzyb","Pieprznik"]
        self.dict['h'] = ["Grzyb","Muchomor Czerwony"]
        self.dict['m'] = ["Grzyb","Maślak"]
        self.dict['l'] = ["Grzyb","Lysiczka"]
        self.dict['c'] = ["Grzyb","Czubajka"]
        self.dict['.'] = ["Teren","Trawa"]
        self.dict['+'] = ["Teren","Mech"]

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

    def drawTrees(self,mapa):
        Ydam = 0
        for line in mapa:
            Xdam = 0
            for symbol in line:
                if symbol in ['B','D','S']:
                    self.surface.blit(self.korona[symbol], (Xdam-24,Ydam-24))
                Xdam += 24
            Ydam += 24

    def printPosition(self,event,mapa,cursor):
        try:
            X = event.pos[0]
            Y = event.pos[1]
            position = (X,Y)
        except:
            X = cursor[0]
            Y = cursor[1]
            position = cursor

        key = mapa[int(Y/24)][int(X/24)]
        info = self.dict[key]
        print(info)
        return position

    def rysujPostac(self,koords):
        X = koords[0] * 24
        Y = koords[1] * 24
        self.surface.blit(self.grzybman,(X,Y))
		
    def idz_dalej(self, krok, sciezka):
        self.rysujPostac(self, krok)
        self.cost=change_cost(self.cost, krok)
        return sciezka
        
        
    def pobierz_sciezke(sciezka):
        if len(sciezka)>0:
            self.krok=sciezka[0]
            sciezka.pop(0)	
            idz_dalej(self, krok, sciezka)			
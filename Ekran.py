import pygame
from pygame.locals import *
import sys
import random
from getmap import *
from generator import Map


class Ekran(object):
    # funkcja inicjujaca
    def __init__(self, Xres, Yres, res):
        pygame.init()
        flag = DOUBLEBUF
        # bufor grafiki
        self.surface = pygame.display.set_mode((Xres,Yres), flag)
        self.RES = res
        self.POS = res - 1
        # zmienna stanu programu (1 -run, 0 - exit)
        self.state = 1
        self.pause = False
        self.loadGraphic()
        # utworzenie mapy
        self.mapa = self.loadmap("map")
        self.mapa[0][0]='.'
        self.postacPosition = (self.POS,self.POS)
#        self.sciezka = [(19,19),(18,19),(18,18),(17,18),(17,17),(16,17),(16,16),(15,16),(15,15)]
        self.loadDict()
        self.cursor = (0,0)
        self.koszyk = []
        self.grzybyUczenie = {}
        self.cost=cost_table(self.mapa, self.grzybyUczenie)
        self.graph=make_graph(self.cost)
#        print(self.graph)
        self.sciezka = shortestPath(self.graph, (self.POS,self.POS), (0,0))
#        plik=open("koszt.txt", "w")
#        for line in self.cost:
#            for elem in line:
#                plik.write(str(elem))
#                plik.write(' ')
#            plik.write('\n')
#        plik.close()	
        self.mainloop()

    # funkcja wyjscia z programu
    def progExit(self):
        sys.exit()

    # petla glowna
    def mainloop(self):
        while self.state == 1:
            for event in pygame.event.get():
                if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                    self.state=0

            self.cursor = self.printPosition(event,self.mapa,self.mapStat,self.cursor)
            self.surface.fill((0,0,0))      #czyszczenie mapy
            self.drawMap(self.mapa)
            self.rysujPostac(self.postacPosition)
            self.naGrzybie(self.mapa,self.sciezka)
            self.drawTrees(self.mapa)      #rysowanie drzew
            pygame.display.flip()
            pygame.time.wait(100)
        self.progExit()

    # wczytywanie grafik
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

    # wczytywanie slownika (dla funkcji debugujacej)
    def loadDict(self):
        self.dict = {}
        self.dict['B'] = "[Teren Trawa" # "[Drzewo Brzoza"
        self.dict['D'] = "[Teren Trawa" # "[Drzewo Dab"
        self.dict['S'] = "[Teren Trawa" # "[Drzewo Swierk"
        self.dict['u'] = "[Grzyb Uszak"
        self.dict['s'] = "[Grzyb Muchomor Sromotnikowy"
        self.dict['p'] = "[Grzyb Pieprznik"
        self.dict['h'] = "[Grzyb Muchomor Czerwony"
        self.dict['m'] = "[Grzyb Maślak"
        self.dict['l'] = "[Grzyb Lysiczka"
        self.dict['c'] = "[Grzyb Czubajka"
        self.dict['.'] = "[Teren Trawa"
        self.dict['+'] = "[Teren Mech"

    # wczytanie mapy z generatora - utworzenie tablicy
    def loadmap(self,mapa):
        mapa = open(mapa, 'r')
        tab1 = []
        for line in mapa:
            tab2 = []
            for i in range(len(line[:-1])):
                tab2.append(line[i])
            tab1.append(tab2)
        self.mapStat = self.createParams(tab1)
        return tab1

    # tworzenie nowego swiata
    def createWorld(self):
        print('Create new world')
        mapa = Map(self.RES, self.RES)
        mapa.generate()
        mapa.print_to_file('map')
        self.mapa = self.loadmap("map")
        self.mapa[0][0]='.'

    # utworzenie grafu
    def createPath(self,start,end):
        print('Create paths')
        self.cost = cost_table(self.mapa, self.grzybyUczenie)
        self.graph = make_graph(self.cost)
        self.sciezka = shortestPath(self.graph, start, end)

    # rysowanie mapy
    def drawMap(self,mapa):
        print('Draw map')
        Ydam = 0
        for line in mapa:
            Xdam = 0
            for symbol in line:
                self.surface.blit(self.tiles[symbol], (Ydam,Xdam))
                Xdam += 24
            Ydam += 24

    # rysowanie koron drzew
    def drawTrees(self,mapa):
        print('Draw trees')
        Ydam = 0
        for line in mapa:
            Xdam = 0
            for symbol in line:
                if symbol in ['B','D','S']:
                    self.surface.blit(self.korona[symbol], (Xdam-24,Ydam-24))
                Xdam += 24
            Ydam += 24

    # wyswietlanie info dotyczace pozycji na mapie (wskazywane przez kursor)
    def printPosition(self,event,mapa,stats,cursor):
        try:
            X = event.pos[0]
            Y = event.pos[1]
            position = (X,Y)
        except:
            X = cursor[0]
            Y = cursor[1]
            position = cursor

        X = int(X/24)
        Y = int(Y/24)
        key = mapa[Y][X]
        info = 'INFO KURSOR: '
        info += self.dict[key]
        if key in ['u', 's', 'p', 'h', 'm', 'l', 'c']:
            stat = ' poison: '
            stat += stats[Y][X]['poison']
            stat += ' shape: '
            stat += stats[Y][X]['shape']
            stat += ' color: '
            stat += stats[Y][X]['color']
            stat += ' stipe: '
            stat += stats[Y][X]['stipe']
            stat += ' taste: '
            stat += str(stats[Y][X]['taste'])
            stat += ']'
        else:
            stat = ']'
        print(str(X) + ' ' + str(Y) + ' ' + info + stat)
        return position

    # rysowanie grzybiarza na mapie
    def rysujPostac(self,koords):
        print('Draw mush-men')
        Y = koords[0] * 24
#        print(Y)
        X = koords[1] * 24
        self.surface.blit(self.grzybman,(X,Y))

    # wytworzenie statystyk kazdego grzyba na mapie
    def createParams(self,mapa):
        print('Create mushroom parameters')
        tab1 = []
        for line in mapa:
            tab2 = []
            for symbol in line:
                if symbol == 'u':
                    rand = random.randint(35,45)
                    dict = {'key': symbol, 'poison': 'n', 'shape': 'cap', 'color': 'red', 'stipe': 'plain',  'taste': rand}
                elif symbol == 's':
                    dict = {'key': symbol, 'poison': 'y', 'shape': 'cap', 'color': 'yellow', 'stipe': 'plain',  'taste': 0}
                elif symbol == 'p':
                    rand = random.randint(5,15)
                    dict = {'key': symbol, 'poison': 'n', 'shape': 'cone', 'color': 'yellow', 'stipe': 'rugged',  'taste': rand}
                elif symbol == 'h':
                    rand = random.randint(10,20)
                    dict = {'key': symbol, 'poison': 'y', 'shape': 'cap', 'color': 'red', 'stipe': 'dotted',  'taste': rand}
                elif symbol == 'm':
                    rand = random.randint(0,10)
                    dict = {'key': symbol, 'poison': 'n', 'shape': 'cap', 'color': 'brown', 'stipe': 'plain',  'taste': rand}
                elif symbol == 'l':
                    rand = random.randint(45,55)
                    dict = {'key': symbol, 'poison': 'n', 'shape': 'cone', 'color': 'brown', 'stipe': 'plain',  'taste': rand}
                elif symbol == 'c':
                    rand = random.randint(15,25)
                    dict = {'key': symbol, 'poison': 'n', 'shape': 'cap', 'color': 'white', 'stipe': 'dotted',  'taste': rand}
                else:
                    dict = {'key': symbol}
                tab2.append(dict)
            tab1.append(tab2)
        return tab1

    # funkcja sprawdza czy grzybiarz stoi na polu z grzybem
    def naGrzybie(self,mapa,sciezka):
        postX = self.postacPosition[0]
        postY = self.postacPosition[1]
        current = mapa[postY][postX]
        if current in ['u', 's', 'p', 'h', 'm', 'l', 'c']:
            print('NA GRZYBIE STOJE')
            self.zbierzGrzyb(self.mapa)
        else:
            print("NIE MA GRZYBA")
        print(sciezka)
        self.postacPosition = self.ideDo(sciezka)

    # funkcja zmieniajaca nastepna pozycje grzybiarza
    def ideDo(self,sciezka):
        startPos = sciezka[0]
        endPos = sciezka[len(sciezka)-1]
        nastepny = False
        for krok in sciezka:
            if endPos == self.postacPosition:
                if endPos == (0,0):
                    self.createPath((0, 0), (self.POS, 0))
                elif endPos == (self.POS,0):
                    self.createPath((self.POS, 0), (0, self.POS))
                elif endPos == (0,self.POS):
                    self.createPath((0, self.POS), (self.POS, self.POS))
                elif endPos == (self.POS,self.POS):
                    self.uczenieMaszynowe(self.koszyk)
                    print('oproznianie koszyka')
                    self.koszyk = []
                    self.createWorld()
                    self.createPath((self.POS,self.POS),(0,0))
                return endPos
            if krok == self.postacPosition:
                nastepny = True
                continue
            if nastepny:
                print('ide do')
                print(krok)
                return krok

    # funkcja zbierajaca grzyb z danej pozycji gracza i dodanie go do koszyka
    def zbierzGrzyb(self,mapa):
        print('I take the mushroom')
        postX = self.postacPosition[0]
        postY = self.postacPosition[1]
        mapa[postY][postX] = '.'
        grzyb = self.mapStat[postY][postX]
        self.koszyk.append(grzyb)

    def uczenieMaszynowe(self,koszyk):
        print('Uczenie')
        wynik = 0
        ileGrzybow = len(koszyk)
        amountMush = {}
        for i in range(ileGrzybow):
            print(koszyk[i])
            key = koszyk[i]['key']
            smak = koszyk[i]['taste']
            if koszyk[i]['poison'] == 'y':
                smak = smak - 15
            if key not in amountMush:
                amountMush[key] = {}
                amountMush[key]['ile'] = 1
                amountMush[key]['smak'] = smak
            else:
                amountMush[key]['ile'] += 1
                amountMush[key]['smak'] += smak
            wynik += smak

        print('summary: ' + str(wynik))
        for elem in amountMush:
            amountMush[elem]['mnoznik'] = amountMush[elem]['smak'] / wynik
            amountMush[elem]['dla1'] = amountMush[elem]['mnoznik'] / amountMush[elem]['ile']
            print(elem)
            print(amountMush[elem])
            tmpWaga = amountMush[elem]['dla1']

            if elem not in self.grzybyUczenie:
                self.grzybyUczenie[elem] = tmpWaga
            else:
                oldWaga = self.grzybyUczenie[elem]
                suma = oldWaga + tmpWaga
                self.grzybyUczenie[elem] = suma / 2

        for elem in self.grzybyUczenie:
            print(self.dict[elem] + ' waga: ' + str(self.grzybyUczenie[elem]) + ']')
import numpy as np
import pickle, itertools
from generator import Map


mapa = pickle.load(open('map_neural.p', 'rb'))
print "Nasza mapa:"
mapa.print_map()


# funkcja aktywacji (funkcja sigmoidalna)
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))

    
# pod uwage bierzemy np.: drugi rzad w mapie
X = np.array([  [0,0,1,1,1,0,1,0],
                [0,1,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0],
                [0,0,1,0,1,0,0,1] ])
    
# przewidywana punktacja za grzyby zebrane w danych rzedzie         
y = np.array([[50,0,10,50]]).T


np.random.seed(1)


# synapsa inicjalizowana wagami o losowych wartosciach
synapse = 2*np.random.random((8,1)) - 1
print "Synapse:\n %s" % synapse


for iter in xrange(10000):

    # nasze warstwy
    l0 = X
    #print "l0:\n %s" % l0
    l1 = nonlin(np.dot(l0,synapse))
    #print "l1:\n %s" % l1

    # jaki byl blad?
    error = y - l1
    # print "Error:\n %s" % error

    # "Error Weighted Derivative"
    l1_delta = error * nonlin(l1, True)

    # aktualizacja wag sieci o nowe dane
    synapse += np.dot(l0.T,l1_delta)


print "Wyniki po nauce sieci:"
print l1



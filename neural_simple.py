import numpy as np


# funkcja aktywacji (funkcja sigmoidalna)
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))

    
# wejscie
X = np.array([  [0,0,1],
                [0,1,1],
                [1,0,1],
                [1,1,1] ])
    
# wyjscie         
y = np.array([[0,0,1,1]]).T


np.random.seed(1)


# synapsa inicjalizowana wagami o losowych wartosciach
synapse = 2*np.random.random((3,1)) - 1
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



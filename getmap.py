#read file to my_list
l = []
with open('C:\\Users\\Pikachu\\Documents\\GitHub\\SI_Grzybiarz\\map', 'r') as infile:
    data = infile.read()

my_list = data.splitlines()

#create mylista - list of list (chars)
mylista = []

for line in my_list:
    mylista.append(line.split())
tmplist = []
for line in mylista:
    if len(line) != 0:
        tmplist.append(line)
mylista = tmplist
#print(mylista)

# change chars to cost of visit
for i in range(len(mylista)):
    for x in ['S', 'B', 'D']:
        mylista[i] = [j.replace(x,'10000') for j in mylista[i]]
    for x in ['m', 'p', 'h', 'c', 'l', 's', 'u']:
        mylista[i] = [j.replace(x,'1') for j in mylista[i]]
    mylista[i] = [j.replace('.','100') for j in mylista[i]]
    mylista[i] = [j.replace('+','10') for j in mylista[i]]


# change values to int    
for i in range(len(mylista)):
    for j in range(len(mylista)):
        mylista[i][j]= eval(mylista[i][j])

#print(mylista)
'''
# create neighbour list
neighbor = []

for y in range(len(mylista)):
    n0 = []
    for x in range(len(mylista[i])):
        n = []
        numberss = range(0, len(mylista))
        if (x-1) in numberss and (y-1) in numberss: n.append((x-1, y-1))
        if (x-1) in numberss and y in numberss: n.append((x-1, y))
        if (x-1) in numberss and (y+1) in numberss: n.append((x-1, y+1))

        if x in numberss and (y-1) in numberss: n.append((x, y-1))
        if x in numberss and (y+1) in numberss: n.append((x, y+1))

        if (x+1) in numberss and (y-1) in numberss: n.append((x+1, y-1))
        if (x+1) in numberss and y in numberss: n.append((x+1, y))
        if (x+1) in numberss and (y+1) in numberss: n.append((x+1, y+1))

        n0.append(n)
    neighbor.append(n0)

#print(neighbor)


neigh_list = []
for y in range(len(mylista)):
    n1 = []
    for x in range(len(mylista[i])):
        n=[]
        numberss = range(0, len(mylista))
        if (x-1) in numberss and (y-1) in numberss: n.append((x-1, y-1, mylista[x-1][y-1]))
        if (x-1) in numberss and y in numberss: n.append((x-1, y ,mylista[x-1][y]))
        if (x-1) in numberss and (y+1) in numberss: n.append((x-1, y+1, mylista[x-1][y+1]))

        if x in numberss and (y-1) in numberss: n.append((x, y-1, mylista[x][y-1]))
        if x in numberss and (y+1) in numberss: n.append((x, y+1, mylista[x][y+1]))

        if (x+1) in numberss and (y-1) in numberss: n.append((x+1, y-1, mylista[x+1][y-1]))
        if (x+1) in numberss and y in numberss: n.append((x+1, y, mylista[x+1][y]))
        if (x+1) in numberss and (y+1) in numberss: n.append((x+1, y+1, mylista[x+1][y+1]))

        n1.append(n)
    neigh_list.append(n1)

#print(neigh_list)

#create node list
nodes = []
for y in range(len(mylista)):
    for y in range(len(mylista)): nodes.append((x, y))

#print nodes



way = []
cost = 0
print(neigh_list[0][0])
print(min(neigh_list[0][0], key = lambda t: t[2]))

for y in range(len(mylista)):
    for x in range(len(mylista[i])):
        way.append((x+1,y))
        
  '''      

def node_name(row_index, col_index):
    return (row_index, col_index)

def make_graph(matrix):
    graph = {}
    width, height = len(matrix[0]), len(matrix)
    columns = range(width)
    for rowindex in range(height):
        for colindex in columns:
            graph[node_name(rowindex, colindex)] = x = {}
            # Up
            if rowindex > 0:
                x[node_name(rowindex - 1, colindex)] = matrix[rowindex - 1][colindex]
            # Down
            if rowindex < height - 1:
                x[node_name(rowindex + 1, colindex)] = matrix[rowindex + 1][colindex]
            # Left
            if colindex > 0:
                x[node_name(rowindex, colindex - 1)] = matrix[rowindex][colindex - 1]
            # Right
            if colindex < width - 1:
                x[node_name(rowindex, colindex + 1)] = matrix[rowindex][colindex + 1]

    return graph
graph=make_graph(mylista)

from priodict import priorityDictionary
#start=(startx, starty)
#end=(endx, endy)
def Dijkstra(G,start,end=None):
	D = {}	# dictionary of final distances
	P = {}	# dictionary of predecessors
	Q = priorityDictionary()   # est.dist. of non-final vert.
	Q[start] = 0

	for v in Q:
		D[v] = Q[v]
		if v == end: break
		for w in G[v]:
			vwLength = D[v] + G[v][w]
			if w in D:
				if vwLength < D[w]:
					raise ValueError
			elif w not in Q or vwLength < Q[w]:
				Q[w] = vwLength
				P[w] = v
	
	return D,P
			
def shortestPath(G,start,end):
	D,P = Dijkstra(G,start,end)
	Path = []
	while 1:
		Path.append(end)
		if end == start: break
		end = P[end]
	Path.reverse()
	return Path

print(shortestPath(graph, (0,0), (29,29)))
#print(Dijkstra(graph,(0,0),(29,29)))

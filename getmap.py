def cost_table(lista):
    costs=[]
    for line in range(len(lista)):
        wiersze=[]
        for symbol in range(len(lista)):
            if lista[line][symbol] in ['S', 'B', 'D']: 
                wiersze.append(10000)
            if lista[line][symbol] in ['m', 'p', 'h', 'c', 'l', 's', 'u']: 
                wiersze.append(1)
            if lista[line][symbol]=='+': 
                wiersze.append(10)
            if lista[line][symbol]=='.': 
                wiersze.append(50)
        costs.append(wiersze)
    return costs

def node_name(row_index, col_index):
    return (row_index, col_index)

def make_graph(matrix):
    graph = {}
    width, height = len(matrix[0]), len(matrix)
    columns = range(width)
    for rowindex in range(height):
        for colindex in columns:
        #    if(matrix[rowindex][colindex]<1000):
            graph[node_name(rowindex, colindex)] = x = {}
                # Up
            if (rowindex > 0): # and (matrix[rowindex - 1][colindex] <1000)
                x[node_name(rowindex - 1, colindex)] = matrix[rowindex - 1][colindex]
				# Down
            if (rowindex < height - 1): # and (matrix[rowindex + 1][colindex]<1000)
                x[node_name(rowindex + 1, colindex)] = matrix[rowindex + 1][colindex]
				# Left
            if (colindex > 0): # and (matrix[rowindex][colindex - 1]<1000)
                x[node_name(rowindex, colindex - 1)] = matrix[rowindex][colindex - 1]
			# Right
            if (colindex < width - 1): # and (matrix[rowindex][colindex + 1]<1000)
                x[node_name(rowindex, colindex + 1)] = matrix[rowindex][colindex + 1]

    return graph
#graph=make_graph(mylista)
#print(graph)

from priodict import priorityDictionary
#start=(startx, starty)
#end=(endx, endy)
def Dijkstra(G,start,end=None):
	D = {}	# dictionary of final distances
	P = {}	# dictionary of predecessors
	Q = priorityDictionary()   # est.dist. of non-final vert.
	Q[start] = 0

	vwLength=0
	for v in Q:
		D[v] = Q[v]
		if v == end: break
		for w in G[v]:
			vwLength = D[v] + G[v][w]
			if w in D:
				if vwLength < D[w]:
					print("wielgachny wynik")
					raise ValueError
			elif w not in Q or vwLength < Q[w]:
				Q[w] = vwLength
				P[w] = v
#	print('Dijkstra:')
#	print(D)
	return D,P

'''wywolanie ponizszej funkcji da nam sciezke'''	
def shortestPath(G,start,end):
    #G1=make_graph(G)
	D,P = Dijkstra(G,start,end)
	Path = []
	while 1:
		Path.append(end)
		if end == start: break
		end = P[end]
	Path.reverse()
	return Path

#print(shortestPath(make_graph(graph), (19,19), (0,0)))

def change_cost(table, step):
    table[step[0]][step[1]]=200
    return table

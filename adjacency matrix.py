# adjacency matrix

nv = 5 # no.of vertices
edges = [(0,1),(0,2),(1,2),(3,2),(4,1),(2,4)]

adj_matrix = []

for i in range(nv):
    row = [0] * nv
    adj_matrix.append(row)

for v1,v2 in edges:
    adj_matrix[v1][v2] = 1  # If vertices are start with 1 not from 0 then do v1-1 & v2-1 
    adj_matrix[v2][v1] = 1  # Undirected graph

for i in range(nv):   
    print(adj_matrix[i])

# Undirected graph & weighted graph

nv = 5 # no.of vertices
edges = [(0,1,3),(0,2,5),(1,2,10),(3,2,6),(4,1,7),(2,4,9)]

adj_matrix = []

for i in range(nv):
    row = [0] * nv
    adj_matrix.append(row)

for v1,v2,w in edges:
    adj_matrix[v1][v2] = w  
    adj_matrix[v2][v1] = w  # Undirected graph & weighted graph

for i in range(nv):
    print(adj_matrix[i])

#Direction graph

nv = 5 # no.of vertices
edges = [(0,1),(0,2),(1,2),(3,2),(4,1),(2,4)]

adj_matrix = []

for i in range(nv):
    row = [0] * nv
    adj_matrix.append(row)

for v1,v2 in edges:
    adj_matrix[v1][v2] = 1  

for i in range(nv):
    print(adj_matrix[i])


# directed graph & weighted graph

nv = 5 # no.of vertices
edges = [(0,1,3),(0,2,5),(1,2,10),(3,2,6),(4,1,7),(2,4,9)]

adj_matrix = []

for i in range(nv):
    row = [0] * nv
    adj_matrix.append(row)

for v1,v2,w in edges:
    adj_matrix[v1][v2] = w  

for i in range(nv):
    print(adj_matrix[i])


# vertices are not integers. They are alphabets 

vertices = ['A', 'B', 'C', 'D', 'E']
edges = [('A','B'), ('A','C'), ('B','C'), ('D','C'), ('E','B'), ('C','E')]
mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}

adj_matrix = []

# create empty adjacency matrix
for i in range(nv):
    row = [0] * nv
    adj_matrix.append(row)

# fill edges
for v1, v2 in edges:
    adj_matrix[mapping[v1]][mapping[v2]] = 1

# print matrix
for row in adj_matrix:
    print(row)
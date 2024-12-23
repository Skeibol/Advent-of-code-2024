from time import perf_counter

class Graph():
    def __init__(self):
        self.connections = None
        self.connectionCounter = None
        
    def getBiggestCluster(self):
        maxlen = -1
        largest = None
        for n in self.connections:
            cluster = travelGraph(n,self,self.connectionCounter,maxlen)
           
            if len(cluster) > maxlen:
                maxlen= len(cluster)
                largest = cluster
        
        return largest


def checkIsConnected(graph, startingNode, targetNodes):
    for target in targetNodes:
        if startingNode not in graph.connections[target]:
            return False
    return True

def travelGraph(startNode,graph,connectionCounter,maxcon,visited = None,connections = None):
    if visited is None:
        connections = [startNode]
        visited = []
    
       
    if connectionCounter[startNode] <= maxcon:
        return []
    
    if len(visited) > 1:
        if checkIsConnected(graph,startNode,connections):
            connections.append(startNode)
        else:
            return []
    
    visited.append(startNode)

    for nextNode in graph.connections[startNode]:
        if nextNode in visited:
            continue
        
        travelGraph(nextNode,graph,connectionCounter,maxcon,visited,connections)
    
    return connections

start = perf_counter()
with open("./advent-of-code/day23/input.txt", "r") as file:
    lines = file.read().splitlines()

conns = {}
connectionCounter = {}
graph = Graph()

for line in lines:
    lhs, rhs = line.split("-")
    if lhs not in connectionCounter:
        conns[lhs] = [rhs]
        connectionCounter[lhs] = 1
    else:
        conns[lhs].append(rhs)
        connectionCounter[lhs] += 1
        
        
    if rhs not in connectionCounter:
        conns[rhs] = [lhs]
        connectionCounter[rhs] = 1
    else:
        conns[rhs].append(lhs)
        connectionCounter[rhs] += 1


graph.connections = conns
graph.connectionCounter = connectionCounter
c = graph.getBiggestCluster()

pword = ''.join([i+',' for i in sorted(c)])[:-1]
print(pword)

end = perf_counter() - start
print(f"Time elapsed recurs: {end}")













# PART 1
# rls = []
# cnt = 0
# for i in range(0,len(relations)):
#     a = relations[i][0]
#     b = relations[i][1]
#     for j in range(i+1,len(relations)):
#         if relations[j][0] == b and relations[j][1] != a:
#             if a[0] == 't' or b[0] == 't' or c[0] == 't':
#                 c = relations[j][1]
#                 for k in range(j+1,len(relations)):
#                     if relations[k][0] == c and relations[k][1] == a:
#                         cnt+=1
              
# print(cnt)
#print(len(rls))
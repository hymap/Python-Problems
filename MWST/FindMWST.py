# Python program for Kruskal's algorithm to find
# Minimum Spanning Tree of a given undirected and weighted graph
import DisjointSet
import PriorityQueue

# Class to represent a graph
class Graph:
 
    def __init__(self):
        #self.V = vertices  # No. of vertices
        self.graph = []  
        self.sortedGraph = [] 
        # to store graph
        try:
            while True:
                buffer = input().split()
                row = []
                for c in buffer:
                    row.append(int(c))
                self.graph.append(row)
        except EOFError:
            pass
        #Trying to get vertices count based on 2nd field from each edge. 
        #0 1 1
        #0 2 5
        #1 2 4
        #2 3 3
        #2 4 2
        #3 5 2
        #4 5 2
        #e.g In above example, 2nd field highest number is 5. So vertices is 5+1 including 0. 
        v= max(self.graph, key=lambda item: item[1])
        if (any(0 in sublist for sublist in self.graph)):
            self.V = v[1]+1 # No. of vertices
        else:
            self.V = v[1]
 
    # The main function to construct MST using Kruskal' algorithm
    def KruskalMST(self):
 
        result = []   # This will store the resultant MWST
        #edgesArr = [] #Final edges in MSWT
         
        # An index variable, used for sorted edges
        i = 0
         
        # An index variable, used for result[]
        e = 0

        # Sort all the edges in non-decreasing order of their weight. 
        #self.graph = sorted(self.graph,
        #                    key=lambda item: item[2])
        j = 0
        pd = PriorityQueue.PriorityQueue() 
        while j < len(self.graph):
            u, v, w = self.graph[j]
            pd.insert([u, v, w])
            j = j+1
        self.sortedGraph = pd.sort()

        #print("graph after sort ",self.sortedGraph)
        ds = DisjointSet.DisjointSet(self.V)

        # Number of edges for MST to be taken is equal to V-1
        while e < self.V - 1:

            # Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = self.sortedGraph[i]
            i = i + 1
            x = ds.find(u)
            y = ds.find(v)

            # Avoid x= y as it forms a cycle else valid edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                #edgesArr.append([u,v])
                ds.union(x, y)
            # Else discard the edge
 
        #result = sorted(result, key=lambda item: item[0])
        #print(" edgesarr ", edgesArr)
        minimumCost = 0
        print ("Edges in the MST : ")
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree" , minimumCost)    
        
# Driver code
g = Graph()
#print("graph ",g.graph)
print("Vertices in given graph: ", g.V)

# Method to find MWST(Minimum Weight Spanning Tree)
g.KruskalMST()

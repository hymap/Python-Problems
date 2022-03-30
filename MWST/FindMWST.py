# Python program for Kruskal's algorithm to find
# Minimum Spanning Tree of a given undirected and weighted graph
 
# Class to represent a graph
class Graph:
 
    def __init__(self):
        #self.V = vertices  # No. of vertices
        self.graph = []  
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
        elem_to_find = 0
        v= max(self.graph, key=lambda item: item[1])
        if (any(elem_to_find in sublist for sublist in self.graph)):
            self.V = v[1]+1 # No. of vertices
        else:
            self.V = v[1]
 
    # Find parent of given vertex
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
 
    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        #print("xroot, yroot, x, y, parent[x],parent[y] ",xroot,yroot, x, y, parent[x],parent[y],rank[xroot],rank[yroot])
        
        # If rank is higher then make it as parent
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
 
        # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
 
    # The main function to construct MST using Kruskal' algorithm
    def KruskalMST(self):
 
        result = []   # This will store the resultant MWST
        #edgesArr = [] #Final edges in MSWT
         
        # An index variable, used for sorted edges
        i = 0
         
        # An index variable, used for result[]
        e = 0

        # Sort all the edges in non-decreasing order of their weight. 
        self.graph = sorted(self.graph,
                            key=lambda item: item[2])
 
        #print("graph after sort ",self.graph)
        parent = []
        rank = []
 
        # Create V subsets with single elements
        for node in range(self.V):
            #print("node ",node)
            parent.append(node)
            rank.append(0)

        # Number of edges for MST to be taken is equal to V-1
        while e < self.V - 1:

            # Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = self.graph[i]
            #print("u, v, w, i ",u, v, w, i )
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            #print("x, y ",x, y )

            # Avoid x= y as it forms a cycle else valid edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                #edgesArr.append([u,v])
                self.union(parent, rank, x, y)
                #print("Appending adges into result : parent, rank, union, result ", parent, rank, self.union, result)
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

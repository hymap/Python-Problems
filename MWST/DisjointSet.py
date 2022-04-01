
class DisjointSet:
  def __init__(self, V):
    self.vertices = 0
    self.parent = [] 
    self.rank = []
    for node in range(V):
      self.parent.append(node)
      self.rank.append(0)

  # Find parent of given vertex
  def find(self, i):
    if self.parent[i] == i:
      return i
    return DisjointSet.find(self, self.parent[i])
 
  # A function that does union of two sets of x and y
  # (uses union by rank)
  def union(self, x, y):
    xroot = DisjointSet.find(self, x)
    yroot = DisjointSet.find(self, y)
        
    # If rank is higher then make it as parent
    if self.rank[xroot] < self.rank[yroot]:
      self.parent[xroot] = yroot
    elif self.rank[xroot] > self.rank[yroot]:
      self.parent[yroot] = xroot
 
    # If ranks are same, then make one as root
    # and increment its rank by one
    else:
      self.parent[yroot] = xroot
      self.rank[xroot] += 1

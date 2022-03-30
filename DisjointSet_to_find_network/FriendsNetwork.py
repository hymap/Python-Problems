from sys import stdin, stdout

# Dictionary based Disjoint Forest
class DisjointSet:
  def __init__(self):
    self.parent = {} 
    self.count = {}
    self.rank = {}

  def addInput(self,x):
    if not x in self.parent:
      self.parent[x] = x
      self.rank[x] = 0
      self.count[x] = 1

  def find(self, x):
    # Finds the representative of the set
    #that x is an element of
    if (self.parent[x] != x):  
      # if x is not the parent of itself
      # Then x is not the representative of
      # its set,
      self.parent[x] = self.find(self.parent[x])
             
      # so we recursively call Find on its parent
      # and move i's node directly under the
      # representative of this set
    return self.parent[x]

  def union(self, x, y):
    # Find current sets of x and y
    xset = self.find(x)
    yset = self.find(y)
    #print("After find return : id,rank, count",self.parent, self.rank, self.count, xset, yset )
    
    if xset == yset:
      return self.count[xset]

    if self.rank[xset] < self.rank[yset]:
      self.parent[xset] = yset
      self.count[yset] += self.count[xset]
      sum_count = self.count[yset]
    elif self.rank[xset] > self.rank[yset]:
      self.parent[yset] = xset
      self.count[xset] += self.count[yset]
      sum_count = self.count[xset]
    else:
      self.parent[yset] = xset
      self.rank[xset] += 1
      self.count[xset] += self.count[yset]
      sum_count = self.count[xset]
    #print("before return in union : id,rank, count",self.parent, self.rank, self.count)
    return sum_count

output = [] #Initialize o/p list
#Read number of test cases
num_of_tests = int(stdin.readline().strip())

for t in range(num_of_tests):
  #Read total number of relations
  F = int(stdin.readline().strip())
  
  ds = DisjointSet()

  #Loop through relations 
  for q in range(F):
    #Read each relation 
    u, v = stdin.readline().strip().split()

    ds.addInput(u)
    ds.addInput(v)
    #Find union of given relation
    sum = ds.union(u, v)

    #Store in o/p to flush at a time in the end 
    output.append(sum)

print("Number of friends in each given relation :")
for cnt in output:
    print(cnt)

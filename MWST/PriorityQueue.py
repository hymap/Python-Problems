# A simple implementation of Priority Queue
# in ascending order using Queue.
class PriorityQueue():
    def __init__(self):
        self.pq = []
        self.sortedGraph = []
  
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.pq) == 0
  
    # for inserting an element in the queue
    def insert(self, data):
        self.pq.append(data)
    
    def size(self):
        return len(self.pq)
  
    # For popping/deleting an element based on Priority of weight of an edge
    def getHighPriorityItem(self):
        try:
            #start comparing with 0th element
            max = 0
            for i in range(0, self.size()):
                #Less weight edge will get highest priority
                if self.pq[i][2] < self.pq[max][2]:
                    max = i
            item = self.pq[max]
            del self.pq[max] 
            #PriorityQueue.pop(self)
            return item
        except IndexError:
            print()
            exit()
    
    def sort(self):
        #Loop through all elements in queue until we sort all items in asending order 
        #and form a sorted list
        while not PriorityQueue.isEmpty(self):
            #Save each priority item into another list 
            item = PriorityQueue.getHighPriorityItem(self)
            self.sortedGraph.append(item)
        return self.sortedGraph

    def size(self):
        return len(self.pq)

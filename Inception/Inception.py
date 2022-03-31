import stack

#Below program is to test in whose dream some person 'Dom' is in currently.
#if user provides query 'Sleep X', This means person named X 
#will be sleeping and Dom is going into X’s dream, from the previous person’s dream (if any).
#If user provides query 'Kick', means person is awaken, and he will enter into the previous person’s dream (if any).
#if user provides query 'Test', means we need to print person name in whose dream he is in currently
class Inception():
    def __init__(self):
        self.queries = stack.Stack()
        self.output = []

    # function to add query to stack
    def addDream(self, query):
        self.queries.push(query)

    # Calls this function for 'Kick' input means - person awaken, 
    # So we need to remove that person 
    def removePrevDream(self):
        if not self.queries.empty():
            self.queries.pop()

    #Find inception if query = 'Test'
    def findInception(self):
        #print("top ", self.queries.top())
        if (not self.queries.empty() and self.queries.top().count("Sleep") > 0):
            str = self.queries.top()
            #print("Sleep cnt ", self.queries.top().count("Sleep"))
            str1, str2 = str.split()
            #print("In dream of ", str2)
            self.output.append(str2)
        else:
            str2 = "Not in a dream"
            self.output.append(str2)
    
    #Printing stack object
    def print(self):
        print("Printing stack : ")
        while not self.queries.empty():
            print(self.queries.pop())

#Driver code
testCases = int(input("Enter Number Of Queries : "))
#print("testCases ",testCases)
obj = Inception()
for i in range(testCases):
    query = input()
    if (query.count("Sleep") > 0):
        obj.addDream(query)
    elif (query.count("Kick") > 0):
        obj.removePrevDream()
    elif (query.count("Test") > 0):
        obj.findInception()

#obj.print()

# For each input line print the output
print("Output : ")
for result in obj.output:
    print(result)

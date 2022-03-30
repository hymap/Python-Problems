# Path through maze
import stack
from collections import deque

class Maze:
    def __init__(self):
        self.maze = []
        self.R, self.C = 0,0
        try:
            while True:
                buffer = input()
                row = []
                for c in buffer:
                    if c in '01':
                        row.append(int(c))
                    elif c in 'eE':
                        self.entrance = (len(self.maze), len(row))
                        row.append(2)
                # self.maze += row
                self.maze.append(row)
        except EOFError:
            pass
        #Total rows and columns in given maze
        self.R, self.C = len(self.maze), len(self.maze[0]) 
        self.directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.final_path = []
    
    def printMaze(self):   
        for r in range(self.R):
            for c in range(self.C):
                print("{:<5}".format(self.maze[r][c]), end='')
            print()

    def printFinalPath(self):
        print("Solution as ordered pairs final_path : ",self.final_path)        

    def traverseStartToEnd(self):
        #A double-ended queue, or deque, has the feature of adding and removing elements from either end
        queue = deque()  

        #Append starting point to queue and 3rd field at first making it to value i.e 2
        #to mark path by incrementing 1
        queue.appendleft((self.entrance[0], self.entrance[1], self.maze[self.entrance[0]][self.entrance[1]])) 
        traverse_path = []

        while len(queue) != 0:
            #print("before pop queue :",queue)
            coord = queue.pop()
            traverse_path.append((coord[0],coord[1]))

            #Return steps to exit if it is 0 and its a border 
            if ((self.maze[coord[0]][coord[1]] == 0) and (coord[0] == 0 or coord[0] == self.R-1 or coord[1] == 0 or coord[1] == self.C-1)):
                self.maze[coord[0]][coord[1]] = coord[2] 
                #self.retractExitToEntrance(coord)
                #self.printMaze()
                #print("Exit point : ",(coord[0],coord[1]))
                self.exit = (coord[0],coord[1])
                return coord[2] ## Steps count

            #Mark them to some other symbol after vising other than entry point. 
            if not (self.maze[coord[0]][coord[1]]  == 2):
                self.maze[coord[0]][coord[1]] = coord[2] 

            #Move to all directions from current point and see 
            for dir in self.directions:
                nr, nc = coord[0]+dir[0], coord[1]+dir[1]

                #Continue if there is no way to move further or if its 1 or if its already visited
                if (nr < 0 or nr >= self.R or nc < 0 or nc >= self.C or self.maze[nr][nc] == 1 or self.maze[nr][nc] > 1):  
                    continue

                #Valid move 
                queue.appendleft((nr, nc, coord[2]+1))

    def retractExitToEntrance(self):
        reverse_path = stack.Stack()
        #final_path = []

        #Push Exit Node into Stack
        #reverse_path.push((end_coord[0],end_coord[1])) 
        reverse_path.push(self.exit)
        curr_node = self.exit

        while True:
            cur_val = self.maze[curr_node[0]][curr_node[1]]
            #Move to all directions from current point and see 
            for dir in self.directions:
                nr, nc = curr_node[0]+dir[0], curr_node[1]+dir[1]

                #Continue if there is no way to move further or if its 1
                if (nr < 0 or nr >= self.R or nc < 0 or nc >= self.C or self.maze[nr][nc] == 1):  
                    continue

                #node is valid and push to stack
                valid_node_val = self.maze[nr][nc]
                if cur_val == valid_node_val+1 :
                    curr_node = (nr,nc)
                    reverse_path.push((nr,nc))
                    break
                        
            #reached entrance, stop here
            if self.entrance == curr_node:
                break

        #Contruct reverpath to final path from entry to exit
        while not reverse_path.empty():
            self.final_path.append(reverse_path.pop())
        #return final_path

m = Maze()
#print(m.maze)
print("Entrance point : ",m.entrance)
steps = m.traverseStartToEnd()
if steps:
    m.retractExitToEntrance()
    m.printMaze()
    print("Exit point : ", m.exit)
    m.printFinalPath()
    print("The shortest path from source to destination has length", steps-2)
else:
    print("Exit Not Found")

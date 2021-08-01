from collections import deque 
from pprint import pprint

class PristonBuilding :
    def __init__(self,m,n,k) :
        self.m = m
        self.n = n
        self.k = k
        self.q = deque()
        self.matrix = [[0]*m for _ in range(n)]
    
    def new_building(self,x,y,time) :
        self.q.append((x,y,time))
        
    def is_valid(self,pos) :
        return pos[0] < self.n and pos[1] < self.m and pos[0] >= 0 and pos[1] >= 0

    def start_simulation(self) :
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        time = 1
        while self.q :
            current_node = self.q.popleft()
    
            self.matrix[current_node[0]][current_node[1]] = 1
            for direction in directions :
                adj_node = (direction[0] + current_node[0],direction[1] + current_node[1])
                if not self.is_valid(adj_node) : continue
                if self.matrix[adj_node[0]][adj_node[1]] == 1 : continue
                
                time = current_node[2] + 1
                
                self.matrix[adj_node[0]][adj_node[1]] = 1  #Burnt
                
                self.new_building(adj_node[0],adj_node[1],time)
                
#                 pprint(self.matrix)
#                 print(time)
#                 print("\n")
#                 print(adj_node)
        
        return time
                


# In[96]:


# m = 10
# n = 10
# k = 4
# pb = PristonBuilding(m,n,k)

# #5 3 4 7 7 5 8 5
# pb.new_building(5-1,3-1,1)
# pb.new_building(4-1,7-1,1)
# pb.new_building(7-1,5-1,1)
# pb.new_building(8-1,5-1,1)

# # pb.new_building(0,0,1)

# print(pb.start_simulation())

# print(pb.matrix)


def cin() :
    string = input().strip()
    while string == "" :
        string = input().strip()
    return string

def run() :
    n,m = cin().split()
    k = int(cin())
    pb = PristonBuilding(int(m),int(n),k)
    
    cells = cin().split()

    i = 0
    while i < 2*k :
        pb.new_building(int(cells[i]) - 1,int(cells[i+1]) - 1,1)
        i += 2
    
    print(pb.start_simulation())
        

run()
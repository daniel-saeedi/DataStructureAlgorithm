#!/usr/bin/env python
# coding: utf-8

# In[122]:


class Vertex(object):
    def __init__(self, key):
        self.key = key
        self.neighbors = {}
        self.parent = None
        self.changes = 0

    def add_neighbor(self, neighbor, weight=0):
        self.neighbors[neighbor] = weight

    def __str__(self):
        return '{} neighbors: {}'.format(
            self.key,
            [x.key for x in self.neighbors]
        )

    def get_connections(self):
        return self.neighbors.keys()

    def get_weight(self, neighbor):
        return self.neighbors[neighbor]

class Graph:
    def __init__(self,n):
        self.verticies = {}
        self.n = n

    def add_vertex(self, vertex):
        self.verticies[vertex.key] = vertex

    def get_vertex(self, key):
        try:
            return self.verticies[key]
        except KeyError:
            return None

    def __contains__(self, key):
        return key in self.verticies

    def add_edge(self, from_key, to_key, weight=0):
        if from_key not in self.verticies:
            self.add_vertex(Vertex(from_key))
        if to_key not in self.verticies:
            self.add_vertex(Vertex(to_key))
        self.verticies[from_key].add_neighbor(self.verticies[to_key], weight)
        self.verticies[to_key].add_neighbor(self.verticies[from_key], weight)

    def get_vertices(self):
        return self.verticies.keys()

    def __iter__(self):
        return iter(self.verticies.values())
    
    def BFS(self,initValues,goalValues) :
        visited = [False] * self.n
        queue = [1]
        
        result = []

        while queue :
            current_node = queue.pop(0)

            if visited[current_node-1] : 
                continue
            visited[current_node-1] = True
            
            if self.verticies[current_node].parent != None:
                if self.verticies[current_node].parent.parent != None :
                    self.verticies[current_node].changes += self.verticies[current_node].parent.parent.changes;
            
            if initValues[current_node-1] != goalValues[current_node-1] :
                if self.verticies[current_node].changes % 2 == 0 :
                    result.append(self.verticies[current_node].key)
                    self.verticies[current_node].changes += 1
            else :
                if self.verticies[current_node].changes % 2 != 0 :
                    result.append(self.verticies[current_node].key)
                    self.verticies[current_node].changes += 1
                
                    
            for child in self.verticies[current_node].neighbors :
                if visited[child.key-1] : continue
                queue.append(child.key)
                child.parent = self.verticies[current_node]
        
        return result
    


# In[123]:


# g = Graph()
# for i in range(1,11):
#     g.add_vertex(Vertex(i))

# # g.verticies
# g.add_edge(2,1)
# g.add_edge(3,1)
# g.add_edge(4,2)
# g.add_edge(5,1)
# g.add_edge(6,2)
# g.add_edge(7,5)
# g.add_edge(8,6)
# g.add_edge(9,8)
# g.add_edge(10,5)

# print(g.BFS())


# In[127]:


def cin():
    string = input().strip()
    while string == "" :
        string = input().strip()
    return list(map(int, string.split()))

def run() :
    n = int(cin())
    g = Graph(n)
    for i in range(1,n+1):
        g.add_vertex(Vertex(i))
    for _ in range(n-1):
        u,v = cin().split()
        g.add_edge(u,v)
    
    initValues = cin()
    goalValues = cin()
    
    result = g.BFS(initValues,goalValues)
    
    print(len(results))
    for result in results:
        print(result)


# In[128]:


run()


# In[ ]:





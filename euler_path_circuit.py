# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 20:41:16 2020

@author: gogoh
"""
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
class Graph:
    def __init__(self,vertices):
        self.v = vertices
        self.graph = defaultdict(list)
    def addEddg(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def DFSUtil(self,v,visited):
        visited[v]= True
        
        for i in self.graph[v]:
            if visited[i]== False:
                self.DFSUtil(i,visited)

    def isConnected(self):
        visited = [False]*(self.v)

        for i in range(self.v):
            if len(self.graph[i])>1:
                break
        if i == self.v-1:
            return True
        self.DFSUtil(i,visited)

        for i in range(self.v):
            if visited[i]==False and len(self.graph[i])>0:
                return True
    def isEulerian(self):
        if self.isConnected() == False:
            return 0
        else:
            odd = 0
            for i in range(self.v):
                if len(self.graph[i])%2 !=0:
                    odd+=1

            if odd == 0:
                return 2
            elif odd == 2:
                return 1
            elif odd >2:
                return 0

    def test(self):
        res = self.isEulerian()
        if res == 0: 
             print ("graph is not Eulerian")
        elif res ==1 : 
            print ("graph has a Euler path")
        else:
            print ("graph has a Euler cycle")




nnodes=int(input("please enter the number of edges"))
G=nx.Graph()
g1 = Graph(nnodes)
for i in range(nnodes):
    u=int(input("input the first node and press enter"))
    v=int(input("input the second node and press enter"))
    g1.addEddg(u,v)
    G.add_node(u)
    G.add_node(v)
    G.add_edge(u,v)
nx.draw(G)
g1.test()
#GUI= nx.Graph()
#GUI.add_node(u)
#GUI.add_node(v)
#GUI.add_edge(u,v)
#g1.test()
#plt.draw(GUI)
#plt.savefig("simple_path.png")
#plt.show()

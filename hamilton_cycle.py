# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 22:16:13 2020

@author: gogoh
"""
import networkx as nx

def hamilton(G):
    F = [(G,[list(G.nodes())[0]])]
    n = G.number_of_nodes()
    while F:
        graph,path = F.pop()
        confs = []
        for node in graph.neighbors(path[-1]):
            conf_p = path[:]
            conf_p.append(node)
            conf_g = nx.Graph(graph)
            conf_g.remove_node(path[-1])
            confs.append((conf_g,conf_p))
        for g,p in confs:
            if len(p)==n:
                return p
            else:
                F.append((g,p))
    return None

G = nx.Graph()
edges = [('B', 'C'), ('B', 'E'), ('C', 'D'), ('A', 'D'), ('D', 'J'), ('D', 'E'), ('E', 'F'), ('F', 'J'), ('J', 'A')]
G.add_edges_from(edges)
hamilton(G)
nx.draw(G)

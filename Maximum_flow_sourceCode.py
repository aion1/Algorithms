# Python program for implementation of Ford Fulkerson algorithm
from collections import defaultdict
import random
import string
from tkinter import *
import tkinter as tk
import re
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
# This class represents a directed graph using adjacency matrix representation


def visual_graph(graph):
    G = nx.DiGraph()
    for i in range(0, len(graph)):
        for j in range(0, len(graph[i])):
            if (graph[i][j] != 0):
                G.add_edge(i, j, capacity=graph[i][j])


    pos=nx.random_layout(G)
    nx.draw(G,pos,with_labels=True)
    labels = nx.get_edge_attributes(G, 'capacity')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()
    print(G.edges)
def visual_detailed_graph_first(graph):
    G = nx.DiGraph()
    for i in range(0, len(graph)):
        for j in range(0, len(graph[i])):
            if (graph[i][j] != 0):
                G.add_edge(i, j, capacity=graph[i][j])
                pos = nx.random_layout(G)
                nx.draw(G, pos, with_labels=True)
                labels = nx.get_edge_attributes(G, 'capacity')
                nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
                x=random.choice("abcdefghijklmn")
                plt.savefig("{}.png".format(x))
                plt.show()
def visual_graph_bd(graph):
    G = nx.DiGraph()
    for i in range(0, len(graph)):
        for j in range(0, len(graph[i])):
            if (graph[i][j] != 0):
                G.add_edge(i, j, capacity=graph[i][j])

    pos = nx.random_layout(G)
    nx.draw(G, pos, with_labels=True)
    labels = nx.get_edge_attributes(G, 'capacity')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    x = random.choice("opqrstuvwxyz")
    plt.savefig("{}.png".format(x))
    plt.show()
    print(G.edges)
class Graph:

    def __init__(self, graph):
        self.graph = graph  # residual graph
        self.ROW = len(graph)



    def BFS(self, s, t, parent):

        # Mark all the vertices as not visited
        visited = [False] * (self.ROW)

        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        # Standard BFS Loop
        while queue:

            # Dequeue a vertex from queue and print it
            u = queue.pop(0)

            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

                # If we reached sink in BFS starting from source, then return
        # true, else false
        #visual_graph(self.graph)
        return True if visited[t] else False

    def BFS_Mutated(self, s, t, parent):

        # Mark all the vertices as not visited
        visited = [False] * (self.ROW)

        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        # Standard BFS Loop
        while queue:

            # Dequeue a vertex from queue and print it
            u = queue.pop(0)

            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

                # If we reached sink in BFS starting from source, then return
        # true, else false
        visual_graph_bd(self.graph)
        return True if visited[t] else False

    def FordFulkerson(self, source, sink):

        # This array is filled by BFS and to store path
        parent = [-1] * (self.ROW)

        max_flow = 0  # There is no flow initially

        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent):

            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while (s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Add path flow to overall flow
            max_flow += path_flow

            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while (v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow
    def FordFulkersonMutated(self, source, sink):

        # This array is filled by BFS and to store path
        parent = [-1] * (self.ROW)

        max_flow = 0  # There is no flow initially

        # Augment the flow while there is path from source to sink
        while self.BFS_Mutated(source, sink, parent):

            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while (s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Add path flow to overall flow
            max_flow += path_flow

            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while (v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow
final_graph = []
class UI:
    def __init__(self):
        self.initUI()
    def initUI (self):
    #the main page frame
        self.mainWindow = tk.Tk()
        self.mainWindow.title("Maximum flow algorithm")
        self.mainWindow.geometry("1024x768")
    #first lable of the source node
        self.label_source = tk.Label(text="Please enter the Source Node")
        self.label_source.config(font=25)
        self.label_source.grid(column=0, row=0)
    #first textbox of the source node input
        self.textbox_source = tk.Entry(width=20)
        self.textbox_source.grid(column=1, row=0,padx=10, pady=10)
    #second lable of the sink node
        self.label_sink = tk.Label(text="Please enter the sink Node")
        self.label_sink.config(font=25)
        self.label_sink.grid(column=0, row=1,padx=10, pady=10)
    #second textbox of the sink node input
        self.textbox_sink = tk.Entry(width=20)
        self.textbox_sink.grid(column=1, row=1, pady=10)
    #third textbox for the array of connections
        self.textbox_arry = tk.Text(height=10, width=79)
    #vscroller for the scrolling over the array of inputs
        self.vertscroll = tk.Scrollbar()
        self.vertscroll.config(command=self.textbox_arry.yview)
        self.textbox_arry.config(yscrollcommand=self.vertscroll.set)
        self.textbox_arry.grid(column=1, row=2)
        self.vertscroll.grid(column=2, row=2, sticky='NS')
    #the submit button
        self.button_submit = tk.Button(text="submit", fg="black",width=25,height=1,command=self.submit)
        self.button_submit.grid(column=1,row=3,padx=15,pady=15)
    #the quit button
        self.button_quit = tk.Button(text="QUIT", fg="red", width=25, height=1, command=sys.exit)
        self.button_quit.grid(column=1, row=6, padx=15, pady=25)
    #result_label
        self.label_result=tk.Label(text="The Result is: ")
        self.label_result.config(font=25)
        self.label_result.grid(column=0,row=3)
    #detailed data button
        self.button_details = tk.Button(text="Save & show details", fg="black", width=25, height=1, command=self.Detailed_data)
        self.button_details.grid(column=1, row=4, padx=15, pady=25)
    #detailed_data of first iteration
        self.button_details_itr = tk.Button(text="Save steps & show details", fg="black", width=25, height=1,command=self.Detailed_data2)
        self.button_details_itr.grid(column=1, row=5, padx=15, pady=25)
    #ournames_label
        self.label_result = tk.Label(text="Implemented by: George Nabil 20160087, Mohamed shabaan 20160209")
        self.label_result.config(font=25)
        self.label_result.grid(column=1, row=7)
    #execute the page
        self.mainWindow.mainloop()

    def retrive_Source(self):
        source = self.textbox_source.get()
        return source
    def retrive_Sink(self):
        sink = self.textbox_sink.get()
        return sink
    def retrive_array(self):
        arry = self.textbox_arry.get(1.0, tk.END + "-1c")
        arrycov=arry.split('\n')
        final_conv=[]
        for i in arrycov:
            final_conv.append(i.split(','))
        return final_conv
    def submit(self):
        source = int(self.retrive_Source())
        sink = int(self.retrive_Sink())
        graphy = self.retrive_array()
        for i in range(0, len(graphy)):
            for j in range(0, len(graphy[i])):
                graphy[i][j] = int(graphy[i][j])
        global final_graph
        final_graph= graphy
        g = Graph(graphy)
        maxFlow=g.FordFulkerson(source,sink)
        print(maxFlow)
        self.label_result.config(text ="The Maximum Flow is: {}".format(maxFlow))
        visual_graph(graphy)
    def Detailed_data(self):
        source=int(self.retrive_Source())
        sink = int(self.retrive_Sink())
        graphy = self.retrive_array()
        for i in range(0, len(graphy)):
            for j in range(0, len(graphy[i])):
                graphy[i][j] = int(graphy[i][j])
        g = Graph(graphy)
        maxFlow = g.FordFulkersonMutated(source, sink)
    def Detailed_data2(self):
        graphy=self.retrive_array()
        for i in range(0, len(graphy)):
            for j in range(0, len(graphy[i])):
                graphy[i][j] = int(graphy[i][j])
        visual_detailed_graph_first(graphy)



#g = Graph(graph)
ui=UI()



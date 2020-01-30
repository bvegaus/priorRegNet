# -*- coding: utf-8 -*-
"""

"""
import pandas as pd
import networkx as nx

predicted_graph = nx.read_edgelist('./data/networks/XXXX.txt', delimiter = ',')
real_graph = nx.read_edgelist('./data/trueNetwork/XXXX.txt', delimiter = ',')
real_graph.remove_node('')

#Add nodes to predicted graph which exist in real_graph and not in predicted_graph
real_graph.add_nodes_from(n for n in grafo_predicho.nodes() if n not in real_graph.nodes())

#Intersection --> True Positives
aux = real_graph.copy()
aux.remove_nodes_from(n for n in real_graph if n not in grafo_predicho)
aux.add_nodes_from(n for n in grafo_predicho.nodes() if n not in aux.nodes())
TP = nx.intersection(aux, grafo_predicho)
TP.number_of_edges() 

#Difference (predicted - real) --> False Positives
FP = nx.difference(grafo_predicho, aux)
FP.number_of_edges()   

#Difference (real - predicted) --> False Negatives
FN = nx.difference(aux, grafo_predicho)
FN.number_of_edges()

#Disjoint union --> True Negatives
TN_complementario = nx.complement(grafo_predicho)
TN = nx.difference(TN_complementario, aux)
TN.number_of_edges()

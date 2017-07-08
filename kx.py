from pylab import show, hist, figure
import networkx as nx1

G = nx1.read_gml('lesmiserables.gml',relabel=True)

def most_important(G):
 """ returns a copy of G with
     the most important nodes
     according to the pagerank """ 
 ranking = nx1.betweenness_centrality(G).items()
 print ranking
 r = [x[1] for x in ranking]
 m = sum(r)/len(r) # mean centrality
 print m
 t = m*4 # threshold, we keep only the nodes with 3 times the mean
 print t
 Gt = G.copy()
 for k, v in ranking:
  if v < t:
   Gt.remove_node(k)
 return Gt

Gt = most_important(G) # trimming

from pylab import show
# create the layout
pos = nx1.spring_layout(G)
# draw the nodes and the edges (all)
nx1.draw_networkx_nodes(G,pos,node_color='b',alpha=0.2,node_size=8)
nx1.draw_networkx_edges(G,pos,alpha=0.1)

# draw the most important nodes with a different style
nx1.draw_networkx_nodes(Gt,pos,node_color='r',alpha=0.4,node_size=254)
# also the labels this time
nx1.draw_networkx_labels(Gt,pos,font_size=12,font_color='b')
show()

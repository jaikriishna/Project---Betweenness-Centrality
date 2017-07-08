from pylab import show, hist, figure
import networkx as nx
# read the graph (gml format)
G = nx.read_gml('lesmiserables.gml',relabel=True)

# drawing the full network
figure(1)
nx.draw_spring(G,node_size=0,edge_color='b',alpha=.2,font_size=10)
show()

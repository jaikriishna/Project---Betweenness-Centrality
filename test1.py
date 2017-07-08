from pylab import show, hist, figure
import networkx as net
MAP= net.read_gml('lesmiserables.gml',relabel=True)


def influence(G):
	place=net.betweenness_centrality(MAP).items()
	print place
	i=[f[1] for f in place]
	mean=sum(i)/len(i)
	print mean
	comp= mean*2
	print comp
	mapx = MAP.copy()
	for y,u in place:
		if u<comp:
			mapx.remove_node(y)
	return mapx
			
mapx= influence(map)

from pylab import show
test = net.spring_layout(MAP)
net.draw_networkx_nodes(MAP,test,node_color='b',alpha=0.2,node_size=8)
net.draw_networkx_edges(MAP,test,alpha=0.1)
net.draw_networkx_nodes(mapx,test,node_color='r',alpha=0.4,node_size=254)
net.draw_networkx_labels(mapx,test,font_size=12,font_color='b')
show()

from multiprocessing import Pool
import time
import networkx as net
import itertools

def parpro(MAP_normalized_weight_source_tuple):
	return net.betweenness_centrality_source(*MAP_normalized_weight_source_tuple)


def division(lis,nodes):
	list_temp=iter(lis)
	while 1:
		x=tuple(itertools.islice(list_temp,nodes))
		if not x:
			return
		yield x

def betweenness_centrality_par(MAP,processes=2):
	p=Pool(processes=processes)
	n_break=len(p._pool)*4
	n_pieces=list(division(MAP.nodes(), int (MAP.order()/n_break)))
	chunk=len(n_pieces)
	temp=p.map(parpro,zip([MAP]*chunk,[True]*chunk,[None]*chunk,n_pieces))
	
	red=temp[0]
	for l in temp[1:]:
		for n in l:
			red[n]+=l[n]
	return red

if __name__=="__main__":
	nodes_amount=100
	MAP_rand = net.barabasi_albert_graph(nodes_amount, 4)
	start=time.time()
	for MAP	in [MAP_rand]:
		print("Betweenness Centrality for:")
		print(net.info(MAP))
		for u in MAP_rand:		
	#		print("\tNo Parallellism Processing:")
	#		start=time.time()
	#		bet=net.betweenness_centrality(MAP)		
	#		print("\t\tTime: %.6F seconds" % (time.time()-start))
	#		print("\t\tBetweenness centrality for node %d: %.6F" % (u,bet[u]))
	#		print("\tParallellism Processing:")
	#		start=time.time()
			bet=betweenness_centrality_par(MAP)
	#		print("\t\tTime: %.6F seconds" % (time.time()-start))
			print("\t\tBetweenness centrality for node %d: %.6F" % (u,bet[u]))	
	print("")
	print("\t\tTime: %.6F seconds" % (time.time()-start))

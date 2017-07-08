from multiprocessing import Pool
import multiprocessing
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

def betweenness_centrality_par(MAP,processes=None):
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

def func(u,MAP_rand):	
	start=time.time()
	bet=net.betweenness_centrality(MAP)		
	print("\t\tTime: %.6F seconds" % (time.time()-start))
	return("\t\tBetweenness centrality for node %d: %.6F" % (u,bet[u]))
	#print("\tParallellism Processing:")
	#start=time.time()
	#bet=betweenness_centrality_par(MAP)
	#print("\t\tTime: %.6F seconds" % (time.time()-start))
	#print("\t\tBetweenness centrality for node %d: %.6F" % (u,bet[u]))

def calculate(func, args):
    result = func(*args)
    return '%s' % (result)


def test():
	PROCESSES = 3
    	pool=Pool(PROCESSES)
        TASKS = [(func, (i,1000)) for i in range(1000)]

        results = [pool.apply_async(calculate, t) for t in TASKS]
	for r in results:
            print(r.get())


if __name__=="__main__":
	nodes_amount=1000
	MAP_rand = net.barabasi_albert_graph(nodes_amount, 4)
	for MAP	in [MAP_rand]:
		print("Betweenness Centrality for:")
		print(net.info(MAP))
		test()
		print("")

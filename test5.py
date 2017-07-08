from multiprocessing import Pool,Manager,Queue
import multiprocessing
import multiprocessing.pool
import time
import networkx as net
import itertools


class NoDaemonProcess(multiprocessing.Process):
    def _get_daemon(self):
        return False
    def _set_daemon(self, value):
        pass
    daemon = property(_get_daemon, _set_daemon)

class MyPool(multiprocessing.pool.Pool):
    Process = NoDaemonProcess



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



def func(u,MAP_rand,que,qu):	
	start=time.time()
	bet=betweenness_centrality_par(MAP)
	que.put(bet[u])
	qu.put(u)
	print("\t\tTime: %.6F seconds" % (time.time()-start))
	return("\t\tBetweenness centrality for node %d: %.6F" % (u,bet[u]))
		

def calculate(func, args):
    result = func(*args)
    return '%s' % (result)


def test(num):
	n=num
	PROCESSES = None
	sum=0
	l=0
	ar=[]
	m = Manager()
    	q = m.Queue()
	lo=m.Queue()
	arr=[]
	lis=[]
	pos=[]
    	pool=MyPool(PROCESSES)
        TASKS = [(func, (i,n,q,lo)) for i in range(n)]

        results = [pool.apply_async(calculate, t) for t in TASKS]
	for r in results:
            print(r.get()) 
	for u in range (n):
		l=q.get()
		k=lo.get()		
		ar.append(l)
		lis.append(k)
		sum=sum+l
	mean=sum/n
	comp= mean*2
	print("Min required BC to influence the network :")
	print(comp)
	for u in range(n):
		if ar[u]>comp:
			arr.append(ar[u])
			pos.append(lis[u])

	print("Hence most Influential NODES in the network are :")
	print(pos,arr)

if __name__=="__main__":
	nodes_amount=1000
	MAP_rand = net.barabasi_albert_graph(nodes_amount, 4)
	for MAP	in [MAP_rand]:
		print("Betweenness Centrality for:")
		print(net.info(MAP))
		test(nodes_amount)
		print("")

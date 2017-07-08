from multiprocessing import Pool,Manager,Queue
import multiprocessing
import time
import networkx as net
import itertools


def func(u,MAP_rand,que,qu):	
	#start=time.time()
	bet=net.betweenness_centrality(MAP)
	que.put(bet[u])
	qu.put(u)
	#print("\t\tTime: %.6F seconds" % (time.time()-start))
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
    	pool=Pool(PROCESSES)
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
	comp= mean*4
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
	start=time.time()	
	for MAP	in [MAP_rand]:
		print("Betweenness Centrality for:")
		print(net.info(MAP))
		test(nodes_amount)
		print("")
	print("\t\tTime: %.6F seconds" % (time.time()-start))

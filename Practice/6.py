import multiprocessing as mp

def func(q):
	q.put([1,True,'Ashe'])

if __name__=='__main__':
	q=mp.Queue()
	p=mp.Process(target=func,args=(q,))
	p.start()
	print(q.get())
	p.join()

import multiprocessing as mp

def func(q):
	q.put('World')

if __name__== '__main__':
	#mp.set_start_method('spawn') #for some reason doesnt work
	q=mp.Queue()
	p=mp.Process(target=func, args=(q,))
	p.start()
	print(q.get())
	p.join

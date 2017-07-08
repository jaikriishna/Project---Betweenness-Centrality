import multiprocessing as mp

def func(name):
	print('hello by',name)

p=mp.Process(target=func,args=('ashe',))
p1=mp.Process(target=func,args=('leon',))
p.start()
p1.start()
p.join()
p1.join()

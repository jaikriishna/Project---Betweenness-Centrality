import multiprocessing as mp
def func(l,i):
	l.acquire()
	try:
		print("Checking",i)
	finally:
		l.release()

if __name__=='__main__':
	lock=mp.Lock()
	for i in range(10):
		mp.Process(target=func, args=(lock,i)).start()
		

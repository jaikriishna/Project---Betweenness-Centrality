import multiprocessing as mp

def func(n,a):
	print(mp.cpu_count())
	n.value=3.1415927
	for i in range(len(a)):
		a[i]=-a[i]

if __name__=='__main__':
	num=mp.Value('d',0.0)
	arr=mp.Array('i',range(10))
	
	p=mp.Process(target=func, args=(num,arr))
	p.start()
	p.join()
	print(num.value)
	print(arr[:])

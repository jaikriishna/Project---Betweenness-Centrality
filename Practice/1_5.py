import multiprocessing
import time
import random
import sys

def calculate(func, args):
    result = func(*args)
    return '%s says that %s%s = %s' % (
        multiprocessing.current_process().name,
        func.__name__, args, result
        )

def mul(a, b):
    return a * b

def test():
    	PROCESSES = 4
    	pool=multiprocessing.Pool(PROCESSES)
        TASKS = [(mul, (i, 7)) for i in range(10)]

        results = [pool.apply_async(calculate, t) for t in TASKS]
        
	print('Ordered results using pool.apply_async():')
        for r in results:
            print('\t', r.get())

if __name__=='__main__':
	test()

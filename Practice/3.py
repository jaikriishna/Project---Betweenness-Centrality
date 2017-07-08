from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def func(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
	info('main line')
	p=Process(target=func,args=('ashe',))
	p1=Process(target=func,args=('leon',))
	p.start()
	p1.start()
	p.join()
	p1.join()


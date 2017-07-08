from multiprocessing import Pool

def f(x):
    return x*x


p=Pool(3)
job=[]
for x in range(10000000):
	job.append(x)
print(p.map(f, job))
for r in results:
            print('\t', r.get())
        


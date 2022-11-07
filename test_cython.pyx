import time

cdef float t1
t1 = time.time()

cdef unsigned long long int sum_var1
sum_var1 = 0

cdef unsigned long long int maxval
maxval = 1000000000

cdef int k
for k in range(maxval):
	sum_var1 += k

print(f"-- {time.time() - t1} seconds --")

import time

t1 = time.time()

sum_var1 = 0
for k in range(1000000000):
	sum_var1 += k

print(f"-- {time.time() - t1} seconds --")

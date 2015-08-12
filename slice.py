import sys
import os

count = int(sys.argv[1])
len = 100
step = count / len

p = 0
while p <= step:
	beg = p * len
	end = beg + len
	if p == step:
		end = count
	
	if (beg < end):
		print( beg, end, count, 'process len = %d' % (end - beg) )
	
	p += 1
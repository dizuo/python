# np++
# peteryfren
# 20160216
'''
The required state consists of a flag indicating if the first triangle has been
completed, two stored processed vertices, (called vertex A and vertex B), and a
one bit pointer indicating which stored vertex will be replaced with the next vertex.
The pointer is initialized to point to vertex A. Each successive vertex toggles the
pointer. Therefore, the first vertex is stored as vertex A, the second stored as vertex
B, the third stored as vertex A, and so on. Any vertex after the second one sent
forms a triangle from vertex A, vertex B, and the current vertex (in that order).
'''

import os, sys

def main():
	cache = []
	cache.append(1)
	cache.append(2)
	
	idx = 3
	pp = 0
	
	while idx <= 10:
		print( 'triangle is (%d, %d, %d), %d' % (cache[0], cache[1], idx, pp) )
		
		cache[pp] = idx
		idx += 1
		pp = 1 - pp
	
if __name__ == "__main__":
	main()
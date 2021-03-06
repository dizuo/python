import sys
import os
import math

def my_str_to_int(s):
	if s[-1] == 'w':
		s = s[0:len(s)-1]
	

def process(fname):
	total = 0
	with open(fname, 'r') as fp:
		while True:
			line = fp.readline()
			if not line:
				break
			
			if len(line) < 2:
				continue
			
			line = line.strip()
			res = line.split(' ', 3)
			if len(res) < 3:
				continue
			
			print( '%s\t\t%s' % (res[0], res[1]) )
			
			val = int(res[1])
			total += val
			
	print ( 'total = %d' % total )
	

def main():
	
	if len(sys.argv) <= 1:
		print( "%s : money.txt" % sys.argv[0] )
		sys.exit(1)
	
	fname = sys.argv[1]
	process(fname)
	
if __name__ == "__main__":
	main()
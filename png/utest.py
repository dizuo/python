#np++
import os, struct, sys, zlib
from parse import * 

unpack = struct.unpack

def main(fname):
	with open(fname, 'r') as fp:		
		while True:
			path = fp.readline()
			if not path:
				break
			path = path.strip('\n')
			
			if len(path) < 2:
				continue
			
			parse_main(path)
		
if __name__ == "__main__":	
	if len(sys.argv) < 2:
		print( sys.argv )
		print('Usage [%s: list]' % sys.argv[0])
		sys.exit(1)
	
	fname = sys.argv[1]
	main(fname)
	
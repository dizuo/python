import sys
import os


def hex_short_to_str(ust):
	s=""
	for i in range(len(ust)/4):
		us=ust[i*4:i*4+4]
		s=s+unichr(int(us,16))
		#print s
	
	return s

# 4e2d,5173,6751,5357,5927,8857,33,31,53f7,9662,505c,8f66,573a,
def dump_my_str(ss):
	res = ss.split(',')
	print(res)
	
	unicode_str = ''
	
	for item in res:
		ust = ''
		
		if  len(item) < 1:
			continue
		
		if len(item) == 2:
			ust = '00' + item
		else:
			ust = item
		
		unicode_str += hex_short_to_str(ust)
	
	print( unicode_str )
	
if __name__ == "__main__":
	if len(sys.argv) < 2:
		print( '%s : unicode_string' % sys.argv[0] )
		print( sys.argv )
		sys.exit(1)
	
	my_str = sys.argv[1]
	dump_my_str(my_str)
	#hex_short_to_str(ust)
	
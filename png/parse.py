#np++
import os, struct, sys, zlib

unpack = struct.unpack

def parse_main(fname):
	with open(fname, 'rb') as fp:		
		fp.seek(0, 2)
		first_file_size = fp.tell()    
		fp.seek(0, 0)
		#print('file length = %d' % file_size)
		
		proc_flag = True
		
		fp.read(8)		
		while True:
			len = unpack('>i',  fp.read(4))[0]
			sign = fp.read(4)
			print(len, sign)
			
			if 'IEND' in sign:
				last_crc = fp.read(4)
				if first_file_size != fp.tell():
					proc_flag = False
				#print( 'file size = %d' % fp.tell() )
				break
			
			if len > 0:
				data = fp.read(len)
			crc = fp.read(4)
		
		print('--------------------------')
		if proc_flag == False:
			print('bad png')
		
if __name__ == "__main__":	
	if len(sys.argv) < 2:
		print( sys.argv )
		print('Usage [%s: test.png]' % sys.argv[0])
		sys.exit(1)
	
	fname = sys.argv[1]
	parse_main(fname)
	
#np++
import os, struct, sys, zlib
import binascii

unpack = struct.unpack
pack = struct.pack

def parse_main(fname):

	dst_bys = []
	
	with open(fname, 'rb') as fp:		
		fp.seek(0, 2)
		first_file_size = fp.tell()    
		fp.seek(0, 0)
		#print('file length = %d' % file_size)
		
		proc_flag = True
		
		headers = fp.read(8)
		dst_bys.append( headers )
		
		while True:
			bs = fp.read(4)
			chunk_len = unpack('>i', bs)[0]		
			dst_bys.append(bs)
			
			sign = fp.read(4)
			dst_bys.append(sign)
			print(chunk_len, sign)
			
			if 'IEND' in sign:
				last_crc = fp.read(4)
				dst_bys.append(last_crc)
				
				if first_file_size != fp.tell():
					proc_flag = False
				#print( 'file size = %d' % fp.tell() )
				break
			
			if chunk_len > 0:
				data = fp.read(chunk_len)
				dst_bys.append(data)
				
			crc = fp.read(4)
			dst_bys.append(crc)
			
			if 'IHDR' in sign:
				header_s = 'eRYF'
				data_s = 'hello world, my name is renyafei. This data is my private data. 我的名字叫任亚飞。'
				total_s = header_s + data_s
				
				loc_len = len(data_s)
				dst_bys.append( pack('>i', loc_len) )
				dst_bys.append( total_s )
				
				loc_crc = binascii.crc32(total_s) & 0xFFFFFFFF
				print(loc_crc)
				dst_bys.append( pack('>I', loc_crc) )				
		
		print('--------------------------')
		if proc_flag == False:
			print('bad png')
		
		with open('data_hiding.png', 'wb') as fp:
			for ch in dst_bys:
				fp.write(ch)
			fp.flush()
		
if __name__ == "__main__":	
	if len(sys.argv) < 2:
		print( sys.argv )
		print('Usage [%s: test.png]' % sys.argv[0])
		sys.exit(1)
	
	fname = sys.argv[1]
	parse_main(fname)
	
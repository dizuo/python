import os
import sys
import struct

unpack = struct.unpack

if len(sys.argv) <= 1:
	print("empty...")
	sys.exit(1)

fp = open(sys.argv[1], 'rb')
fp.seek(0, 2)#from end
filesize = fp.tell()
print(filesize)
fp.seek(0, 0)

dirIndex = unpack('i', fp.read(4))[0]
level = unpack('i', fp.read(4))[0]
blockno = unpack('i', fp.read(4))[0]
print( 'dir = %d, level = %d, blockno = %d' % (dirIndex, level, blockno) )

sign = unpack('4s', fp.read(4))[0]
version = unpack('i', fp.read(4))[0]
offset = unpack('I', fp.read(4))[0]
blocksize = unpack('I', fp.read(4))[0]

crc = unpack('I', fp.read(4))[0]

print( 'sign = %s, version = %d, offset = %d, blocksize = %d' % (sign, version, offset, blocksize) )

print( crc )

fp.close()


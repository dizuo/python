# -*- coding: cp936 -*-
# np++

import sys
import os

base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]

def byte2bin(val):
	res = bin(val)[2:]
	
	mid = []
	for i in range( 8-len(res) ):
		mid.insert(0, '0')
	
	return ''.join(mid) + res

def val2bin(val):
	ls = []
	while True:
		if val == 0:	break
		
		loc = byte2bin(val % 256)		
		ls.insert(0, loc)
		val = val / 256		
	
	res = ''
	for s in ls:	
		res+=s	
		res+=' '
	return res

def bin_test():
	s = 'ren亚'
	bs = bytes(s)
	
	print(' \'r\' bin : %s' % bin(ord(bs[0]))[2:] )
	
	#print( bin(bs[0]) )
	
def hexdump(src, length=8):
	result = []
	digits = 4 if isinstance(src, unicode) else 2
	for i in xrange(0, len(src), length):
		s = src[i:i+length]
		hexa = b' '.join(["%0*X" % (digits, ord(x))  for x in s])
		text = b''.join([x if 0x20 <= ord(x) < 0x7F else b'.'  for x in s])
		result.append( b"%04X   %-*s   %s" % (i, length*(digits + 1), hexa, text) )
	
	return b'\n'.join(result)
	
if __name__ == "__main__":
	bin_test()
	
	for i in range(10):
		print( i, byte2bin(i) )
	
	s = 'renyafei'
	for ch in s:
		print( ch, byte2bin(ord(ch)) )
	
	utfs = u'任亚飞'.encode('utf-8')
	print( hexdump(utfs) )
	
	print( val2bin(0xE4) )
	print( val2bin(0xE9) )
	
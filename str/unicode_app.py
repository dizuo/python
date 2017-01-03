#np++

def sh_to_us(val):
	print ( ('\u' + hex(val)[2:]).decode('unicode-escape') )

sh_to_us(0x4e2d)

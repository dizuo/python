#np++
#peteryfren 2017-1-2
#test multiplayer.

def sh_to_us(val):
	print ( ('\u' + hex(val)[2:]).decode('unicode-escape') )

def window_unit_test(val, cnt):
	tmpval = val
	while val < tmpval + cnt:
		sh_to_us(val)
		val += 1
	
if __name__ == "__main__":
	sh_to_us(0x4e2d)
	window_unit_test(0x4e2d, 4)
	

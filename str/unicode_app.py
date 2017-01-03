#np++
#peteryfren 2017-1-2
#test multiplayer.

def sh_to_us(val):
	print ( ('\u' + hex(val)[2:]).decode('unicode-escape') )

def unit_test(val):
	cnt = 4
	while val < val+cnt:
		sh_to_us(val)
		val += 1
	
if __name__ == "__main__":
	sh_to_us(0x4e2d)
	unit_test()
	

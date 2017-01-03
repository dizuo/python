#np++
#peteryfren 2017-1-2
#test multiplayer.

def sh_to_us(val):
	print ( ('\u' + hex(val)[2:]).decode('unicode-escape') )

if __name__ == "__main__":
	sh_to_us(0x4e2d)

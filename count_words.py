import os
import sys

def main():
	fname = sys.argv[1]
	
	with open(fname, 'r') as fp:
		isme = 0
		me_line_cnt = 0
		she_line_cnt = 0
		
		me_word_cnt = 0
		she_word_cnt = 0
		
		while True:
			line = fp.readline()			
			if not line:
				break
			if '...' in line:
				isme = 0
				continue
			if 'peter' in line and ':' in line:
				isme = 1
				continue
			
			if isme == 0:
				she_line_cnt += 1
				me_word_cnt += len(line)
			else:
				me_line_cnt += 1
				she_word_cnt += len(line)
				
			print( isme, line.strip() )
		
		print( 'my lines = %d, words = %d' % (me_line_cnt, me_word_cnt) ) 
		print( 'you words = %d, words = %d' % (she_line_cnt, she_word_cnt) ) 

if __name__ == "__main__":
	main()
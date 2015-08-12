#notepad++

import os
import sys

# replace all file with this file.
my_head='./Head/2/2F06179372E2514E68C9D4D3B33C57D2'

# like tree tool in linux.
def my_tree(src_dir, indent=""):
	
	#print( src_dir, os.listdir(src_dir) )
	
	for cname in os.listdir(src_dir):
		src_file = os.path.join(src_dir, cname)		
		if os.path.isdir(src_file):
			print( '%s%s' % (indent,cname) )
			next_indent = indent +  "\t"
			my_tree(src_file, next_indent)
		elif '2F06179372E2514E68C9D4D3B33C57D2' in cname:
			print('skip it file')
		else:
			#print( cname )
			print( src_file )
			open(src_file, "wb").write(open(my_head, "rb").read())
		
def main():
	my_tree('./Head')	
	
if __name__ == "__main__":
	main()
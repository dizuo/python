import os
import sys

# like tree tool in linux.
def my_tree(src_dir, indent=""):
    for cname in os.listdir(src_dir):

        src_file = os.path.join(src_dir, cname)
        if os.path.isdir(src_file):

            print( '%s%s' % (indent,cname) )
            next_indent = indent +  "\t"
            my_tree(src_file, next_indent)

def main():
    if len(sys.argv) <= 1:
        print( "empty parameters..." )
        print( "usage[ %s : dir_name ]" % sys.argv[0] )
        sys.exit(1)

    my_tree( sys.argv[1] )

if __name__ == "__main__":
    main()

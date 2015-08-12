#encoding: gbk

'''
# Edit by IDLE
# peteryfren 20150319
# edit create with atom.
# display all parking floors...
# sample output:

北京市
        100081
                B3
                B4
        100050
                B1
                B2
        100067
                B2
        100017
                B1
        100098
                B1
        100012
                B2
                B3
        100051
                B2
                B3
        100052
                B2
                B3
                B4
'''

import os
import sys

# like tree tool in linux.
def my_tree(src_dir, xdict, indent=""):
    for cname in os.listdir(src_dir):

        src_file = os.path.join(src_dir, cname)
        if os.path.isdir(src_file):
            #print dirname or parking id.
            #if xdict.__contains__(cname) == True:
            #    print( '%s%s' % (indent, xdict[cname]) )
            #else:
            print( '%s%s' % (indent,cname) )

            next_indent = indent +  "\t"
            my_tree(src_file, xdict, next_indent)

def main():
    if len(sys.argv) <= 1:
        print( "empty parameters..." )
        print( "usage[ %s : dir_name ]" % sys.argv[0] )
        sys.exit(1)

    # load dir dict from file.
    dir_dict = {}
    fname = sys.argv[1] + '/NIParkingIndex.txt'
    print(fname)
    fp = open(fname, 'r')
    while True:
        line = fp.readline()
        if not line:
			break
        res = line.split(' ', 3)
        id = res[0]
        dir_name = res[1]
        #print( dir_name )
        #print( '%s == %s' % (dir_name, id) )

        if dir_dict.__contains__(dir_name) == False:
            dir_dict[dir_name] = id
    fp.close()

    #print(dir_dict)
    
    my_tree( sys.argv[1], dir_dict )

if __name__ == "__main__":
    main()

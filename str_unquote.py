# -*- coding: cp936 -*-
import sys, urllib

ss = '%E5%8C%97%E4%BA%AC%E5%B8%82'
print(sys.getdefaultencoding())

tt = urllib.unquote(ss)

# print in python IDE right, in cmd random chars...
print( type(tt) )
print( 'This is utf-8 sequence : ', tt )
print(tt)

#
gbks = tt.decode('utf-8').encode('gbk')
print( type(gbks) )
print( 'This is gbk sequence : ', gbks )
print(gbks)

us = u'北京市'
print( 'This is unicode sequence : ', us)
print(us)


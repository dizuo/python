# -*- coding: cp936 -*-
# http://d.hd.baofeng.com/ search 任亚飞, url如下：
# http://d.hd.baofeng.com/q_JUU0JUJCJUJCJUU0JUJBJTlBJUU5JUEzJTlF

import urllib, base64

def my_encrypt(ches):
    utf_s = ches.encode('utf-8')
    print('utf-8 str : %s' % utf_s)
    url_s = urllib.quote(utf_s)
    print('url quote str : %s' % url_s)
    return base64.b64encode(url_s)

def my_decrypt(srcs):
    url_s = base64.b64decode(srcs)
    print(url_s)
    return urllib.unquote(url_s)

if __name__ == "__main__":
    s = u'任亚飞'
    res = my_encrypt(s)
    print('after encrypt : %s' % res)

    srcs = my_decrypt(res)
    print(srcs)
    
    

    


# encoding: UTF-8

import re

def main():
    ss = '595525,1,24 => {10375,single,1,17763781} {10376,single,1,17763782}'
    pat = re.compile(r'\W+')# ƥ��ǵ����ַ�
    pat1 = re.compile(r'\D+')# ������
    pat2 = re.compile(r'\d+')# ����
    tok = re.compile(r'=> ')# �򵥷ָ�

    print( pat.split(ss) )
    print( pat1.split(ss) )
    print( pat2.split(ss) )
    print( tok.split(ss) )

if __name__ == "__main__":
    main()

#!/usr/bin/python
#coding:utf-8
from multiprocessing.dummy import Pool as ThreadPool 

def push2wx(opend_id):
 print opend_id

users = [
 'open_id_1', 
 'open_id_2',
 'open_id_3',
 'open_id_4',
 'open_id_5',
 'open_id_6',
 'open_id_7',
 'open_id_8'
 # etc.. 
 ]

# 初始化线程池，4为线程数，默认使用cpu核数
pool = ThreadPool(4) 

# 线程池中的空余线程会执行 push2wx(users[i])
results = pool.map(push2wx, users)

print( results )
pool.close() 
pool.join() 
# 打完收工

# 跑出结果的时间从零点几秒到几十秒不等。。不能算是个合格的答案。第一次拍的时候直接0.1秒出答案吓我一跳。。
import hashlib
import itertools
import time
import sys
from random import *

def gethash(str1):
    str1 = str1.encode('ascii')
    m = hashlib.sha1()
    m.update(str1)
    return m.hexdigest()

start_time = time.time()
hashvalue = '67ae1a64661ac8b4494666f58c4822408dd0a3e4'

data = ['qwin%(=*', 'QWIN580+']
data3 = [0]*8
while(True):
    for i in range(8):    
        data3[i] = data[randint(0,1)][i]
    list1 = list(itertools.permutations(data3,8))
    list2 = [''.join(x) for x in list1]
    
    for j in list2:
        if gethash(''.join(j)) == hashvalue:
            print(''.join(j),"---%s seconds ---" %(time.time()-start_time))
            sys.exit(0)


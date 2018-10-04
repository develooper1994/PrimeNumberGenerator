'''
Created on 8 Eyl 2016

@author: selcu
'''
from asal import * #asal.asalmı yazmak yerine asalmı yazarak kullanacağım. her zaman kullanılmaz birden fazla aynı adda fonksiyon varsa karışır.


asalmı_gelismis_birlerbas(10000000001)

from random import randint
import time
print('\n'*5)
try:
    inp=int(input('bir sayı girin ve asal mı diye kontrol edin.'))
except ValueError:
    inp=randint(-100,100)
print(inp,':',end=' ')
now=time.clock()
asalmı_gelismis_birlerbas(inp)
last=time.clock()
print('bu kadar zamanda tamamladı.',last-now)








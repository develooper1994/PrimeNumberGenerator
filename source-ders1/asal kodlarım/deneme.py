'''
Created on 9 Eyl 2016

@author: robotik
'''
import time
from asal import asalmı_gelismis_asallardan,asalmı_gelismis  ,  deneme_asalmı_gelismis_asallardan

print(asalmı_gelismis_asallardan(10000001))
print(asalmı_gelismis(10000001))
print(asalmı_gelismis_asallardan(4141))
print(asalmı_gelismis(4141))
print(asalmı_gelismis_asallardan(319))
print(asalmı_gelismis_asallardan(102))
print(asalmı_gelismis_asallardan(103))
print(asalmı_gelismis_asallardan(10000001))
print(asalmı_gelismis_asallardan(319))
print(asalmı_gelismis_asallardan(4141))

now=time.clock()
print('31371',asalmı_gelismis(31371))
last=time.clock()
print(last-now)

now=time.clock()
print('31371',asalmı_gelismis_asallardan(31371))
last=time.clock()
print(last-now)

print('\n'+'-*'*40+'\n')

print(deneme_asalmı_gelismis_asallardan(10000001))
print(deneme_asalmı_gelismis_asallardan(4141))
print(deneme_asalmı_gelismis_asallardan(319))
print('102:',deneme_asalmı_gelismis_asallardan(102))
print('103',deneme_asalmı_gelismis_asallardan(103)) # True
print(deneme_asalmı_gelismis_asallardan(10000001))
print(deneme_asalmı_gelismis_asallardan(319))
print(deneme_asalmı_gelismis_asallardan(1681))
print(deneme_asalmı_gelismis_asallardan(4141))
now=time.clock()
print('31371',deneme_asalmı_gelismis_asallardan(31371))
last=time.clock()
print(last-now)

print('\n'+'-*'*40+'\n')

print(deneme_asalmı_gelismis_asallardan(0))
print(deneme_asalmı_gelismis_asallardan(1))
print(deneme_asalmı_gelismis_asallardan(-1))
print(deneme_asalmı_gelismis_asallardan(2))
print(deneme_asalmı_gelismis_asallardan(7))
print(deneme_asalmı_gelismis_asallardan(-11))
print(deneme_asalmı_gelismis_asallardan(101))
now=time.clock()
print('31371',deneme_asalmı_gelismis_asallardan(31371))
last=time.clock()
print(last-now)

print('\n'+'-*'*40+'\n')
#asallar

now=time.clock()
print('179426549',asalmı_gelismis(179426549))
last=time.clock()
print(last-now)

now=time.clock()
print('179426549',asalmı_gelismis_asallardan(179426549))
last=time.clock()
print(last-now)

now=time.clock()
print('179426549',deneme_asalmı_gelismis_asallardan(179426549))
last=time.clock()
print(last-now)
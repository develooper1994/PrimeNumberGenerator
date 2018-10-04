'''
Created on 8 Eyl 2016

@author: robotik
'''
from test.test_binop import isnum
print('python')
print()
print('robotik '*5,end='-*-*-*-*-*-*-*-*-*') # end varsayılan olarak '\n'satır başıdır. siz end yerine ne koyarsanız print onu yapar.
print('3.1 '+'2.2 '*3)
print(float('3.1')+float('2.2'))
#print(int('3.1')+int('2.2')) #hata
print(int(3.2)+int(0.8))
print(int(float('3.2'))+int(float('0.8')))
print('İstanbul\'un taşı toprağı altındı.')
print('''İstanbul\'un taşı toprağı altındı.''')


print('t' in 'robotoik') #t robotik kelimesinin içinde mi?
print('t' is 'robotik') #t robotik kelimesi mi?
print('t' == 'robotik')

sep='-'
dogumtarifi=['05','11','1900']
print(sep.join(dogumtarifi))
print(dogumtarifi)

if 't' in 'robotik':
    print("butik")
else:
    import math
    print(math.atan(5/4))
# -4,-3,-2,-1
#  0,1,2 ,3
L=[1,8,27,64]

print(L[:])
print(L)
print(L[1:4])
L[1:4]='H','T','s'
print(L)
L=['a',1]
print(L)


a,b=0,1
while a<10:
    a,b=b,a+b
    print(a,end=' ')

'''
sifre='xyz'
sayac=0
son=4
while True:
    i=input('sifreyi doğru bil')
    if i=='xyz':
        print('doğru bildin geç')
        break
    else:
        sayac=sayac+1
        kalan=son-sayac
        print('yanlış,kaldı',kalan)
        
        if kalan==0:
            print('al sana, dıkşın') ; break
'''   


print() 
import asal

print('100:',end=' ')
asal.asalmı_gelismis(100)
print('a:',end=' ')
asal.asalmı_gelismis('a')
print('101:',end=' ')
asal.asalmı_gelismis(101)
print('103:',end=' ')
asal.asalmı_gelismis(103)
print('105:',end=' ')
asal.asalmı_gelismis(105)
print('107:',end=' ')
asal.asalmı_gelismis(107)
print('-107:',end=' ')
asal.asalmı_gelismis(-107)
print('0:',end=' ')
asal.asalmı_gelismis(0)
print('1:',end=' ')
asal.asalmı_gelismis(1)
print('2:',end=' ')
asal.asalmı_gelismis(2)
print('-1:',end=' ')
asal.asalmı_gelismis(-1)
print('-2:',end=' ')
asal.asalmı_gelismis(-2)
print('-11:',end=' ')
asal.asalmı_gelismis(-11)

print(isnum(1))
print(isnum(-1))
print(isnum('1'))
print(isnum('a'))
L=[1,2,3]
print(isnum(L[:]))

def isnum_foreach(s):
    for i in s:
        if not isnum(i):
            return 0
    else:
        return 1
    
print(isnum_foreach(L))  

bosluk=lambda n: print('\n','-*'*n,'\n')

bosluk(30)

import math
try:
    a=1/0
except ZeroDivisionError:
    a=math.inf

print(a)
    
    
    
    
    
    
    
    
    
    
    






























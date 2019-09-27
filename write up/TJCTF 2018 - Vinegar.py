#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 15:36:41 2019

@author: matin fallahi
"""
import sys
sys.path.append('../')
from Vinegar import Vinegar  
import itertools 
import hashlib


vi=Vinegar()
#key =  "KkkkkkkkkKkkkkkkkkKkkkkkkkkKkk" -->key 9 Letter key
flag = "uucbx{simbjyaqyvzbzfdatshktkbde}"
sha256 = "8304c5fa4186bbce7ac030d068fdd485040e65bf824ee70b0bdbac03862bec93"


for per in itertools.product('asdfghjklqwertyuiopzxcvbnm',repeat=5):
    #print(per)
    key=''.join(per)
    mflag=vi.decrypt(key,'uucbx')
    if mflag=='tjctf':
        print ("firstpart of key:",key)
        firstpart=key
        break



for per in itertools.product('asdfghjklqwertyuiopzxcvbnm',repeat=4):
    key=firstpart+''.join(per)
    mflag=vi.decrypt(key,flag)
    h = hashlib.sha256()
    h.update(mflag.encode('utf-8'))
    hflag=h.hexdigest()
    if hflag==sha256:
        print ("falag:",mflag,"\n key:",key)
        break
    
    
print("\n Best wishes. :)")
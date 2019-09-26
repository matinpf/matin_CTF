#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 15:36:41 2019

@author: matin fallahi
"""

ba=97  #ord('a')
bz=122
bA=65
bZ=90

def encrypt(k,m):
    key=k.lower()
    key_len=len(key)
    massage = m.lower()
    encrypt=''
    incrementor=0
    for i in massage:
        if(122>=ord(i)>=97):
            x=incrementor%key_len
            pre_i=(ord(i) + (ord(key[x])-97))
            #print("in shod enc",pre_i,ord(i),(ord(key[x])-97))
            if(pre_i>122):
                pre_i=pre_i-26
            encrypt=encrypt+ chr(pre_i)
            incrementor=incrementor+1
        else :
            encrypt=encrypt+i
    return(encrypt)


def decrypt(k,c):
    key=k.lower()
    key_len=len(key)
    cipher = c.lower()
    decrypt=''
    incrementor=0
    for i in cipher:
        if(122>=ord(i)>=97):
            x=incrementor%key_len
            negative=26-(ord(key[x])-97)
            pre_i=(ord(i) + negative)
            #print(ord(i))
            #print("in shod",pre_i,ord(i),negative)
            if(pre_i>122):
                pre_i=pre_i-26
            decrypt=decrypt+ chr(pre_i)
            incrementor=incrementor+1
        else :
            decrypt=decrypt+i
    return(decrypt)
     
    
m='matin[sds:]'
k='mAtin'
    
c=encrypt(k,m)
print(c)
print("=================================") 
print(decrypt(k,c))     
        
#decrypt = input('Enter text to decrypt : ')
#decrypt = decrypt.lower().replace(" ", "")
#for i in decrypt:
#    print(chr(ord(i) - 5))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 22:42:38 2020

@author: matin
"""

import subprocess

def is_english_tex(text) :
    dic_a={}
    for char in text:
        dic_a[char]=dic_a.get(char,0) + 1
    e_p= dic_a.get('E',0)/len(text)
    z_p= dic_a.get('Z',0)/len(text)
    if e_p>0.08 and z_p<0.01:
        return True
    else:
        return False



def shift_crypto(text,step):
    text=text.upper()
    dcrypted=""
    for char in text:
        if ord(char)>=65 and ord(char)<91:
            new_ord=(ord(char)-65+step)%26
            dcrypted=dcrypted+chr(new_ord+65)
        else:
            dcrypted=dcrypted+char
    return dcrypted
        
        

#r_text=".fgavbc ba av fgyhfre tavgnruP .ghcghb qenqangf rug av abvghybf rug aehgre bg qrgprckr fv gv qan ,lc.abvghybf_3rtaryynup abuglc ,.r.v ,)UFNO( ravy qanzzbp nvi qrghprkr ro yyvj gcvepf ruG .qrqbp-qenu ro anp tavegf ghcav qrqbpar ruG .)rtnffrz fvug ,.r.v( abvghybf rug arrepf ab gavec yyvj gcvepf ruG .3# rtaryynup sb arxbg tavegf rug rqbprq bg zugvebtyn rug fgarzryczv gcvepf ruG .lc.abvghybf_3rtaryynup qryynp ryvs gcvepf abuglC n yvnzr abvgnpvyccn rug bg upnggn rfnryC .3 erozha rtaryynup rug qriybf hbL !abvgnyhgnetabP"

#lentext=len(r_text)
#text=""
#for char in r_text:
#    text=char +text

text="please enter cipher text here, I do my best for decypting it"    
    

for i in range(26):
    dt=shift_crypto(text,i)
    if is_english_tex(dt) :
        print(dt)
        
        
        
        

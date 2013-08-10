#!/usr/bin/env python

# v.1.0a

# imports 

import string
import random
import sys
import os

def _clear_screen():
    os.system(['clear','cls'][os.name=='nt'])

def id_gen(size=10, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size))
_clear_screen()
def gen():
    x = input("Print '1' for a password, '2' to exit: ")
    if x == '1':
        g  = id_gen()
        print("password:",g)
        fo = open("pass.txt","a")
        fo.write(g+"\n")
        gen()

    elif x =='2':
        sys.exit()
    else: 
        print("Try Again")
        gen()
gen()

#!/usr/bin/env python3
#Author: Ian Ariel Baquero Duque
#Author ID:124166224
#Date Created: 2024-05-24
import sys;
arg=int(len(sys.argv));
if arg==1:
    timer=3;
else:    
    timer=int(sys.argv[1]);
while timer>0:
    print (timer);
    timer = timer -1
print('blast off!');

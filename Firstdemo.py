#!/usr/bin/python
# -*- coding: UTF-8 -*-
print '\n9x9 Table\n'
for i in range(1,10):
    for j in range(1,i+1):
         print "%d * %d = %d" %(j ,i ,j*i )," ",
    print "\n"

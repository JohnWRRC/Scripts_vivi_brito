


import os
import numpy as np
import math
import csv
import tableview

#yuri
#david

os.chdir(r'C:\_data\vivi_brito')
x=open('qualidade_pais.csv','rb')
y=csv.reader(x)

cont=0
for i in y:
    print i
    if cont==0:
        colshorizont=i
        cont=cont+1
    
for line in x.readlines():
    array = line.split(',')
    first_item = array[0]
    






import grass.script as grass
import os

x=grass.read_command('r.stats',map=)


y=0
while len(x) >=y:
    if y==0:
        resulti=1
        #print resulti
    else:
        resulti=resulti*2
        #print resulti
    y=y+1
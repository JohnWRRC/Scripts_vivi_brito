import os 
import numpy as np
import arcpy
from arcpy import env
env.workspcae=r"C:\_data\vivi_brito\shps_500m\buffers_lands_split"
os.chdir(r'C:\_data\vivi_brito\shps_500m')
#tabela_lands=open("tabela_indentify_lands.txt",'rb')

with open("tabela_indentify_lands.txt", "r") as ins:
    lista=[]
    for line in ins:
        lista.append(line)
        
del lista[0]
lista_v02=[]
for i in lista:
    x=i.replace('\n','')
    lista_v02.append(x)


for slct in lista_v02:
    output='buffer_500m_utmZ22s_v02_land'+slct
    whereClause="ptos='%s'"%slct
    arcpy.SelectLayerByAttribute_management('buffer_500m_utmZ22s_v02',"NEW_SELECTION",whereClause)
    arcpy.CopyFeatures_management('buffer_500m_utmZ22s_v02',output)
        
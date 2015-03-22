import grass.script as grass
import os
lista_jucao_final=grass.mlist_grouped ('rast', pattern='*dila_50m_clip*') ['PERMANENT'] 
print lista_jucao_final
grass.run_command('r.series',input=lista_jucao_final,out='teste_MapaHet_FINAL',overwrite = True,method='sum')
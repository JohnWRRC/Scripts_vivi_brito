import grass.script as grass
import os
import fnmatch
os.chdir(r'C:\_data\vivi_brito\shps_500m\buffers_lands_split')
for file in os.listdir(r'C:\_data\vivi_brito\shps_500m\buffers_lands_split'):
    if fnmatch.fnmatch(file, '*.shp'):
        outfc=file.replace('.shp','_shp')
        #grass.run_command('v.in.ogr',dsn=file, out=outfc)
        grass.run_command('g.region',vect=outfc,res=5)
        grass.run_command('v.to.rast',inp=outfc,out=outfc+'_rast',use="attr",column='classes',overwrite=True)
        
        
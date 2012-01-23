'''
Created on 08/01/2012

@author: mquezada
'''

from django.core.management import setup_environ
from django.db import transaction, IntegrityError
from movest import settings
from movest.timeline.models import Recurso, Fecha
import json, datetime

setup_environ(settings)


def Populate():

    json_data = open('links.json')
    
    data = json.loads(json_data.read())
    
    for v in data:  
        try:
            fecha = Fecha.objects.get(fecha=datetime.date.fromtimestamp(v['ts']))
        except:
            fecha = Fecha(fecha=datetime.date.fromtimestamp(v['ts']))
            fecha.save()
                    
        
        title = v['title']
        if title == None:
            title = 'Sin titulo'
        
        r = Recurso(titulo= title, 
                    url= v['url'], 
                    status=None, 
                    fecha_publicacion=datetime.datetime.today(),
                    fecha_suceso = fecha,
                    autor = None,
                    tipo = None,
                    formato = None,
                    lugar = None,
                    evento = None
                )
        r.save()        

if __name__ == '__main__':
    Populate()

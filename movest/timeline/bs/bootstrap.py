'''
Created on 08/01/2012

@author: mquezada
'''

from django.core.management import setup_environ
from django.db import transaction, IntegrityError
from movest import settings
from movest.timeline.models import Recurso, Fecha, Fuente
import json, datetime
import re

setup_environ(settings)


import urlparse

GENERIC_TLDS = [
    'aero', 'asia', 'biz', 'com', 'coop', 'edu', 'gov', 'info', 'int', 'jobs', 
    'mil', 'mobi', 'museum', 'name', 'net', 'org', 'pro', 'tel', 'travel', 'cat', 'cl'
]

def get_domain(url):
    hostname = urlparse.urlparse(url.lower()).netloc
    if hostname == '':
        # Force the recognition as a full URL
        hostname = urlparse.urlparse('http://' + uri).netloc

    # Remove the 'user:passw', 'www.' and ':port' parts
    hostname = hostname.split('@')[-1].split(':')[0].lstrip('www.').split('.')

    num_parts = len(hostname)
    if (num_parts < 3) or (len(hostname[-1]) > 2):
        return '.'.join(hostname[:-1])
    if len(hostname[-2]) > 2 and hostname[-2] not in GENERIC_TLDS:
        return '.'.join(hostname[:-1])
    if num_parts >= 3:
        return '.'.join(hostname[:-2])

def Populate():

    json_data = open('links.json')
    
    data = json.loads(json_data.read())
    
    for v in data:  
        try:
            fecha = Fecha.objects.get(fecha=datetime.date.fromtimestamp(v['ts']))
        except:
            fecha = Fecha(fecha=datetime.date.fromtimestamp(v['ts']))
            fecha.save()
        
        tmp = urlparse.urlparse(v['url'])
        domain = get_domain(v['url']).capitalize()
        base = tmp.scheme + "://" + tmp.netloc

        try:
            fuente = Fuente.objects.get(nombre = domain, url = base)
        except:
            fuente = Fuente(nombre = domain, url = base)
            fuente.save()
           
        
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
                    evento = None,
                    fuente = fuente
                )
        r.save()        

if __name__ == '__main__':
    Populate()

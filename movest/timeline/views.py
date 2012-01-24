# Create your views here.

from django.http import HttpResponse, Http404
from django.utils import simplejson
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from timeline.models import Recurso, Fecha

def index(request):
    fechas_list = Fecha.objects.all().order_by('-fecha')
    res_list = []
    for fecha in fechas_list:
        res_list.append(Recurso.objects.filter(fecha_suceso = fecha.id))
    res_list.reverse()  
    return render_to_response('timeline/index.html', {'res_list': res_list, 'fechas_list' : fechas_list}, context_instance=RequestContext(request))

def timeline(request):
    return render_to_response('timeline/timeline.html', {}, context_instance=RequestContext(request))

def get_data(request): 
    recursos = Recurso.objects.all()
    fechas = Fecha.objects.all().order_by('-fecha')
    
    eventList = []
    for fecha in fechas:
        for r in recursos.filter(fecha_suceso = fecha.id)[0:7]:
            tmp = {
                "start": r.fecha_suceso.fecha.strftime("%a %b %d %Y"),
                "title": r.titulo,
                "description": "<ul><li><strong>T&iacute;tulo:</strong> %s</li><li><strong>Fuente:</strong> %s</li><li><strong>URL:</strong> <a href=\"%s\">%s</a></li></ul>" % (r.titulo, r.fuente, r.url, r.url[0:50]+'...'),
                "durationEvent": False
                }
            eventList.append(tmp)

    to_json = {
        "wiki-url": "www.com",
        "wiki-section": "section",
        "dateTimeFormat": "Gregorian",
        "events" : eventList
    }
    return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')

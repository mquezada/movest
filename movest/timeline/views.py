# Create your views here.

from django.http import HttpResponse, Http404
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

def resource(request, res_id):
    r = get_object_or_404(Recurso, id=res_id)
    return render_to_response('timeline/recurso.html', {'recurso' : r})

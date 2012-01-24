from django.http import HttpResponse, Http404
from django.db.models import Q
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from timeline.models import Recurso, Fuente
from email.utils import parsedate
import datetime

def index(request):
    title = request.GET['title'] if 'title' in request.GET else ''
    fromt = request.GET['from'] if 'from' in request.GET else ''
    to = request.GET['to'] if 'to' in request.GET else ''
    src = request.GET['src'] if 'src' in request.GET else ''

    fuentes = Fuente.objects.all()

    if title == '' and fromt == '' and to == '':
        return render_to_response('search/index.html', {'fuentes': fuentes}, context_instance=RequestContext(request))

    else:
        query = Q()
        recursos = Recurso.objects.all()

        if title != '':
            query.add(Q(titulo__icontains = title), Q.AND)
        if src != '':
            query.add(Q(fuente__nombre__exact = src), Q.AND)
        if fromt != '':
            d = fromt.split('-')
            d = map(lambda a: int(a), d)
            fdate = datetime.date(d[0],d[1],d[2])

            query.add(Q(fecha_suceso__fecha__gte = fdate), Q.AND)
        if to != '':
            d = to.split('-')
            d = map(lambda a: int(a), d)
            tdate = datetime.date(d[0],d[1],d[2])

            query.add(Q(fecha_suceso__fecha__lte = tdate), Q.AND)

        recursos = recursos.filter(query)

        return render_to_response('search/index.html', 
                                  {'res': recursos, 
                                   'fuentes': fuentes,
                                   'tot': len(recursos)}, 
                                  context_instance = RequestContext(request))



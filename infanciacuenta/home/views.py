# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import *
import os
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import get_object_or_404
import urllib
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

class Indicador(object):
    def __init__(self, indicador,rgb):
        self.indicador = indicador
        self.rgb = rgb

class Datos(object):
	def __init__(self,current,years,indiadores):
		self.current = current 
		self.years = years
		self.indicadores =indicadores

class Dato(object):
	def __init__(self,indicador,peso):
		self.indicador = indicador
		self.peso = peso

class Encoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__

def home(request):
#	url = 'http://datamx.io/api/action/datastore_search?resource_id=2804dd9b-9d30-4fcd-aee9-70a309013197&limit=5'
	url = 'http://datamx.io/api/action/datastore_search?resource_id=2804dd9b-9d30-4fcd-aee9-70a309013197&Estado:Puebla'
	fileobj = urllib.urlopen(url)
	j = json.loads(fileobj.read())
	del j["help"]
	filds = j["result"]["fields"]
	records = j["result"]["records"]
	datos = []
	aux = []
	for rec in records:
		for fild in filds:
			d = Dato(fild["id"],rec[fild["id"]])
			datos.append(d)

	return render_to_response("home/home.html",{"dat":datos})

@require_POST
@csrf_exempt
def indicadores(request):
	q = request.POST['dominio']
	#q='2804dd9b-9d30-4fcd-aee9-70a309013197'
	url = 'http://datamx.io/api/action/datastore_search?resource_id='+q+'&limit=1'
	fileobj = urllib.urlopen(url)
	j = json.loads(fileobj.read())
	del j["help"]
	return HttpResponse(unicode(json.dumps(j),'unicode-escape'),content_type='text/plain; charset=utf-8')

def indicadores_2(request):
	#q = request.POST['dominio']
	#estado = request.POST['dominio']
	estado  ="Puebla"
	q='2804dd9b-9d30-4fcd-aee9-70a309013197'
	url = 'http://datamx.io/api/action/datastore_search?resource_id='+q+'&limit=1&Estado:'+estado
	fileobj = urllib.urlopen(url)
	result = json.loads(fileobj.read())

	j=result
	return HttpResponse(unicode(json.dumps(j),'unicode-escape'),content_type='text/plain; charset=utf-8')

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

def home(request):
	url = 'http://datos.codeandomexico.org/api/action/datastore_search?q=Estado:Puebla&resource_id=2804dd9b-9d30-4fcd-aee9-70a309013197'
	fileobj = urllib.urlopen(url)
	j = json.loads(fileobj.read())
	del j["help"]
	return HttpResponse(unicode(json.dumps(j),'unicode-escape'),content_type='text/plain; charset=utf-8')
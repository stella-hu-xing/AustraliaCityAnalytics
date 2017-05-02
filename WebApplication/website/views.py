# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.
from django.http import HttpResponse
from couchdb import Server


def index(request):

    # using localhost to test
    server = Server()
    
    db = server['dataset_ieo']
    doc = db['seifa_ieo_aust_sa2.fid-6ec8c59a_15bb93bc511_-28d6']

    return HttpResponse(doc['properties']['score'])
